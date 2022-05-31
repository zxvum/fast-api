from fastapi import FastAPI
import uvicorn

from app import models, router
from app import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router.router)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)