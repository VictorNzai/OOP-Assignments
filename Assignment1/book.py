# Base Class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def describe(self):
        print(f"'{self.title}' by {self.author} - {self.pages} pages, Genre: {self.genre}")

    def read(self):
        print(f"You start reading '{self.title}'... 📖")

# Subclass (Inheritance)
class ComicBook(Book):
    def __init__(self, title, author, pages, genre, illustrator):
        super().__init__(title, author, pages, genre)
        self.illustrator = illustrator

    # Overriding method
    def describe(self):
        print(f"Comic: '{self.title}' by {self.author}, illustrated by {self.illustrator}. Pages: {self.pages}")

    def read(self):
        print(f"Flipping through colorful pages of '{self.title}'... 🎨")

# Usage
normal_book = Book("1984", "George Orwell", 328, "Dystopian")
comic_book = ComicBook("Spider-Man", "Stan Lee", 150, "Superhero", "Steve Ditko")

normal_book.describe()
normal_book.read()

print()

comic_book.describe()
comic_book.read()
