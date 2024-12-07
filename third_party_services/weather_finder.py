
import requests
from fastapi import HTTPException
from local import api_key_weather_finder

def get_weather_description(city: str) -> str:

    try:
        # Construct the URL for the weather API
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        url = f"{base_url}q={city}&appid={api_key_weather_finder}"

        # Send a GET request to the weather API and parse the JSON response
        response = requests.get(url).json()

        if response.get("weather"):
            return response['weather'][0]['description']
        else:
            raise HTTPException(status_code=404, detail="City not found")

    except requests.RequestException as e:
        # Handle request-related errors
        raise HTTPException(status_code=500, detail=f"Error fetching weather data: {e}")

    except KeyError:
        # Handle missing data or unexpected response format
        raise HTTPException(status_code=500, detail="Unexpected response format from weather API")

    except Exception as e:
        # Handle other unexpected errors
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")