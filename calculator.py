"""Python Calculator — supports basic arithmetic and advanced operations."""

import math
import operator
from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def floor_divide(a: Number, b: Number) -> int:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return int(a // b)


def modulus(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Cannot compute modulus with zero divisor.")
    return a % b


def power(base: Number, exp: Number) -> Number:
    return base ** exp


def square_root(a: Number) -> float:
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


def absolute(a: Number) -> Number:
    return abs(a)


def logarithm(a: Number, base: Number = math.e) -> float:
    if a <= 0:
        raise ValueError("Logarithm is undefined for non-positive numbers.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(a, base)


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": floor_divide,
    "%": modulus,
    "**": power,
}

MENU = """
=== Python Calculator ===
Operations:
  +   Addition
  -   Subtraction
  *   Multiplication
  /   Division
  //  Floor Division
  %   Modulus
  **  Power
  sqrt  Square Root (single number)
  abs   Absolute Value (single number)
  log   Logarithm (number [base], default base=e)
  q   Quit
"""


def get_number(prompt: str) -> Number:
    while True:
        try:
            value = input(prompt).strip()
            return int(value) if "." not in value else float(value)
        except ValueError:
            print("  Invalid number. Please try again.")


def run_calculator() -> None:
    print(MENU)
    while True:
        op = input("Enter operation (or 'q' to quit): ").strip().lower()

        if op == "q":
            print("Goodbye!")
            break

        try:
            if op == "sqrt":
                a = get_number("  Enter number: ")
                result = square_root(a)
                print(f"  sqrt({a}) = {result}\n")

            elif op == "abs":
                a = get_number("  Enter number: ")
                result = absolute(a)
                print(f"  abs({a}) = {result}\n")

            elif op == "log":
                a = get_number("  Enter number: ")
                raw_base = input("  Enter base (press Enter for natural log): ").strip()
                if raw_base == "":
                    result = logarithm(a)
                    print(f"  ln({a}) = {result}\n")
                else:
                    base = float(raw_base)
                    result = logarithm(a, base)
                    print(f"  log_{base}({a}) = {result}\n")

            elif op in OPERATIONS:
                a = get_number("  Enter first number: ")
                b = get_number("  Enter second number: ")
                result = OPERATIONS[op](a, b)
                print(f"  {a} {op} {b} = {result}\n")

            else:
                print("  Unknown operation. Please choose from the menu.\n")

        except (ZeroDivisionError, ValueError) as e:
            print(f"  Error: {e}\n")


if __name__ == "__main__":
    run_calculator()
