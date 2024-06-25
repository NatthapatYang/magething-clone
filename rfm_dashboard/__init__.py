from flask import Flask , render_template

def create_app():
    app = Flask(__name__)

    from .controller import landing_page
    app.register_blueprint(landing_page.bp)

    return app