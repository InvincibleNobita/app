#from utils import create_app
from flask import Flask

from posts.routes import posts_bp
from weather.routes import weather_bp

app = Flask(__name__)
with app.app_context():
       
        # Register Blueprints
        app.register_blueprint(posts_bp)
        app.register_blueprint(weather_bp)

if __name__ == '__main__':
    app.run(debug=True)