import backend
import tkinter as tk
from tkinter import simpledialog, messagebox
from backend import Book
from PIL import Image, ImageTk  # pip install pillow


root = tk.Tk()
root.title("📚 Book Management System")
root.geometry("800x600")

# Background image
bg_image = Image.open(r"D:\\College FCDS\\Samsung_projects\\Library_T1\\library_bg.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Title
title_label = tk.Label(root, text="📚 Book Management System 📚", font=("Arial", 20, "bold"), bg="#d4a373", fg="white")
title_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#d4a373")
btn_frame.pack(pady=10)



def gui_add_book():
    id = simpledialog.askinteger("Add Book", "Enter book ID:")
    name = simpledialog.askstring("Add Book", "Enter book name:")
    field = simpledialog.askstring("Add Book", "Enter field:")
    num_pages = simpledialog.askinteger("Add Book", "Enter number of pages:")
    writer = simpledialog.askstring("Add Book", "Enter writer:")
    publisher = simpledialog.askstring("Add Book", "Enter publisher:")
    publish_year = simpledialog.askinteger("Add Book", "Enter publish year:")
    is_borrowed = simpledialog.askstring("Add Book", "Is borrowed? (yes/no):").lower() == "yes"
    borrow_price = simpledialog.askfloat("Add Book", "Enter borrow price:")
    rate = simpledialog.askfloat("Add Book", "Enter rate:")

    new_book = Book(id, name, field, num_pages, writer, publisher, publish_year, is_borrowed, borrow_price, rate)
    Book.books.append(new_book)
    messagebox.showinfo("Success", f"Book '{name}' added successfully!")
    #output_area.insert(tk.END, f"Book '{name}' added successfully!\n")

def gui_show_books():
    if not Book.books:
        messagebox.showinfo("Info", "No books in the system.")
    else:
        output = "\n".join([f"ID: {b.id}, Name: {b.name}, Field: {b.field}, num_pages: {b.num_pages}, writer:{b.writer}, publisher: {b.publisher}, publish_year:{b.publish_year}, is_borrowed: {b.is_borrowed}, borrow_price: {b.borrow_price}, rate: {b.rate} " for b in Book.books])
        messagebox.showinfo("Books", output)

def gui_update_book():
    id_to_update = simpledialog.askinteger("Update Book", "Enter book ID to update:")
    if id_to_update is not None:
        # Find the book object with the given ID
        book = Book.find_book_by_id(id_to_update)
        if book != None:
                field_to_update = simpledialog.askstring(
                    "Update Book",
                    "What do you want to update? (id, name, field, num_pages, writer, publisher, publish_year, is_borrowed, borrow_price, rate)"
                )
                if field_to_update:
                    new_value = simpledialog.askstring("Update Book", f"Enter new value for {field_to_update}:")
                    Book.updater(id_to_update,field_to_update,new_value)  # Call on the instance, not the class

                    messagebox.showinfo("Success", f"{field_to_update} updated successfully!")
                    #output_area.insert(tk.END, f"{field_to_update} updated successfully!\n")
                return  # Exit after updating the book
        # If loop completes without finding the book
        messagebox.showerror("Error", "Book not found.")


def gui_add_review():
    id = simpledialog.askinteger("Add Review", "Enter book ID:")
    if id is not None:
            review = simpledialog.askstring("Add Review", "Enter your review:")
            if review:
                Book.add_review(id, review)
                messagebox.showinfo("Success", "Review added successfully!")
                #output_area.insert(tk.END, "Review added successfully!\n")
            else:
             messagebox.showerror("Warning", "review not entered.")
def gui_show_reviews():
    Book.show_reviews()
def gui_show_overall_review():
    Book.show_overall(id)

buttons = [
    ("Add Book", gui_add_book),
    ("Show Books", gui_show_books),
    ("Update Book", gui_update_book),
    ("Add Review", gui_add_review),
    ("Show Reviews", gui_show_reviews),
    ("Show Overall Review", gui_show_overall_review)
]



for text, cmd in buttons:
    tk.Button(btn_frame, text=text, command=cmd, font=("Arial", 12), width=20, bg="#f4a261", fg="white").pack(pady=5)


root.mainloop()