from fastapi import FastAPI

app = FastAPI(title="Romaha ID - Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}
