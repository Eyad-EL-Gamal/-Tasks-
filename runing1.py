from library_system import Book , Member , StaffMember , Library 
if__name__="__main__"
library = Library
staff = StaffMember("Mohamed" , "E117" , "5335")
book1 = Book("Evening talk" , "Taha Housen" , "14598")
book2 = Book("Building destinies" , "Najep Mahfoth" , "15896")
staff.add_book(library, book1)
staff.add_book(library, book2)
print("Books n Library")
library.display_books
member = Member("Ali" , "s684")
member.borrow_book(book1)
print("Books in Library after borrowing:")
library.display_books
member.return_book(book1)
print("Books in Library after returning")
library.display_books