from flask import Blueprint
from flask import current_app as app


# Blueprint Configuration
posts_bp = Blueprint(
    'posts_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@posts_bp.route('/', methods=['GET'])
def posts():
    """postspage."""
    #products = fetch_products(app)
    return "tweets loading..."
    # return render_template(
    #     'index.jinja2',
    #     title='Flask Blueprint Demo',
    #     subtitle='Demonstration of Flask blueprints in action.',
    #     template='posts-template',
    #     products=products
    # )