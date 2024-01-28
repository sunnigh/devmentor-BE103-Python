from api.general.routes import routers
# from api.v1.routes import routers as v1_routes


def init_api_list(app):
    app.include_router(
        routers,
    )

    # app.include_router(
    #     # v1_routes,
    #     prefix="/v1/services",
    # )

    return
