class Author(object):
    author_id: int
    first_name: str
    last_name: str

    """The author class"""

    def __init__(
            self,
            author_id: int,
            first_name: str,
            last_name: str
    ):
        """author`s parameters"""
        self.author_id = author_id
        self.first_name = first_name
        self.last_name = last_name
