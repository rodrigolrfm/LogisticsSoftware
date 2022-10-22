from threading import Thread
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.mainrouter import router as mainrouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from typing import Callable
import logging
from threading import Thread


def get_application() -> FastAPI:
	application = FastAPI()
	application.include_router(mainrouter)

	origins = ["*"]

	application.add_middleware(
	    CORSMiddleware,
	    allow_origins=origins,
	    allow_credentials=True,
	    allow_methods=["*"],
	    allow_headers=["*"],
	)

	return application

app = get_application()