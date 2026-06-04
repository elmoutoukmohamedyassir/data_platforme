from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API is running"}


@router.get("/status")
def status():
    return {
        "status": "ok",
        "service": "data_platform",
        "version": "0.1"
    }


@router.get("/ping")
def ping():
    return {"message": "pong"}













