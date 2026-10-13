from src.core.config import get_settings

s = get_settings()
def test_read_secrets():
    assert s.weather.base_url == "http://api.openweathermap.org/data/2.5"
    assert s.weather.api_key.get_secret_value() == '123'

'''from ip to geo
{'city': {
    'name': 'St Petersburg', 
    'names': {
        'en': 'St Petersburg', 
        'de': 'Sankt Petersburg', 
        'es': 'San Petersburgo', 
        'fa': 'سن پترزبورگ', 
        'fr': 'Saint-Pétersbourg', 
        'ja': 'サンクトペテルブルク', 
        'ko': '상트페테르부르크', 
        'pt-BR': 'São Petersburgo', 
        'ru': 'Санкт-Петербург', 
        'zh-CN': '聖彼得堡'
    }
    }, 
    'country': {
        'name': 'Russia', 
        'iso_code': 'RU', 
        'names': {
            'en': 'Russia', 
            'de': 'Russische Föderation', 
            'es': 'Rusia, (la) Federación de', 
            'fa': 'روسیه', 'fr': 'Russie, Fédération de', 
            'ja': 'ロシア', 
            'ko': '러시아', 
            'pt-BR': 'Rússia', 
            'ru': 'Россия', 
            'zh-CN': '俄罗斯'
        }, 
        'geoname_id': 2017370, 
        'name_native': 'Россия', 
        'phone_code': '7', 
        'capital': 'Moscow', 
        'currency': 'RUB', 
        'flag': '🇷🇺', 
        'languages': [
            {
                'iso_code': 'ru', 
                'name': 'Russian', 
                'name_native': 'Русский'
            }
            ]
    }, 
    'state': 
    {
        'name': 'St.-Petersburg'
    }, 
    'location': 
    {
        'latitude': 59.9311, 
        'longitude': 30.3609
    }, 
    'continent': 
    {
        'code': 'EU', 
        'name': 'Europe', 
        'names': 
        {
            'de': 'Europa', 
            'en': 'Europe', 
            'es': 'Europa', 
            'fa': 'اروپا', 
            'fr': 'Europe', 
            'ja': 'ヨーロッパ', 
            'ko': '유럽', 
            'pt-BR': 'Europa', 
            'ru': 'Европа', 
            'zh-CN': '欧洲'
        }, 
        'geoname_id': 6255148
    }, 
    'subdivisions': [
        {
            'names': 
            {
                'en': 'St.-Petersburg', 
                'de': 'Sankt Petersburg', 
                'es': 'San Petersburgo', 
                'fa': 'سن\u200cپترزبورگ', 
                'fr': 'Saint-Pétersbourg', 
                'ja': 'サンクトペテルブルグ', 
                'ko': '상트페테르부르크', 
                'pt-BR': 'São Petersburgo', 
                'ru': 'Санкт-Петербург'
            }
        }, 
        {
            'names': 
            {
                'en': 'St.-Petersburg', 
                'de': 'Sankt Petersburg', 
                'es': 'San Petersburgo', 
                'fa': 'سن\u200cپترزبورگ', 
                'fr': 'Saint-Pétersbourg', 
                'ja': 'サンクトペテルブルグ', 
                'ko': '상트페테르부르크', 
                'pt-BR': 'São Petersburgo', 
                'ru': 'Санкт-Петербург'
            }
        }
    ], 
    'ip': '92.62.62.157'
}
'''

''' location from city name
{'results': [
    {
        'datasource': {
            'sourcename': 'openstreetmap', 
            'attribution': '© OpenStreetMap contributors', 
            'license': 'Open Database License', 
            'url': 'https://www.openstreetmap.org/copyright'
        }, 
        'name':'Berlin', 
        'ref': 'BE', 
        'other_names': {
            'name:km': 'ប៊ែរឡាំង',
        }, 
        'country': 'Germany', 
        'country_code': 'de', 
        'city': 'Berlin', 
        'iso3166_2': 'DE-BE', 
        'lon': 13.3951309, 
        'lat': 52.5173885, 
        'state': 'Berlin', 
        'state_code': 'BE', 
        'result_type': 'city', 
        'formatted': 'Berlin, Germany', 
        'address_line1': 'Berlin', 
        'address_line2': 'Germany', 
        'category': 'administrative', 
        'timezone': {
            'name': 'Europe/Berlin', 
            'offset_STD': '+01:00', 
            'offset_DST': '+02:00', 
            'offset_STD_seconds': 3600, 
            'offset_DST_seconds': 7200, 
            'abbreviation_STD': 'CET', 
            'abbreviation_DST': 'CEST'
        }, 
        'plus_code': '9F4MG98W+X3', 
        'plus_code_short': 'G98W+X3 Berlin, Germany', 
        'rank': {
            'importance': 0.8522196536088086, 
            'popularity': 8.995467104553104, 
            'confidence': 0, 
            'confidence_city_level': 0, 
            'match_type': 'full_match'
        }, 
        'place_id': '513147ea984eca2a4059cb694fc939424a40f00101f901d6f3000000000000c002089203064265726c696e', 
        'bbox': {
            'lon1': 13.088345, 
            'lat1': 52.3382448, 
            'lon2':13.7611609, 
            'lat2': 52.6755087
        }
    }, 
    {
        'country_code': 'de', 
        'name': 'Berlin', 
        'country': 'Germany', 
        'datasource': {
            'sourcename': 'whosonfirst', 
            'attribution': "Who's On First", 
            'license': 'CC0', 
            'url': 'https://www.whosonfirst.org/docs/licenses/'
        }, 
        'state': 'Berlin', 
        'state_code': 'BE', 
        'district': 'Berlin', 
        'city': 'Berlin', 
        'iso3166_2': 'DE-BE', 
        'lon': 13.407032, 
        'lat': 52.524932, 
        'result_type': 'city', 
        'formatted': 'Berlin, BE, Germany', 
        'address_line1': 'Berlin', 
        'address_line2': 'BE, Germany', 
        'timezone': {
            'name': 'Europe/Berlin', 
            'offset_STD': '+01:00', 
            'offset_DST': '+02:00', 
            'offset_STD_seconds': 3600, 
            'offset_DST_seconds': 7200, 
            'abbreviation_STD': 'CET', 
            'abbreviation_DST': 'CEST'
        }, 
        'plus_code': '9F4MGCF4+XR', 
        'plus_code_short': 'F4+XR Berlin, Germany', 
        'rank': {
            'popularity': 8.995467104553104, 
            'confidence': 0, 
            'confidence_city_level': 0, 
            'match_type': 'full_match'
        }, 
        'place_id': '51d7d9907f66d02a4059db4fc6f830434a40c002089203064265726c696ee2031e77686f736f6e66697273743a6c6f63616c6974793a313031393039373739', 
        'bbox': {
            'lon1': 13.088333, 
            'lat1': 52.338242, 
            'lon2': 13.760469, 
            'lat2': 52.674917
        }
    }
'''

"""
current weather response data

{'datetime': '17:00:00', 'datetimeEpoch': 1791903600, 'temp': 14.8, 'feelslike': 14.8, 'humidity': 55.39, 'dew': 5.7, 'precip': 0.0, 'precipprob': 0.0, 'snow': 0.0, 'snowdepth': 0.0, 'preciptype': None, 'windgust': 28.4, 'windspeed': 12.9, 'winddir': 176.0, 'pressure': 1022.0, 'visibility': 24.1, 'cloudcover': 92.0, 'solarradiation': 128.0, 'solarenergy': 0.5, 'uvindex': 1.0, 'severerisk': 0.0, 'conditions': 'Overcast', 'icon': 'cloudy', 'stations': None, 'source': 'fcst', 'sunrise': '07:29:10', 'sunriseEpoch': 1791869350, 'sunset': '18:17:51', 'sunsetEpoch': 1791908271, 'moonphase': 0.09}
"""