from imdb import IMDb

def get_movie_cast():
    movie_name = input("Please enter the name of the movie: ")
    ia = IMDb()
    movies = ia.search_movie(movie_name)

    if movies:
        movie = movies[0]
        ia.update(movie)

        cast = movie.get('cast', [])
        if cast:
            print(f"The main cast of the '{movie}' is: ")
            for actor in cast[:10]:
                print(f" - {actor['name']}")
        else:
            print(f"No cast information found for {movie_name}")
    else:
        print(f"Movie {movie_name} not found.")


