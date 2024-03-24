from uvicorn import Config

config = Config(".env")
SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")