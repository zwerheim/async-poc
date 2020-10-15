
from sanic.views import HTTPMethodView
from sanic.response import text
from sanic_openapi import doc


class EchoAsyncView(HTTPMethodView):

    @doc.summary("Async GET method demo")
    async def get(self, request):
        return text('I am async get method')

    @doc.summary("Async POST method demo")
    @doc.consumes({"view": {"name": str}}, location="body")
    async def post(self, request):
        return text('I am async post method')

    @doc.summary("Async PUT method demo")
    async def put(self, request):
        return text('I am async put method')

    @doc.summary("Async DELETE method demo")
    async def delete(self, request):
        return text('I am delete method2')
