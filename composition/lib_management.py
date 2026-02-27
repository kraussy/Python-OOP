#Library Management System 

from datetime import datetime
class BorrowRecord:
    def __init__(self, book, book_date, return_date):
        self.book = book
        self.book_date = datetime.now()
        self.return_date = None
        
    def close(self):
        self.return_date = datetime.now()
        
class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = True
        
    def borrow(self):
        self.is_available = False
        
    def return_book(self):
        self.is_available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.records = []
        
    def borrow_book(self, book):
        if not book.is_available:
            print(f"sorry, {book.title} is not here!")
            return 
        book.borrow()
        record = BorrowRecord(book, datetime.now(), None)
        self.records.append(record)
        print("Sucessfully borrowed book!")
        
    def return_book(self, book):
        for record in self.records:
            if record.book == record.return_date is None:
                record.close()
                book.return_book()
                print(f"{self.name} returned {book.title}.")
                return
        print("No active borrow record found.")
        
    def history(self):
        print(f"\n📋 Borrow history for {self.name}:")
        for r in self.records:
            status = "Returned" if r.return_date else "Still borrowed"
            print(f"  - {r.book.title} | Borrowed: {r.book_date} | {status}")
    
class Branch:
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def add_member(self,member):
        self.members.append(member)

    def available_books(self):
        print("***Available Books ***")
        
        if b.is_available:
            for index, b in enumerate(self.books, 1):
                print(f"{index}. {b.title}")


class Library:
    def __init__(self, name):
        self.name = name
        self.branches = []
        
    def add_branch(self, branch):
        self.branches.append(branch)
        
    def find_book(self, title):
        for bran in self.branches:
            for book in bran.books:
                if book.title == title:
                    return book
        return None
    
    def total_members(self):
        pass
        
# ---- Test it out ----
lib = Library("City Library")

b1 = Branch("Downtown")
b2 = Branch("Uptown")
lib.add_branch(b1)
lib.add_branch(b2)

book1 = Book("1984", "George Orwell", "")
book2 = Book("Dune", "Frank Herbert", '')
b1.add_book(book1)
b1.add_book(book2)

m1 = Member("Alice", "M001")
b1.add_member(m1)

m1.borrow_book(book1)
m1.borrow_book(book1)  # should print: not available
m1.return_book(book1)
m1.history()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
