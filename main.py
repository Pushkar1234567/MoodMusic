from fastapi import FastAPI,HTTPException
from third_party_services.weather_finder import get_weather_description
from third_party_services.song_recommend import recommend_song
from mood_weather_match import mood_weather_match
from serializers import MoodCityRequest

# Create FastAPI app instance
app = FastAPI()

# Endpoint for a simple "Hello World" message
@app.get("/hello")
def hello():
    return {"message": "Hello World"}

# Endpoint for recommendation based on mood and city
@app.post("/recommend/")
def get_recommendation(request: MoodCityRequest):
    # Extract mood and city from request
    mood = request.mood
    if not mood:
        raise HTTPException(status_code=400, detail="Mood is required")

    city = request.city
    if not city:
        raise HTTPException(status_code=400, detail="City is required")

    try:
        # Get weather description for the city
        weather_description = get_weather_description(city)
        
        # Check if mood matches the weather description
        if mood_weather_match(mood, weather_description):
            # Recommend a song based on the mood
            song = recommend_song(mood)
            if song:
                # If song recommendation found
                return {
                    "mood": mood,
                    "city": city,
                    "weather": weather_description,
                    "song": song
                }
            else:
                # If no song recommendation found
                raise HTTPException(status_code=404, detail="No song recommendations found for the given mood")
        else:
            # If mood does not match weather description
            return {
                "message": "The current weather does not match your mood",
                "mood": mood,
                "city": city,
                "weather": weather_description,
            }

    except Exception as e:
        # Handle unexpected errors and raise HTTPException with 500 status code
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")