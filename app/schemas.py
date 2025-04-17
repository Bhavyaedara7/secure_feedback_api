 from pydantic import BaseModel, EmailStr

# User Base Schema
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None

# Schema for User Registration
class UserCreate(UserBase):
    password: str

# Schema for outputting user info (excluding password)
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

