from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Deployment Observability API",
        "status": "ready",
        "deployment_id": "ga2-a34366"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("APP_PORT", 7007))
    uvicorn.run(app, host="0.0.0.0", port=port)
