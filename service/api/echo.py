import connexion
from marshmallow.fields import String
from marshmallow import Schema

from aiohttp import web


class GetPeopleSchema(Schema):
    """ Validation class for GET change """
    echo_string = String()


class HttpError(Exception):
    code=500


async def search(echo_string, request):
    reponse = {
        'echo': echo_string
    }
    return web.json_response({
        'data': [reponse, reponse, reponse, reponse, reponse]
    })


async def get(echo_id, echo_string, request):
    return web.json_response({
        'data': {
            'echo': echo_id + " " + echo_string
        }
    })


async def post(echo_string, request):
    raise web.HTTPInternalServerError(
        text="test error unable to post: {}".format(echo_string)
    )
