# Installation

## Local development

run `docker-compose up` to start this server.

It uses port 8000

The OpenApi 3.0 spec is located in service/specs/service.yaml

Connexion uses this to perform validation on both the input and responses. It also sets up routing automatically

Routing is implicit in this example. Reference:

- [https://github.com/zalando/connexion]
- [https://swagger.io/docs/specification/about/]

A swagger UI is also provided at [localhost:8000/v1.0/ui/]

### Sample Requests

- `curl localhost:8000/v1.0/echo/1234?echo_string=test` for a single get example
- `curl localhost:8000/v1.0/echo?echo_string=test` For a list example
- `curl -X POST localhost:8000/v1.0/echo?echo_string=123` For an error example
