class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:",self.title,"\n", "Author:", self.author)
my_book = Book("The Great Gatsby","F. Scott Fitzgerald")
my_book.display_info()
