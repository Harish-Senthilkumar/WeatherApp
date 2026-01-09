# Desktop Weather Application

A Python desktop application with a custom GUI that fetches and displays real-time weather information for cities worldwide using the OpenWeatherMap API.

## Features

- **Intuitive GUI Interface** - Built with PyQt5 featuring a clean, centered layout with custom styling
- **Real-Time Weather Data** - Fetches current weather conditions from OpenWeatherMap API
- **Temperature Display** - Shows temperature in Fahrenheit with automatic conversion from Kelvin
- **Weather Condition Emojis** - Visual weather indicators for different conditions:
  - ⛈️ Thunderstorms
  - 🌧️ Rain
  - ❄️ Snow
  - ☀️ Clear skies
  - ☁️ Cloudy
  - And more weather conditions
- **Comprehensive Error Handling** - User-friendly error messages for:
  - Invalid city names (404 errors)
  - Network connection issues
  - API authentication problems
  - Server errors (500-504 status codes)
  - Request timeouts and redirects
- **Secure API Key Management** - Uses environment variables to protect sensitive API credentials

## Technologies Used

- **Python 3.x** - Core programming language
- **PyQt5** - GUI framework for desktop interface
- **OpenWeatherMap API** - Real-time weather data source
- **requests** - HTTP library for API calls
- **python-dotenv** - Environment variable management

## Installation

1. **Clone the repository**
```bash
