from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

# Custom modules: cfg y globals
import config as cfg

# Import views (endpoints)
import services


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": cfg.ORIGINS}})
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type, Authorization'
app.config['CORS_EXPOSE_HEADERS'] = 'Content-Type, Authorization'

# Register docs on API
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Wealthabout App"})
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# Register blueprints for different components
app.register_blueprint(services.indexes_view)


if __name__ == '__main__':
    app.run(host=cfg.HOST,port=cfg.PORT,debug=False)
