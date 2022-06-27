from app.dao.genres import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one_genre(self, did=None):
        return self.dao.get_genre(did)

    def get_some_genres(self):
        return self.dao.get_genres()
