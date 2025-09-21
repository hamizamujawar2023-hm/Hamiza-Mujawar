import queue
from datetime import datetime # for automatic date/time

# Initial book list
books = [{"title": "Atomic Habits", "author": "Author : James ", "status": "Available"},
         {"title": "Miracle Morning", "author": "Author:Elrod", "status": "Available"},
         {"title": "Unshakeable", "author": "Author : Tony Robin", "status": "Available"},
         {"title": "Power of Now", "author": "Author : Eckhart Tolle", "status": "Available"},
         {"title": "Mindset", "author": "Author : Carol", "status": "Available"},
         {"title": "The 7 Habbits", "author": "Author :Stephen", "status": "Available"}]
book_queue = queue.Queue()
borrowed_books = {}
date_time = []

# Add a new book
def enqueue(title, author):
    new_book = {"title": title, "author": author, "status": "Available"}
    books.append(new_book) # Add to books list
    book_queue.put(new_book)
    print(f"Book added: {title} by {author}")

# Remove a book
def remove_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print(f"Book removed: {title}")
            return
    print("Book not found.")
# Issue a book
def issue_book(title, borrower):
    for book in books:
        if book["title"].lower() == title.lower() and book["status"] == "Available":
            book["status"] = "Issued"
            date = input("Enter the date (dd/mm/yy): ")
            time = input("Enter the time (HH:MM): ")
            date_time.append({
                "title": title,
                "borrower": borrower,
                "date": date,
                "time": time })
            borrowed_books[title] = borrower
            print(f"Book '{title}' issued to {borrower} on {date} at {time}.")
            return
    print(f"Book '{title}' not available.")
# Return a book
def return_book(title):
    for book in books:
        if book["title"].lower() == title.lower() and book["status"] == "Issued":
            book["status"] = "Available"
            borrowed_books.pop(title, None)
            print(f"Book '{title}' returned successfully.")
            return
    print(f"Book '{title}' not found or not issued.")

# Sort books alphabetically
def sort_books():
    books.sort(key=lambda x: x["title"].lower())
    print("Books sorted by title.")

# Search for a book
def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            print(f"Book found: {book['title']} by {book['author']} - {book['status']}")
            return
    print("Book not found.")

# Display all books
def display_books():
    print("\nBooks:")
    for i, book in enumerate(sorted(books, key=lambda x: x["title"].lower()), start=1):
        print(f"{i}. {book['title']} by {book['author']} - {book['status']}")
# Main menu loop
while True:
    print("\n=============== Library Management ===============")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Sort Books")
    print("6. Search Book")
    print("7. Display Books")
    print("8. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        enqueue(title, author)
    elif choice == "2":
        title = input("Enter book title to remove: ")
        remove_book(title)
    elif choice == "3":
        title = input("Enter book title to issue: ")
        borrower = input("Enter borrower name: ")
        issue_book(title, borrower)
    elif choice == "4":
        title = input("Enter book title to return: ")
        return_book(title)
    elif choice == "5":
        sort_books()
    elif choice == "6":
        title = input("Enter book title to search: ")
        search_book(title)
    elif choice == "7":
        display_books()
    elif choice == "8":
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid option. Please choose again.")
