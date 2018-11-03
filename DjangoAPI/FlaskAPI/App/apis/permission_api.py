
from flask_restful import Resource

from App.apis.decrator import permission_required


class PermissionsResource(Resource):
    @permission_required("WRITE")
    def post(self):

        return {"msg": "ok"}

