import pytest
import what_is_year_now
from unittest.mock import patch, MagicMock


@patch('urllib.request.urlopen')
def test_format_v1(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",\
        "currentDateTime":"2021-04-09T19:29Z",\
        "utcOffset":"00:00:00",\
        "isDayLightSavingsTime":false,\
        "dayOfTheWeek":"Friday",\
        "timeZoneName":"UTC",\
        "currentFileTime":132624701535543575,\
        "ordinalDate":"2021-99",\
        "serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021


@patch('urllib.request.urlopen')
def test_format_v2(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",\
        "currentDateTime":"09.04.2021T19:29Z",\
        "utcOffset":"00:00:00",\
        "isDayLightSavingsTime":false,\
        "dayOfTheWeek":"Friday",\
        "timeZoneName":"UTC",\
        "currentFileTime":132624701535543575,\
        "ordinalDate":"2021-99",\
        "serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021


@patch('urllib.request.urlopen')
def test_exception_format(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",\
        "currentDateTime":"2021/04/09T19:29Z",\
        "utcOffset":"00:00:00",\
        "isDayLightSavingsTime":false,\
        "dayOfTheWeek":"Friday",\
        "timeZoneName":"UTC",\
        "currentFileTime":132624701535543575,\
        "ordinalDate":"2021-99",\
        "serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    with pytest.raises(Exception):
        what_is_year_now.what_is_year_now()
