from app.dao.directors import DirectorDAO
from app.dao.genres import GenreDAO
from app.dao.movies import MoviesDAO
from app.service.directors import DirectorService
from app.service.genres import GenreService
from app.service.movies import MoviesService
from app.setup_db import db

movie_dao = MoviesDAO(db.session)
movie_service = MoviesService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
