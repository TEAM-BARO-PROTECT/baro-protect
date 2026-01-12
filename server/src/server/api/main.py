from fastapi import FastAPI
from .settings import ApiSettings

settings = ApiSettings()

app = FastAPI(
    title="Baro Protect API",
    debug=settings.api_debug,
)

# Health check endpoint
@app.get("/health")
async def health_check():
	return {"status": "ok"}