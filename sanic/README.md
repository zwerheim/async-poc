# Installation

## Local development

run `docker-compose up` to start this server.

It uses port 8000

This example uses a basic blueprint and a class based view to handle routing.

The swagger-spec is informed via decorators with the `sanic-openapi` package. This is in swagger-spec 2.0

- [https://sanic.readthedocs.io/en/latest/sanic/getting_started.html] For all the relevant documentation
- [https://github.com/huge-success/sanic-openapi]
- [https://swagger.io/docs/specification/about/]

A swagger UI is also provided at [http://localhost.com:8000/swagger/]

### Sample Requests

- `curl -X GET localhost:8000/v1/api/echo`
- `curl -X POST localhost:8000/v1/api/echo`
- `curl -X PUT localhost:8000/v1/api/echo`
- `curl -X DELETE localhost:8000/v1/api/echo`
