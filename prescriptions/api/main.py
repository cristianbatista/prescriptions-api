from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from prescriptions.api.endpoints.health import router as health_router
from prescriptions.api.endpoints.prescriptions import router as prescriptions_router
from prescriptions.api.error_handling import init_error_handling
from prescriptions.config import settings
from prescriptions.infrastructure.postgre import create_engine_db, create_session_local
from prescriptions.models.prescription_model import Base


def create_app():
    app = FastAPI(title=settings.PROJECT_NAME)

    # Setup event handlers
    @app.on_event("startup")
    async def startup() -> None:
        create_session_local()
        Base.metadata.create_all(create_engine_db())

    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Define routers
    app.include_router(health_router, tags=["health"], prefix="/health")
    app.include_router(
        prescriptions_router, tags=["prescriptions"], prefix="/prescriptions"
    )

    init_error_handling(app)

    return app


app = create_app()
