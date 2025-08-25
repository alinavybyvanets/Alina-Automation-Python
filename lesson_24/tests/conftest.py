import os
import json
import pytest
import logging
import requests
from requests.auth import HTTPBasicAuth
from typing import Generator

LOG_FILE = "test_search.log"

@pytest.fixture(scope="session", autouse=True)
def _configure_logging() -> None:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    for h in list(logger.handlers):
        logger.removeHandler(h)
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    ch =  logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    fh = logging.FileHandler(LOG_FILE, mode ="w", encoding ="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.info("Logging configured. File: %s ", LOG_FILE)

@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("CARS_API_URL", "http://127.0.0.1:8080")

@pytest.fixture(scope="session")
def creds() -> tuple[str, str]:
    username = os.getenv("CARS_API_USERNAME", "test_user")
    password = os.getenv("CARS_API_PASSWORD", "test_pass")
    return username, password

@pytest.fixture(scope="class")
def session_auth(base_url: str, creds: tuple[str, str]) -> Generator[requests.Session, None, None]:
    logger = logging.getLogger("session_auth")
    s = requests.Session()

    username, password = creds
    auth_url = f'{base_url}/auth'
    logger.info("Authenticating at %s as '%s' ...", auth_url, username)
    resp = s.post(auth_url, auth=HTTPBasicAuth(username, password), timeout=10)
    logger.debug("Auth response: %s", resp.text)

    assert resp.status_code == 200, f'Auth failed (HTTP {resp.status_code} ): {resp.text}'
    try:
        payload = resp.json()
    except json.JSONDecodeError:
        raise AssertionError(f'Auth did not return JSON. Raw: {resp.text!r}')

    access_token = payload.get("access_token")
    assert access_token, f'No access_token in auth response. Got: {payload!r}'

    s.headers.update({"Authorization": f'Bearer {access_token}'})
    logger.info("Authenticated. Token stored in session headers.")
    try:
        yield s
    finally:
        s.close()
        logger.info("Session closed.")
