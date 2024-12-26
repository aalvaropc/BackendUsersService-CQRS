from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CreateUserRequest(BaseModel):
    name: str = Field(..., title="User's Name", max_length=100, example="John Doe")
    email: EmailStr = Field(..., title="User's Email", example="persona@example.com")
    password: str = Field(
        ..., 
        title="User's Password", 
        min_length=8, 
        max_length=128, 
        example="securepassword123",
        description="The password must be at least 8 characters long."
    )

class UpdateUserRequest(BaseModel):
    name: Optional[str] = Field(None, title="User's Name", max_length=100, example="John Doe")
    email: Optional[EmailStr] = Field(None, title="User's Email", example="persona@example.com")
