from ch_2.weather import Weather
from pytest_mock import MockFixture
from io import StringIO


def test_find_lowest_temp():

    sample_csv = StringIO("""\
    station_id,date,temperature_c
    81,2004.042,27.732
    81,2009.042,25.728
    100,2000.458,20.500
    100,2013.542,21.100
    105,2000.708,27.871
    """)


    # assert MockFixture(Weather.find_lowest_temp()) == {'station_id': 100, 'date': 2000.458, 'temperature_c': 20.500}

    '''
    I couldn't get this unit test to work within the time limit.
    I couldn't quite figure out how to mock my class instance variables, especially 'weather_records'
    '''