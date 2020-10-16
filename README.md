# Sanic vs AIOHTTP

## Sanic

### Pros

- Simple and easy to setup
- Well supported in the community with a wide variety of third party packages
- Good performance
- Supports multiple workers natively
- Has redis extension

### Cons

- Doesn't support openapi-spec 3.0
- Uses GINO a Asyncio compatible driver built on sqlalchemy core - Not pure sqlalchemy

## Aiohttp

### Pros

- Widly supported in the community with a wide variety of third party packages
- Supports sqlalchemy out of the box
- Supported by connexion - API first routing and input/output validation - Driven by yaml spec
- Uses AIOPG an Asyncio compatible postgres driver. Extends sqlalchemy
- Has redis extension

### Cons

- Slower performance than Sanic
- Does not natively support multiple workers (Use gunicorn to run multiple)

## Conclusions

Performance and support are comparible between both frameworks. Both also have great community support. The one major difference is our desrire to support the API-First style for these servers. The `connexion` package enables this and only supports AioHttp at this time. This along with closer sqlalchemy support means we will likely go with AioHttp as our main server framework moving forward.

