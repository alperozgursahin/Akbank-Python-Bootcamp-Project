class Library :
    
    def __init__(self):
        self.file = open("books.txt","a+")

    def __del__(self):
        self.file.close()

    def ListBooks(self):
        f = open("books.txt","r")
        lines = f.read().splitlines()
        for line in lines:
            splitted_line = line.split(", ")
            book_name = splitted_line[0]
            author = splitted_line[1]
            released_year = splitted_line[2]
            number_of_pages = splitted_line[3]
            print(f"Book Name: {book_name}, Author: {author}, Released Year: {released_year}, Number of Pages: {number_of_pages}")

    def AddBook(self):
        pass

    def RemoveBook(self):
        pass
   

    

lib = Library()
lib.ListBooks()
