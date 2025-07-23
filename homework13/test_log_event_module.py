import os
import pytest
from log_event_module import log_event, logger, LOG_FILE
def read_log_file():
    with open(LOG_FILE, "r") as f:
        return f.read()
def test_success_login():
    log_event("alina", "success")
    logs = read_log_file()
    assert "INFO" in logs
    assert "Username: alina, Status: success" in logs
def test_expired_login():
    log_event("malina", "expired")
    logs = read_log_file()
    assert "WARNING" in logs
    assert "Username: malina, Status: expired" in logs
def test_failed_login():
    log_event("oksana", "failed")
    logs = read_log_file()
    assert "ERROR" in logs
    assert "Username: oksana, Status: failed" in logs
def test_unknown_login():
    log_event("mirco", "invalid")
    logs = read_log_file()
    assert "ERROR" in logs
    assert "Username: mirco, Status: invalid" in logs


