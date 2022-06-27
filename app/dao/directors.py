from app.dao.model.directors import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_director(self, did):
        query = self.session.query(Director)
        return query.get(did)

    def get_directors(self):
        query = self.session.query(Director)
        return query.all()
