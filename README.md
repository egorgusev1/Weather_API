# Weather App

![Weather App Screenshot](/images/weather_app.png)

## [Live Demo](https://weather-app-nine-sigma-76.vercel.app/)

A modern weather application that automatically detects user location and provides real-time weather updates and forecasts.

## ⚠️ Important Note

**You must place the `.env` file inside the `weather_app` directory, not in the root directory.**

This is critical for the application to function properly, as it looks for environment variables in the `weather_app` folder.

## Features

- **Automatic Location Detection**: Identifies your city from your IP address
- **Current Weather**: Displays temperature, conditions, and other key metrics
- **5-Day Forecast**: Shows upcoming weather trends at a glance
- **Custom Location Search**: Get weather for any city worldwide
- **Responsive Design**: Works on desktop and mobile devices

## Quick Start

### Prerequisites

Before getting started, you'll need API keys from:
1. [OpenWeatherMap](http://api.openweathermap.org) - For weather data
2. [IPInfo](https://ipinfo.io) - For IP-based location detection

## Project Structure

```
Weather_API/
├── __pycache__/
├── images/
├── venv/
├── weather_app/           # Main application directory
│   ├── __pycache__/
│   ├── templates/         # HTML templates
│   ├── main.py            # Application entry point
│   ├── .env               # Place your API keys here! 
│   └── ...
├── install_requirements.sh
├── README.md
├── requirements.txt
└── vercel.json
```

### Installation

#### macOS / Linux

```bash
# Clone the repository
git clone https://github.com/egorgusev1/Weather_API.git

# Navigate to the project directory
cd Weather_App

# Install dependencies
chmod +x install_requirements.sh
./install_requirements.sh

# Create .env file with your API keys
# IMPORTANT: Create this file inside the weather_app directory
cd weather_app
echo "API_KEY = \"Your OpenWeatherMap API key\"" > .env
echo "IPINFO_TOKEN = \"Your IPInfo token\"" >> .env
cd ..
```

#### Windows

```powershell
# Clone the repository
git clone https://github.com/egorgusev1/Weather_API.git

# Navigate to the project directory
cd Weather_App

# For Windows, manually install the requirements
pip install -r requirements.txt

# Create .env file with your API keys
# IMPORTANT: Create this file inside the weather_app directory
cd weather_app
# Either create this file manually or use these commands:
echo API_KEY = "Your OpenWeatherMap API key" > .env
echo IPINFO_TOKEN = "Your IPInfo token" >> .env
cd ..
```

### Running the Application

#### macOS / Linux

```bash
# Navigate to the weather_app directory
cd weather_app

# Start the application
python3 main.py
```

#### Windows

```powershell
# Navigate to the weather_app directory
cd weather_app

# Start the application
# Use python or py depending on your installation
python main.py
# OR
py main.py
```

The application will be available at `http://localhost:5000`

### Running Tests

#### macOS / Linux

```bash
pytest
```

#### Windows

```powershell
python -m pytest
# OR
py -m pytest
```

## API Endpoints

The application provides the following endpoints:

- **`GET /`**: Main page that displays the weather interface
  - Automatically detects user location on initial load
  - Accepts POST requests with a city name for manual searches

- **`GET /api/weather`**: JSON API endpoint for programmatic access
  - Query parameters:
    - `city` (optional): City name to get weather for
  - Returns weather data in JSON format including current conditions and forecast
  - Uses IP-based location detection if no city is specified

## Technologies

- Flask web framework
- OpenWeatherMap API
- IPInfo geolocation services
- Responsive front-end design

## Contributors

- [Mohamed Amara](https://github.com/Shaku-Med)
- [Mykola Demianiuk](https://github.com/Demianiuk-Mykola)
- [Egor Gusev](https://github.com/egorgusev1)

<!-- Pull request. -->