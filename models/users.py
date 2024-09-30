from beanie import Document

from pydantic import BaseModel, EmailStr, ConfigDict


class User(Document):
  email: EmailStr
  password: str

  class Settings:
    name = "users"

  model_config = ConfigDict(
    json_schema_extra = {
        "example": {
            "email": "fastapi@packt.com",
            "password": "strong!!!"
        }
    }
  )


class TokenResponse(BaseModel):
  access_token: str
  token_type: str
