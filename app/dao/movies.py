from app.dao.model.movies import Movie


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_movie(self, mid):
        query = self.session.query(Movie)
        return query.get(mid)

    def get_movies(self, **kwargs):
        query = self.session.query(Movie)

        for key, value in kwargs.items():
            query = query.filter(getattr(Movie, key) == int(value))
        return query.all()

    def create(self, data):
        new_movie = Movie(**data)
        with self.session.begin():
            self.session.add(new_movie)
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_movie(mid)
        if not movie:
            return
        self.session.delete(movie)
        self.session.commit()
