import unittest
import io

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # Capturar la salida estándar de la función
        output = io.StringIO()
        import sys
        original_stdout = sys.stdout
        sys.stdout = output
        fizzbuzz()
        sys.stdout = original_stdout

        # Convertir la salida a una lista de cadenas
        output = output.getvalue().splitlines()

        # Comprobar que la salida tiene 100 elementos
        self.assertEqual(len(output), 100)

        # Comprobar que los múltiplos de 3 y 5 se imprimen como "fizzbuzz"
        for i in range(15, 101, 15):
            self.assertEqual(output[i-1], "fizzbuzz")

        # Comprobar que los múltiplos de solo 3 se imprimen como "fizz"
        for i in range(3, 101, 3):
            if i % 5 != 0:
                self.assertEqual(output[i-1], "fizz")

        # Comprobar que los múltiplos de solo 5 se imprimen como "buzz"
        for i in range(5, 101, 5):
                if i % 3 != 0:
                    self.assertEqual(output[i-1], "buzz")

        if __name__ == "__main__":
            unittest.main()
            
import codewars_test as test
from solution import sum_two_smallest_numbers

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)