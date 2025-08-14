import datetime as dt
from collections import Counter
from tkinter import simpledialog
import tkinter as tk

class Book:
    books = [] # Class variable for all books acts as database
    dict_of_reviews = {}  # Class variable for reviews

    def __init__(self, id, name, field, num_pages, writer, publisher, publish_year, is_borrowed=False, borrow_price=0.0, rate=0):
        self.id = id
        self.name = name
        self.field = field
        self.num_pages = num_pages
        self.writer = writer
        self.publisher = publisher
        self.publish_year = publish_year
        self.is_borrowed = is_borrowed
        self.borrow_price = borrow_price
        self.rate = rate

    '''def updater(self, request):
        request = request.lower().strip()
        if request == "id":
            self.id = int(input("Enter new id: "))
        elif request == "name":
            self.name = input("Enter new name: ")
        elif request == "field":
            self.field = input("Enter new field: ")
        elif request == "num_pages":
            self.num_pages = int(input("Enter new number of pages: "))
        elif request == "writer":
            self.writer = input("Enter new writer: ")
        elif request == "publisher":
            self.publisher = input("Enter new publisher: ")
        elif request == "publish_year":
            self.publish_year = int(input("Enter new publish year: "))
        elif request == "is_borrowed":
            self.is_borrowed = input("Is the book borrowed? (yes/no): ").lower() == "yes"
        elif request == "borrow_price":
            self.borrow_price = float(input("Enter new borrow price: "))
        elif request == "rate":
            self.rate = float(input("Enter new rate: "))'''
    @classmethod
    def find_book_by_id(cls, target_id):
            for book in cls.books:
              if book.id == target_id:  # Compare object's id with target
                 return book  # Return the matching object
            return None  # If not found
    @classmethod
    def updater(cls,book_id,field, new_value):
        book = cls.find_book_by_id(book_id)
        if not book:
            return False, "Book not found."
        # Update based on requested field
        if hasattr(book, field):
            setattr(book, field, new_value)
            return True, f"{field} updated successfully."
        else:
            return False, f"Field '{field}' does not exist."
        



    def show(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Field: {self.field}")
        print(f"Number of Pages: {self.num_pages}")
        print(f"Writer: {self.writer}")
        print(f"Publisher: {self.publisher}")
        print(f"Publish Year: {self.publish_year}")
        print(f"Is Borrowed: {'Yes' if self.is_borrowed else 'No'}")
        print(f"Borrow Price: {self.borrow_price}")
        print(f"Rate: {self.rate}")

    def book_age(self):
        current_year = dt.datetime.now().year
        return current_year - self.publish_year
    
    @classmethod
    def book_exists(cls,book_id):
     for book in cls.books:
        if book.id == book_id:  # check each object's id
            return True
        
     return False

    @classmethod
    def add_review(cls,self, id, review):
       if self.book_exists(id):
         cls.dict_of_reviews[id].append(review)
       else:
         cls.dict_of_reviews[id] = [review] 

    @classmethod
    def show_reviews(cls):
        if not cls.dict_of_reviews:
            print("No reviews available.")
        else:
            for id, reviews in cls.dict_of_reviews.items():
                print(f"ID: {review.keys}")
                for review in reviews:
                    print(f"Review: {review}")
                

    @classmethod
    def show_overall(cls, id):
        book_reviews = [r.values for r in cls.dict_of_reviews if r.key == id]
        if not book_reviews:
            print(f"No reviews found for Book ID {id}.")
            return
        counter = Counter(book_reviews)
        most_common = counter.most_common(1)[0][0]
        print(f"Book ID {id} Overall Review: {most_common}")
