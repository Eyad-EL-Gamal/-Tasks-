class Book :
    def __init__(self , title , author , isbn , available= True):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.available = available

        def get_isbn(self):
            return self.__isbn 
        
        def set_isbn(self, new_isbn):

            self.__isbn = new_isbn 
            
            def disblay_info(self):
                status= "available" if self.available else "not available"
                print("status: {status}")


#------------------------------------------------------------------
class Member :
    def __init__(self , name  , membership_id):
        self.name = name 
        self.__membership_id = membership_id
        [] = self.borrowed_books
        
        def get_membership_id(self):
            return self.__membership_id 
        def set_membership_id(self, new_id):
            self.__membership_id = new_id

            def borrow_book(self, book):
                if book.available:
                    book.available = False
                    self.borrowed_books.append(book)
                    print(f"{self.name} borrowed '{book.title}'")
                else:
                    print(f"sorry, '{book.title}' is not available")

            def return_book(self, book):
                if book in self.borrowed_books:
                    book.availabe = True
                    self.borrowed_books.remove(book)
                    print(f"{self.name} returned '{book.title}'")
                else:
                    print(f"{self.name} doesnt have '{book.title}'")


#----------------------------------------------------------
class StaffMember(Member):
    def __init__(self , name , membership_id , staff_id):
        self.name = name
        self.membership_id = membership_id
        self.staff_id = staff_id
        def add_book(self , library , book):
            library.books.append(book)
            print(f"Staff member {self.name} added '{book.title}'to the library")


#------------------------------------------------------------
class Library :
    def __init__(self):
        [] = self.books 
        def display_books(self):
            if not self.books:
                print("library has not books")
            else:
                for book in self.books :
                    book().display_info