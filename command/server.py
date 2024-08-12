from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.index import init_api_list
from infrastructure.mysql import engine, Base

class ServerCreator:
    def __init__(self):
        self.app = FastAPI()
        self.init_router()
        self.init_cors()

    def init_router(self):
        init_api_list(self.app)

    def init_cors(self):
        # CORS configuration
        origins = [
            "http://localhost",
            "http://127.0.0.1",
            "http://127.0.0.1:8009",
        ]

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def get_app(self):
        return self.app

    def database_init(self):
        Base.metadata.create_all(bind=engine)


server_creator = ServerCreator()
server_creator.database_init()
app = server_creator.get_app()
