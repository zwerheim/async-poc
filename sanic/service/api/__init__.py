from sanic import Blueprint

from .echo import EchoAsyncView

bp_api = Blueprint('api', url_prefix='/api', version=1)
bp_api.add_route(EchoAsyncView.as_view(), '/echo')
