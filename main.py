import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database.connection import Settings
from routes.events import event_router
from routes.users import user_router


settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
  await settings.initialize_database()
  yield

app = FastAPI(lifespan=lifespan)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# @app.on_event("startup")
# async def init_db():
#   await settings.initialize_database()

@app.get("/")
async def home():
  return RedirectResponse(url="/event/")
