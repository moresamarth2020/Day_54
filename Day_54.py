#!/usr/bin/env python
# coding: utf-8

# # Exercise-6-Solution
# - Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

# In[23]:


class library:
    def __init__ (self):
        self.nobooks = 0
        self.books = []
        
    def addbook (self, book):
        self.books.append(book)
        self.nobooks = len(self.books)
        
    def showInfo(self):
        print(f"The Library Has {self.nobooks} books. The Books Are")
        for book in self.books:
            print(book)
        
l1 = library()
l1.addbook("Story of the War")

l2 = library()
l2.addbook("Story Of the Gang")
l2.showInfo()

l3 = library()
l3.addbook("Gang of vasipur")

l4 = library()
l4.addbook("Story of Samarth")

library.showInfo(l1)
library.showInfo(l2)
library.showInfo(l3)
library.showInfo(l4)


# In[ ]:




