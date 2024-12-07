import requests
from local import api_key_mood_songs
from fastapi import HTTPException

def recommend_song(mood: str) -> dict:

    try:
        # Define the URL for the song recommendation API
        url = "http://ws.audioscrobbler.com/2.0/"

        # Define parameters for the request to the song recommendation API
        params = {
            "method": "tag.gettoptracks",
            "tag": mood,
            "api_key": api_key_mood_songs,
            "format": "json",
            "limit": 10
        }

        response = requests.get(url, params=params).json()

        songs = []  # Initialize an empty list to store songs

        if "tracks" in response and "track" in response["tracks"]:
            tracks = response["tracks"]["track"]
            for track in tracks[:10]:
                songs.append({
                    "artist": track["artist"]["name"],
                    "title": track["name"],
                    "url": track["url"]
                })

        return songs

    except requests.RequestException as e:
        # Handle request-related errors, such as network issues or timeouts
        raise HTTPException(status_code=500, detail=f"Error fetching song recommendations: {e}")

    except Exception as e:
        # Handle other unexpected errors
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")