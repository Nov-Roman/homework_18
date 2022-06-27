from app.dao.movies import MoviesDAO


class MoviesService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_one_movie(self, mid):
        return self.dao.get_movie(mid)

    def get_some_movies(self, **kwargs):
        return self.dao.get_movies(**kwargs)

    def create_movies(self, data):
        return self.dao.create(data)

    def full_update(self, movie_id, data):
        movie = self.get_one_movie(movie_id)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie

    def partial_update(self, movie_id, data):
        movie = self.get_one_movie(movie_id)

        if 'title' in data:
            movie.title = data["title"]
        elif 'description' in data:
            movie.description = data['description']
        elif 'trailer' in data:
            movie.trailer = data['trailer']
        elif 'year' in data:
            movie.year = data['year']
        elif 'rating' in data:
            movie.rating = data['rating']
        elif 'genre_id' in data:
            movie.genre_id = data['genre_id']
        elif 'director_id' in data:
            movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie

    def delete(self, movie_id):
        self.dao.delete(movie_id)
