from apis.auth.views import sub_router as router
from apis.schema import APIResponse

router = router("/ldap", tag=["LDAP Authentication"])


@router.get("/login", summary="Login", description="User login")
async def login():
    """
    Login endpoint for user authentication.
    """
    return APIResponse.success({"status": "ok", "message": "User logged in successfully"})
