import math
class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    @staticmethod
    def get_whole(number):
        return math.floor(number)

    """
    Method to get the fractional part of a double number
    """
    @staticmethod
    def get_fraction(number):
        whole = math.floor(number)
        return (number-whole)

    """
    Method to check if a given number is odd or even
    """
    @staticmethod
    def is_odd(number):
        if number%2 == 0 :
            return "even"
        else:
            return "odd"
