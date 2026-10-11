from src.core.config import get_settings

s = get_settings()
def test_read_secrets():
    assert s.weather.base_url == "http://api.openweathermap.org/data/2.5"
    assert s.weather.api_key.get_secret_value() == '123'