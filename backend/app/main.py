from fastapi import FastAPI

app = FastAPI(
    title="Eidolon Nous",
    description="A local-first AI simulation engine.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "project": "Eidolon Nous",
        "status": "Running",
        "message": "Hello from Eidolon Nous!"
    }