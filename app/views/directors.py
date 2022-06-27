from flask_restx import Resource, Namespace
from app.dao.model.directors import DirectorSchema
from app.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route("/")
class DirectorsView(Resource):
    schema = DirectorSchema(many=True)

    def get(self):
        return self.schema.dump(director_service.get_some_directors()), 200


@director_ns.route("/<int:director_id>")
class DirectorView(Resource):
    schema = DirectorSchema()

    def get(self, director_id: int):
        return self.schema.dump(director_service.get_one_director(director_id)), 200

