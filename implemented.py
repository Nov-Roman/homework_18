from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from dao.movies import MoviesDAO
from dao.setup_db import db
from service.directors import DirectorService
from service.genres import GenreService
from service.movies import MoviesService

movie_dao = MoviesDAO(db.session)
movie_service = MoviesService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
