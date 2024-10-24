
from data import Price,Rectangle,Point,Book,Circle,Employee
import hw1
import unittest


# Write your test cases for each part below...
import math
import unittest
from data import Price, Rectangle, Point, Book, Circle, Employee


class TestMethods(unittest.TestCase):

    # Part 1
    def test_vowel_count_1(self):
        self.assertEqual(hw1.vowel_count("Hello World"), 3)  # 'e', 'o', 'o'

    def test_vowel_count_2(self):
        self.assertEqual(hw1.vowel_count("Python"), 1)  # 'o'

    # Part 2
    def test_shorts_list_1(self):
        self.assertEqual(hw1.shorts_list([[1, 2], [3, 4], [5]]), [[1, 2], [3, 4]])  # Two lists of length 2

    def test_shorts_list_2(self):
        self.assertEqual(hw1.shorts_list([[1], [2], [3, 4, 5]]), [])  # No lists of length 2

    # Part 3
    def test_ascending_pairs_1(self):
        self.assertEqual(hw1.ascending_pairs([[3, 1], [2, 2], [1, 4]]), [[1, 3], [2, 2], [1, 4]])  # Sorted pairs

    def test_ascending_pairs_2(self):
        self.assertEqual(hw1.ascending_pairs([[5, 5], [0, 1], [2, 3]]), [[5, 5], [0, 1], [2, 3]])  # Already sorted

    # Part 4
    def test_add_prices_1(self):
        price1 = Price(5, 75)  # $5.75
        price2 = Price(3, 50)  # $3.50
        result = hw1.add_prices(price1, price2)
        self.assertEqual((result.dollars, result.cents), (9, 25))  # $9.25

    def test_add_prices_2(self):
        price3 = Price(2, 99)  # $2.99
        price4 = Price(0, 2)  # $0.02
        result = hw1.add_prices(price3, price4)
        self.assertEqual((result.dollars, result.cents), (3, 1))  # $3.01

    # Part 5
    def test_rectangle_area_1(self):
        rect = Rectangle(Point(0, 0), Point(4, 3))
        self.assertEqual(hw1.rectangle_area(rect), 12)  # Area = width * length = 4 * 3

    def test_rectangle_area_2(self):
        rect2 = Rectangle(Point(1, 1), Point(5, 4))
        self.assertEqual(hw1.rectangle_area(rect2), 12)  # Area = 4 * 3

    # Part 6
    def test_books_by_author_1(self):
        book1 = Book(["AuthorA"], "Title1")
        book2 = Book(["AuthorB"], "Title2")
        book3 = Book(["AuthorA"], "Title3")
        books = [book1, book2, book3]
        actual = hw1.books_by_author("AuthorA", books)
        expected = [Book(["AuthorA"], "Title1"), Book(["AuthorA"], "Title3")]

        self.assertEqual(expected, actual)  # Two books by AuthorA

    def test_books_by_author_2(self):
        book1 = Book(["AuthorA"], "Title1")
        book2 = Book(["AuthorB"], "Title2")
        book3 = Book(["AuthorA"], "Title3")
        books = [book1, book2, book3]
        actual = hw1.books_by_author("AuthorB",books)
        expected = [Book(["AuthorB"],"Title2")]

        self.assertEqual(expected, actual)  # One book by AuthorB

    # Part 7
    def test_circle_bound_1(self):
        rect = Rectangle(Point(0, 0), Point(4, 4))
        circle = hw1.circle_bound(rect)
        self.assertEqual((circle.center.x, circle.center.y), (2.0, 2.0))  # Center should be at (2, 2)

    def test_circle_bound_2(self):
        rect = Rectangle(Point(0, 0), Point(4, 4))
        circle = hw1.circle_bound(rect)
        self.assertAlmostEqual(circle.radius, math.sqrt(8))  # Radius should be sqrt(8)

    # Part 8
    def test_below_pay_average_1(self):
        emp1 = Employee("Alice", 20)
        emp2 = Employee("Bob", 30)
        emp3 = Employee("Charlie", 25)
        employees = [emp1, emp2, emp3]

        self.assertEqual(len(hw1.below_pay_average(employees)), 1)  # Only Alice is below average

    def test_below_pay_average_2(self):
        emp1 = Employee("Alice", 20)
        emp2 = Employee("Bob", 30)
        emp3 = Employee("Charlie", 25)
        employees = [emp1, emp2, emp3]
        self.assertEqual(hw1.below_pay_average(employees)[0].name, "Alice")


if __name__ == '__main__':
    unittest.main()


