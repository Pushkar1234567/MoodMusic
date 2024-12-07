from pydantic import BaseModel,validator

class MoodCityRequest(BaseModel):
    mood: str
    city: str

    # Validator method to convert mood and city to lowercase
    @validator('mood', 'city')
    def convert_to_lowercase(cls, v):
        if isinstance(v, str):
            return v.lower()
        return v