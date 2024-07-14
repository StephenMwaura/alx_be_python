class Book:
    def __init__(self, title, author):
         self.title = title
         self.author = author
         self._is_checked_out = False
    def get_title(self):
         return self.title
    def get_author(self):
         return self.author
    def is_checked_out(self):
         return self.is_checked_out
    def check_out(self):
         self.is_checked_out = True
    def return_book(self):
         self.is_checked_out = False
         
class Library:
     def __init__(self):
          self._books= []
          
     
     def add_book(self , book):
          self._books.append(book)
     def check_out_book(self ,title):
          for book in self._books:
               if book.get_title() == title:
                    if not book.is_checked_out():
                         book.check_out()
                         return f"Book {title} checked out."
                    else:
                      return f"Book {title} is already checked out."
          return f"{title} not found."         
                    
                    
     def return_book(self,title):
          for book in self._books:
               if book.get_title() ==title:
                if book.is_checked_out():
                    book.return_book()
                    return f"Book {title} has been returned."
                else:
                     return f"Book {title} was not checked out."
          return f"Book {title} not found."
               
     def list_available_books(self):
          available_books = []
          for book in self._books:
               if not book.is_checked_out():
                    available_books.append(book.get_title())
                    if available_books:
                         return available_books
                    
          
          
