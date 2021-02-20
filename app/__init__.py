from flask import Flask


# Create Flask's `app` object

def create_app():
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates")
    app.config['DEBUG'] = True

    with app.app_context():
        from . import routes

    return app
