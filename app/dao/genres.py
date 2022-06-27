from app.dao.model.genres import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_genre(self, did):
        query = self.session.query(Genre)
        return query.get(did)

    def get_genres(self):
        query = self.session.query(Genre)
        return query.all()

