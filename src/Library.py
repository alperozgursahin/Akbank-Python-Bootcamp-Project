class Library :
    
    def __init__(self):
        self.file = open("books.txt","a+")

    def __del__(self):
        self.file.close()

    def ListBooks(self):
        f = open("books.txt","r")
        lines = f.read().splitlines()
        for line in lines:
            splitted_line = line.split(",")
            book_name = splitted_line[0]
            author = splitted_line[1]
            released_year = splitted_line[2]
            number_of_pages = splitted_line[3]
            print(f"Book Name: {book_name}, Author: {author}, Released Year: {released_year}, Number of Pages: {number_of_pages}")

    def AddBook(self):
        f = open("books.txt", "a")
        book = input("Add book details(Book Name,Author,Released Year,Number of Pages):\n")
        f.write("\n" + book)


    def RemoveBook(self):
        books_list = []
        f = open("books.txt","r")
        lines = f.read().splitlines()
        book_to_remove = (input("Give the book title to remove:\n")).lower()
        founded = False
        for line in lines:
            if book_to_remove == line.split(",")[0].lower():
                founded = True
            else :
                books_list.append(line)
        f.close()
        f = open("books.txt","w")
        for book in books_list:
            f.write(book + "\n")
        
        if (founded):
            print(f"{book_to_remove.title()} succesfully removed from database!")
        else :
            print(f"There is no {book_to_remove.title()} book in database!")

def switch(value):
    try:
       value = int(value)
    except ValueError:
       print ('Give a Valid Number, Please.')
    lib = Library()
    if(value == 1):
        lib.ListBooks()
    elif (value == 2):
        lib.AddBook()
    elif (value == 3):
        lib.RemoveBook()
    else:
       print ('Valid range, please: 1-3')

while True:
    print("***MENU***\n1) List Books\n2) Add Book\n3) Remove Book")
    value = input('Choose an operation:\n')
    if (value == "q"):
        print("Goodbyee!")
        break
    switch(value)

