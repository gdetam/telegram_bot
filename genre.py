class Genre(object):
    genre_id: int
    name: str

    """The genre class"""

    def __init__(
            self,
            genre_id: int,
            name: str
    ):
        """author`s parameters"""
        self.genre_id = genre_id
        self.name = name
