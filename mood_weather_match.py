def mood_weather_match(mood: str, weather: str) -> bool:
    try:
        # Define a map of moods to corresponding weather conditions
        mood_weather_map = {
            "happy": ["clear sky", "few clouds", "scattered clouds", "broken clouds"],
            "sad": ["rain", "thunderstorm", "drizzle", "light rain", "shower rain"],
            "calm": ["mist", "overcast clouds", "fog", "smoke", "haze"],
            "angry": ["storm", "heavy rain", "thunderstorm with heavy rain", "thunderstorm with light rain"],
            "excited": ["clear sky", "few clouds", "thunderstorm"],
            "relaxed": ["clear sky", "few clouds", "mist", "light rain"]
        }

        # Get the mood-specific weather conditions from the map
        mood_conditions = mood_weather_map.get(mood, [])

        if any(condition in weather for condition in mood_conditions):
            return True  # Mood matches weather
        return False  # Mood does not match weather

    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Return False in case of any error