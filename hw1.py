
import math
from data import Price,Rectangle,Point,Book,Circle,Employee

# Write your functions for each part in the space below...

# Part 1
#Counts the number of vowels in from user entered string
#INPUT is a string
#output is an integer
def vowel_count(letters:str) -> int:
    count = 0
    for char in letters:

        if char.upper() == "A" or char.upper() == "E" or char.upper() == "I" or char.upper() == "O" or char.upper() == "U":
            count = count +1
    return count


# Part 2
#Counts the number of lists inside an initial list that are equal to 2 in length
#INPUT:nested list of integers
#Output:nested list of integers
def shorts_list(list1: list[list[int]]) ->list[list[int]]:
    list_of_short = []
    for list in list1:
        if len(list) == 2:
            list_of_short.append(list)
    return list_of_short

# Part 3
# take a nested list and return it with each list with 2 elements in an ascending order
#INPUT: nested list of integers
#Output: nested list of integers
def ascending_pairs(list1: list[list[int]]) -> list[list[int]]:
    list_ascending_pairs =[]
    for list in list1:
        if len(list) == 2:
            if list[0] > list[1]:
                temporary_for_swap = list[1]
                list[1] = list[0]
                list[0] = temporary_for_swap
        list_ascending_pairs.append(list) # should check if this is the right indent LOL
    return list_ascending_pairs
# Part 4
#compounds price with correct change <100
#INPUT: Price
#Output: Price
def add_prices(price1: Price, price2: Price) -> Price:

    total_price_dollars = price1.dollars + price2.dollars
    cent_dollars = (price1.cents + price2.cents)//100
    total = Price((total_price_dollars + cent_dollars), (price1.cents + price2.cents)%100)

    return total
# Part 5
#find area of a rectangle of Rectangle class
#INPUT: rectangle
#Output: float
def rectangle_area(rectangle1: Rectangle) -> float:
    width = abs(rectangle1.top_left.x - rectangle1.bottom_right.x)
    length = abs(rectangle1.top_left.y - rectangle1.bottom_right.y)
    return length* width
# Part 6
# find the books by a given author in a list
#INPUT: authors name as a list
#Output: list of books
def books_by_author(author_name :str,books_list: list[Book])->list:
    books_by_the_author = []
    for book in books_list:
        if author_name in book.authors:
            books_by_the_author.append(book)
    return books_by_the_author


book1 = Book(["AuthorA"], "Title1")
book2 = Book(["AuthorB"], "Title2")
book3 = Book(["AuthorA"], "Title3")
books = [book1, book2, book3]
books_a = books_by_author("AuthorA", books)
print(books_a)

# Part 7
#returns the smallest circle that encompasses a rectangles points
#INPUT: rectangle
#Output: circle
def circle_bound(rectangle1: Rectangle) -> Circle:
    center_of_rectangle = Point(abs(rectangle1.top_left.x + rectangle1.bottom_right.x)/2,abs(rectangle1.top_left.y + rectangle1.bottom_right.y)/2)
    radius = math.sqrt((rectangle1.bottom_right.x-center_of_rectangle.x)**2 + (rectangle1.bottom_right.y-center_of_rectangle.y)**2)
    circle1=Circle(center_of_rectangle,radius)
    return circle1
# Part 8
#returns all Employees that have pay rates less than average
#INPUT: list of Employees
#Output: list of Employees (below average)
def below_pay_average(list1:list[Employee])->list:
    pay_rate_list = [float(x.pay_rate) for x in list1]
    average = sum(pay_rate_list)/len(list1)

    less_than_ave = []
    for employee in list1:
        if employee.pay_rate < average:
            less_than_ave.append(employee)
    return less_than_ave

