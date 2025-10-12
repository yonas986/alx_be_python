class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor that initializes book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
