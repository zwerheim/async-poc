import connexion
from connexion.resolver import RestyResolver

import os


# app = connexion.AioHttpApp(__name__, specification_dir='specs/')
# app.add_api('service.yaml', resolver=RestyResolver('api'))
# app.app.errorhandler(BaseUtilsException)(handle_exception)

def create_app():
    """ Create an application instance for adev to pickup up

    Returns:
        aiohttp.web.Application instance
    """
    app = connexion.AioHttpApp(__name__, specification_dir='specs/', port=8000)
    app.add_api(
        'service.yaml',
        resolver=RestyResolver('api'),
        strict_validation=True,
        validate_responses=True,
        pass_context_arg_name='request'
    )
    return app.app


if __name__ == "__main__":
    app = connexion.AioHttpApp(__name__, specification_dir='specs/', port=8000)
    app.add_api(
        'service.yaml',
        resolver=RestyResolver('api'),
        strict_validation=True,
        validate_responses=True,
        pass_context_arg_name='request'
    )

    app.run(port=8000, debug=True)
