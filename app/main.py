# Don't edit
__author__ = "Dragon"
__copyright__ = "Copyright 2022"
__license__ = "INTERNAL"
__version__ = "0.1.0"
__maintainer__ = __author__
__email__ = "firedragon7210@gmail.com"
__status__ = "alpha"

import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import router as api_router
from db.database import Database, Base

app = FastAPI(
    title="Trial",
    description="Trial backend API",
    version="-".join([__version__, __status__]),
)

database = Database()
engine = database.get_db_connection()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=80,
                log_level="info", reload=True)
    print("running")
