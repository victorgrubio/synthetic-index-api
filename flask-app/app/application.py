from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy



def create_app(config_object='config.DevelopmentConfig'):
    app = Flask(__name__)
    # Setup CORS
    app.config.from_object(config_object)
    CORS(app, resources={r"/*": {"origins": app.config['ORIGINS']}})
    # Register Swagger
    swagger = Swagger(app)
    # Register DB
    from models import db
    db.init_app(app)

    with app.app_context():
        # Import views (endpoints)
        import components
        # Register blueprints for different components
        app.register_blueprint(components.indexes_blueprint)
        db.create_all()
        return app


app = create_app()

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'])
