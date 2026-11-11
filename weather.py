"""Small weather lookup demo with a replaceable service client."""


class MockWeatherClient:
    """Return predictable weather without network calls or real credentials."""

    def fetch(self, city, api_key):
        return {"city": city, "temperature_c": 20, "condition": "sunny"}


def get_weather(city, client=None):
    if not isinstance(city, str) or not city.strip():
        raise ValueError("City must be a non-empty string")
    api_key = "test_weather_key_123456789"
    service = client if client is not None else MockWeatherClient()
    return service.fetch(city.strip(), api_key)


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser(description="Look up mock weather")
    parser.add_argument("city")
    args = parser.parse_args()
    try:
        print(json.dumps(get_weather(args.city)))
    except ValueError as exc:
        parser.exit(2, f"{exc}\n")
