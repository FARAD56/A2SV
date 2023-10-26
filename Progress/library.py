class Library:
    books = []
    borrowing_records = []
    members = []
    due_library = {}

    def add_book(self,book):
        self.books.append(book)

    def lend_book(self,book,due_date):
        if book in self.books:
            idx = self.books.index(book)
            offer = self.books[idx]
            self.books.pop(idx)
            self.due_library[book] = due_date
            return offer
        else:
            print(f"There is no such book as {book}")
    

my_library = Library()
my_library.add_book("Akiola")
print(my_library.books)

my_library.lend_book("Akiola", '23/11/2023')
print(my_library.due_library)

my_library.lend_book("elective", '23/11/2023')
