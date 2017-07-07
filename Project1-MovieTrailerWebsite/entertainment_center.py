import fresh_tomatoes
import media

# adding movie Toy Story
toy_story = media.Movie("Toy Story",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# adding movie Avatar
avatar = media.Movie("Avatar",
                     "https://www.movieposter.com/posters/archive/main/101/MPW-50968",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# adding movie School of Rock
school_of_rock = media.Movie("School of Rock",
                             "https://images-na.ssl-images-amazon.com/images/I/81m0ywBJ67L._SY445_.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# adding movie Ratatouille
ratatouille = media.Movie("Ratatouille",
                          "http://fontmeme.com/images/Ratatouille-film-poster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# adding movie Midnight in Paris
midnight_in_paris = media.Movie("Midnight in Paris",
                                "https://ih0.redbubble.net/image.12813797.9187/flat,1000x1000,075,f.u2.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

# adding movie Hunger Games
hunger_games = media.Movie("Hunger Games",
                           "http://www.impawards.com/2012/posters/hunger_games_ver26_xlg.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# adding the movies into a list of objects Movie
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# open the website including the movies in the list above by method open_movies_page provided in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)