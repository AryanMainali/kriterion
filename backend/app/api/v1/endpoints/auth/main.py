from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import auth, assignments, courses, submissions
# Import other routers as needed
# from app.api.v1.endpoints import admin, languages, reports


app = FastAPI(
    title="Kriterion API",
    description="API for the Kriterion Automated Grading System.",
    version="1.0.0",
)

# --- CORS Configuration ---
# This is the crucial part to fix the login errors.
# It allows your frontend (on Vercel) to communicate with your backend (on Railway).

# IMPORTANT: Replace the placeholder with your actual Vercel frontend URL.
# You can find this in your Vercel project settings.
# For development, you might also want to allow localhost.
origins = [
    "http://localhost:3000",  # For local frontend development
    "https://kriterion.vercel.app",  # <-- REPLACE THIS
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allows cookies and authorization headers
    allow_methods=["*"],     # Allows all HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],     # Allows all headers
)


@app.get("/")
def read_root():
    """A simple endpoint to confirm the API is running."""
    return {"message": "Welcome to the Kriterion API"}


# --- API Routers ---
# Include the routers from your different API endpoint modules.
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(assignments.router, prefix="/api/v1/assignments", tags=["Assignments"])
app.include_router(courses.router, prefix="/api/v1/courses", tags=["Courses"])
app.include_router(submissions.router, prefix="/api/v1/submissions", tags=["Submissions"])
# ... include other routers here
