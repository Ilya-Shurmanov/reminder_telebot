from fastapi import FastAPI
from api.routes import router


# Create an instance of the FastAPI class
app = FastAPI()

# Import and include your API routers here


app.include_router(router)

# If you want to run the application directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
