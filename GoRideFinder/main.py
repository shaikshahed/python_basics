from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/db_name"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# OAuth2PasswordBearer for handling token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Logic to verify the token and get the current user
    return token

# API endpoint for user registration
@app.post("/register", response_model=dict)
def register_user(username: str, email: str, password: str):
    # Logic to create a new user in the database
    return {"message": "User registered successfully"}

# Example protected route (requires authentication)
@app.get("/protected-route")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
