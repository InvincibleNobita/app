#from utils import create_app
from flask import Flask

from posts.routes import posts_bp
from weather.routes import weather_bp

app = Flask(__name__)
# Register Blueprints
app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(weather_bp,url_prefix='/weather')

if __name__ == '__main__':
    app.run(debug=True)