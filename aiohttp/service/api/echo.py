from aiohttp import web


async def search(echo_string, request):
    reponse = {
        'echo': echo_string
    }
    return web.json_response({
        'data': {
            'echo': [reponse, reponse, reponse, reponse, reponse]
        }
    })


async def get(echo_id, echo_string, request):
    return web.json_response({
        'data': {
            'echo': echo_id + " " + echo_string
        }
    })


async def get_echo_test(echo_id, echo_string, request):
    return web.json_response({
        'data': {
            'echo': echo_id + " " + echo_string
        }
    })


async def post(echo_string, request):
    raise web.HTTPInternalServerError(
        text="test error unable to post: {}".format(echo_string)
    )
