"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1. Encapsulation - data and it's functionality lives close to each other
   2. Abstraction - we can hide details we don't need
   3. polymorphism - components are interchangeable

2. What is a class?
  it's a blueprint for an object


3. What is a method?

It's a function, which lives inside of its class. Method is associated with the class. 
method takes an instance of the class as a first parameter 

4. What is an instance in object orientation?

it's an individual object that has all the attributes described in the class definition

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Instance attributes are owned by a specific instance of a class.
   Class attributes are owned by the class itself and shared by all the instances of the class. 

   Example:
   class Melon:
      species = Christams
      qty = 5

>>> m1 = Melon
m1 instance has two attributes (species and qty)
>>> m2 = Melon
>>> m2.sales_tax = 5
m2 has three attributes - species, qty and its own - sales_tax


"""


# Part 2: Road Class
# #############################################################################

# Create your Road class here
class Road:
    num_lanes = 2
    speed_limit = 25

# Instantiate Road objects here
road_1 = Road()
road_2 = Road()

road_1.num_lanes = 4
road_1.speed_limit = 40

# Part 3: Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # # write the update_password method here
    def update_password(self, current_pswd, new_pswd):
        if current_pswd == self.password:
            self.password = new_pswd            
        else: 
            print('Invalid password')


# # Part 4: Build a Library
# # #############################################################################
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# # Create your Library class here
class Library:
    books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def find_books_by_author(self, author):
        books_lst = []
        for book in self.books:
            if book.author == author:
                books_lst.append(book)

        return books_lst

# # Part 5: Rectangles
# # #############################################################################

class Rectangle(object):
    """A rectangle object."""

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the rectangle's area (length * width)."""
        return self.length * self.width

# Create the Square class here
class Square(Rectangle):

    def __init__(self, side_length):
        super(Square,self).__init__(side_length, side_length)
        self.length = self.width = float(side_length)

    def calculate_area(self):
        
        if self.length == self.width:
            return super(Square, self).calculate_area()
        else: 
            print('Invalid Square')




