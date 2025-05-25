from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health Check"])


@router.get("/", summary="Health Check", description="Check if the server is running")
async def health_check():
    """
    Health check endpoint to verify the server is running.
    """
    return {"status": "ok", "message": "Server is running"}
