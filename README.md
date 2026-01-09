# Weather Desktop Application

A Python-based desktop weather application with a graphical user interface that fetches and displays real-time weather information for any city in the world.

## Features
- Clean and intuitive GUI built with PyQt5
- Real-time weather data from OpenWeatherMap API
- Temperature display in Fahrenheit
- Weather condition descriptions with emoji icons
- Comprehensive error handling for network issues and invalid inputs
- Secure API key management using environment variables

## Technologies Used
- Python
- PyQt5 (GUI framework)
- OpenWeatherMap API
- requests library
- python-dotenv

## Installation
1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Create a `.env` file and add your OpenWeatherMap API key: `OPENWEATHER_API_KEY=your_api_key_here`
4. Run the application: `python weather_app.py`

## Requirements
- Python 3.x
- PyQt5
- requests
- python-dotenv
