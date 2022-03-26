
from flask import Blueprint
from flask import current_app as app

from weather.controller import get_weather

#from dotenv import load_dotenv
#load_dotenv()



# Blueprint Configuration
weather_bp = Blueprint(
    'weather_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@weather_bp.route('/', methods=['GET'])
def weather(lat,lon):
    """weatherpage."""
    data = get_weather(lat,lon)
    #products = fetch_products(app)
    return data
    # return render_template(
    #     'index.jinja2',
    #     title='Flask Blueprint Demo',
    #     subtitle='Demonstration of Flask blueprints in action.',
    #     template='weather-template',
    #     products=products
    # )