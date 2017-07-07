import webbrowser

class Movie():
    # class Movie, that provides a template for all the movies objects
    # nouns: title, storyline, poster_image, youtube_trailer
    # verbs, show_trailer()

    def __init__(self, title, poster_image, trailer_youtube):
        # constructor for class Movie
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # function show_trailer, to open the youtube trailer url in the browser when the function is called
        webbrowser.open(self.trailer_youtube_url)