from configuration.server import Server


def create_app():
    return Server().app


app = create_app()
