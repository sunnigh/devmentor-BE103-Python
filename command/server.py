from fastapi import FastAPI

from api.index import init_api_list


class ServerCreator:
    def __init__(self):
        self.app = FastAPI()
        self.init_router()

    def init_router(self):
        # init_example_app(self.app)
        init_api_list(self.app)

    def get_app(self):
        return self.app


server_creator = ServerCreator()
app = server_creator.get_app()
