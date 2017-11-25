import pytest
from pytest import fixture
from tmdbwrapper import TV
import vcr



@fixture
def tv_keys():
    # Responsible only for returning the test data
    return ['id', 'origin_country', 'poster_path', 'name',
              'overview', 'popularity', 'backdrop_path',
              'first_air_date', 'vote_count']

def utv_keys():
    return [u'origin_country', u'poster_path', u'name',
            u'overview', u'popularity', u'original_name',
            u'id', u'vote_average', u'vote_count', u'first_air_date',
            u'original_language', u'backdrop_path', u'genre_ids']

@vcr.use_cassette('tests/vcr_cassettes/tv-info.yml', filter_query_parameters=['api_key'])
def test_tv_info(tv_keys):
    """Tests an API call to get a TV show's info"""

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
    assert set(tv_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml', filter_query_parameters=['api_key'])
def test_tv_popular(tv_keys):
    response = TV.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    assert set(tv_keys).issubset(response['results'][0].keys())
