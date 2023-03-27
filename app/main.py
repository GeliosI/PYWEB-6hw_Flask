import atexit

from errors import ApiError, error_handler
from models import close_db, init_db
from views import AdView

from app import get_app

init_db()
atexit.register(close_db)

app = get_app()

app.add_url_rule(
    "/ads/<int:ad_id>/",
    view_func=AdView.as_view("ad"),
    methods=["GET", "PATCH", "DELETE"],
)

app.add_url_rule(
    "/ads/",
    view_func=AdView.as_view('ad_create'),
    methods=['POST'],
)

app.errorhandler(ApiError)(error_handler)

if __name__ == '__main__':
    app.run()