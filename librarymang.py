class library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        print(" List of books present are :")
        for book in self.books:
            print(" *",book )
    def borrowbook(self, bookname):
        print(self.books)
        if bookname in (self.books):
            print(f" You have been issued this {bookname}. please keep it safe")
            self.books.remove(bookname)
            return True
        else:
            print(" sorry this book is not availble yet ")
            return  False
    def returnbook(self,bookname ):
        self.books.append(bookname)
        print("Thanks for returning the book")

class student:
    def requestbook(self):
        self.book = input(" Enter the book you want to borrow a book: ")
        return self.book
    def returntbook(self):
        self.book = input(" Enter the book you want to return a book : ")
        return self.book



if __name__ =="__main__":
    centralibrary = library(["c++","python","django","dbms"," algorithm"])
    student = student()
    centralibrary.displayavailablebooks()


    while(True):
        welcomemsg = '''==== welcome to centralibrary========
        please choose a option
        1 List all the books
        2 request a book
        3 return a book
        4 exit
        '''
        print(welcomemsg)
        a = int(input(" Enter a choice : "))
        if a == 1:
            centralibrary.displayavailablebooks()
        elif a == 2:
            centralibrary.borrowbook(student.requestbook())
        elif a == 3:
            centralibrary.returnbook(student.returntbook())
        elif a == 4:
            print(" ********** Thanks for using central library , Have a great day ahead  *******  ")
            exit()
        else:
            print(" Invalid choice!!!! ")