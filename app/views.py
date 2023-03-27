from crud import create_item, delete_item, get_item, patch_item
from errors import ApiError
from flask import jsonify, request
from flask.views import MethodView
from models import Ad, get_session_maker
from schema import PatchAd, CreateAd, validate

Session = get_session_maker()


class AdView(MethodView):
    def post(self):
        ad_data = validate(CreateAd, request.json)
        with Session() as session:
            ad = create_item(session, Ad, **ad_data)
            return jsonify(
                {
                    "id": ad.id,
                    "description": ad.description,
                    "owner": ad.owner,
                    "creation_time": ad.creation_time.isoformat()
                }
            )

    def get(self, ad_id):
        with Session() as session:
            ad = get_item(session, Ad, ad_id)
            return jsonify(
                {
                    "id": ad.id,
                    "description": ad.description,
                    "owner": ad.owner,
                    "creation_time": ad.creation_time.isoformat()
                }
            )

    def patch(self, ad_id: int):
        with Session() as session:
            patch_data = validate(PatchAd, request.json)
            ad = get_item(session, Ad, ad_id)
            ad = patch_item(session, ad, **patch_data)
            return jsonify(
                {
                    "id": ad.id,
                    "description": ad.description,
                    "owner": ad.owner,
                    "creation_time": ad.creation_time.isoformat(),
                }
            )

    def delete(self, ad_id: int):
        with Session() as session:
            ad = get_item(session, Ad, ad_id)
            delete_item(session, ad)
            return {"deleted": True}