from api import bp_api
from sanic import Sanic
from sanic_openapi import swagger_blueprint


app = Sanic(__name__)
app.blueprint(swagger_blueprint)

app.config.API_VERSION = '0.1'
app.config.API_TITLE = 'Sanic OpenAPI-Spec Demo'
app.config.API_TERMS_OF_SERVICE = 'Use with caution!'
app.config.API_CONTACT_EMAIL = 'zach.werheim@axial.net'

if __name__ == "__main__":
    app.blueprint(bp_api)
    app.run(host='0.0.0.0', port=8000, debug=True)
