import os
import unittest
from unittest.mock import Mock, patch

from weather import get_weather


class WeatherTests(unittest.TestCase):
    @patch.dict(os.environ, {"WEATHER_API_KEY": "test-only-placeholder"}, clear=True)
    def test_passes_environment_key_and_trimmed_city_to_client(self):
        client = Mock()
        client.fetch.return_value = {"city": "London", "temperature_c": 20}
        result = get_weather(" London ", client)
        client.fetch.assert_called_once_with("London", "test-only-placeholder")
        self.assertEqual(result, client.fetch.return_value)
        self.assertNotIn("test-only-placeholder", str(result))

    @patch.dict(os.environ, {}, clear=True)
    def test_missing_key(self):
        with self.assertRaisesRegex(ValueError, "WEATHER_API_KEY"):
            get_weather("London")

    def test_invalid_city(self):
        for city in (None, "", "   ", 42):
            with self.subTest(city=city):
                with self.assertRaisesRegex(ValueError, "City"):
                    get_weather(city)

    @patch.dict(os.environ, {"WEATHER_API_KEY": "   "}, clear=True)
    def test_blank_key(self):
        with self.assertRaisesRegex(ValueError, "WEATHER_API_KEY"):
            get_weather("London")

    @patch.dict(os.environ, {"WEATHER_API_KEY": "test-only-placeholder"}, clear=True)
    def test_mock_weather(self):
        self.assertEqual(get_weather("London"), {
            "city": "London", "temperature_c": 20, "condition": "sunny"
        })


if __name__ == "__main__":
    unittest.main()
