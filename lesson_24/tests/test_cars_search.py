import logging
from typing import Any, Iterable, Optional
import pytest
import requests

logger = logging.getLogger(__name__)
def _is_sorted(items:Iterable[Any]) -> bool:
    it = iter(items)
    try:
        prev = next(it)
    except StopIteration:
        return True
    for cur in it:
        if prev > cur:
            return False
        prev = cur
    return True


class TestCarsSearch:
    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 1),
            ("year", 5),
            ("engine_volume", 10),
            ("brand", 20),
            (None, 25),
            ("price", None),
            ("year", 30),
        ],
    )

    def test_search_cars_param(self, session_auth, base_url: str, sort_by: Optional[str], limit: Optional[int]):
        params = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = limit

        url = f'{base_url}/cars'
        logger.info("GET %s with params=%s", url, params)

        resp = session_auth.get(url, params=params, timeout=10)
        logger.info("Response %s", resp.status_code)
        logger.debug("Body: %s", resp.text)

        assert resp.status_code == 200, f'Unexpected status code: {resp.status_code} Body: {resp.text}'
        data = resp.json()
        assert isinstance(data, list), f'Expected a list, got {type(data).__name__}. Body: {resp.text}'

        if data:
            sample = data[0]
            assert isinstance(sample, dict), f'Expected dict items, got {type(sample).__name__}'
            for key in ("brand", "year", "engine_volume", "price"):
                assert key in sample, f"Missing key '{key}' in car item: {sample}"

        if limit is not None and isinstance(limit, int) and limit > 0:
            assert len(data) <= limit, f'Returned {len(data)} items, expected <=  {limit}'

        if sort_by is not None and data:
            try:
                column = [row[sort_by] for row in data]
            except KeyError as e:
                pytest.fail(f"Server did not return field '{sort_by}' in items. Error: {e}")
            assert _is_sorted(column), f"Data is not sorted ascending by '{sort_by}': {column}"

    def test_requires_auth(self, base_url: str):
        url = f'{base_url}/cars'
        logger.info("GET %s without auth", url)
        resp = requests.get(url, timeout=10)
        logger.info("Unauthenticated response %s", resp.status_code)
        assert resp.status_code in {401, 403,422}, f'Expected auth error, got  {resp.status_code}'
