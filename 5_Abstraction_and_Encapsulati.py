
class Library:
    customers = {}
    borrowedBooksList = {}
    
    def __init__ (self, listOfBooks):
        self.availableBooks = listOfBooks
        
    def addCustomer (self, name, age):
        for key in self.customers:
            if key == name:
                print("Customer already exists!")
        self.customers[name] = Customer(name, age)
        
    def displayCustomers(self):
        print(self.customers)
        for k, v in self.customers.items():
            print(k,v.age, v.name, v.borowedBook)
            
        
    def displayAvailableBooks(self):
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
            
    def displayBorrowedBooks(self):
        print("Borrowed Books: ")
        for k,v in self.borrowedBooksList.items():
            print(k,v)
            
    def lendBook(self, requestedBook, customer):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
            self.borrowedBooksList[customer] = requestedBook
            
        elif requestedBook not in self.availableBooks:
            print("Sorry, the book is not available")
            
    def addBook(self, returnedBook, cust):
        print(self.borrowedBooksList[cust])
        if self.borrowedBooksList[cust] == returnedBook:
            del(self.borrowedBooksList[cust])
            self.availableBooks.append(returnedBook)
        
        print("You have returned the book. Thank you!")
   
    
    
class Customer:
    borowedBook = ['None']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def requestBook(self):
        print("Enter the name of the book you would like to borrow:")
        self.book= input()
        return self.book
    
    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book

#Create objects         
library = Library(['Dywizjon 303', 'Piramidy', 'Historia'])
library.addCustomer('Piotr', 34)

#jak zobaczyc customer age

#=====================Menu===========================================
while True:
    print("===========  Menu =========")
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    print("Enter 5 to add customer")
    print("Enter 6 to display avaible customers")
    print("Enter 7 to display borrowed books")
    
    userChoice = int(input())
    
    
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        name = str(input('Customer name: '))
        requestedBook = library.customers[name].requestBook()
        customer = library.customers[name].name
        library.customers[name].borowedBook.append(requestedBook) 
        library.lendBook(requestedBook, customer)
    elif userChoice is 3:
        
        cust = str(input("Customer name: "))
        returnedBook = library.customers[cust].returnBook()
        print(returnedBook)
        library.addBook(returnedBook, cust)
        
        
    elif userChoice is 4:
	    break
    elif userChoice is 5:
        print("Add new customer")
        name = input("customer name: ")
        age =  input("cdd age: ")
        library.addCustomer(name, age)
    elif userChoice is 6:
        print("List avaible customers")
        library.displayCustomers()
    elif userChoice is 7:
        library.displayBorrowedBooks()
		
