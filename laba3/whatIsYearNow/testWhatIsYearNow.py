import pytest
import what_is_year_now
from unittest.mock import patch


def test_format_v1():
    json_return_value = {
        "$id": "1",
        "currentDateTime": "2022-04-09T19:29Z",
        "utcOffset": "00:00:00",
        "serviceResponse": "null"
    }
    with patch('json.load', return_value=json_return_value):
        year = what_is_year_now.what_is_year_now()
        assert year == 2022


def test_format_v2():
    json_return_value = {
        "$id": "1",
        "currentDateTime": "09.04.2023T19:29Z",
        "utcOffset": "00:00:00",
        "isDayLightSavingsTime": "false",
        "dayOfTheWeek": "Friday",
        "timeZoneName": "UTC",
        "currentFileTime": 132624701535543575,
        "ordinalDate": "2023-99",
        "serviceResponse": "null"
    }
    with patch('json.load', return_value=json_return_value):
        year = what_is_year_now.what_is_year_now()
        assert year == 2023


def test_exception_format():
    json_return_value = {
        "$id": "1",
        "currentDateTime": "2024/04/09T19:29Z",
        "utcOffset": "00:00:00",
        "isDayLightSavingsTime": "false",
        "dayOfTheWeek": "Friday",
        "timeZoneName": "UTC",
        "currentFileTime": 132624701535543575,
        "ordinalDate": "2021-99",
        "serviceResponse": "null"
    }
    with patch('json.load', return_value=json_return_value), pytest.raises(Exception):
        what_is_year_now.what_is_year_now()
