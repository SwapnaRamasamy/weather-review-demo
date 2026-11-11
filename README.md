# Weather Review Demo

A minimal Python project for testing automated code review. Requires Python 3.9 or newer and no third-party packages.

## Run

PowerShell:

```powershell
$env:WEATHER_API_KEY = "local-mock-placeholder"
python weather.py London
```

The default client returns mock data. No network requests are made and no real API key is needed. The key is read from the environment and never included in output. `.env.example` documents the variable; this project does not automatically load `.env` files.

## Test

```powershell
python -m unittest discover -v
```

## Review exercise

The main branch is the clean baseline. A later pull request can deliberately replace the environment configuration with a fake hardcoded test API key to evaluate a reviewer. Never use a real credential for this exercise.
