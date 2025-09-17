from fastapi import FastAPI

from routes import basic_routes, cannedjson_routes

app = FastAPI()
app.include_router(basic_routes.router)
app.include_router(cannedjson_routes.router)
