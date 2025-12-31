# construction_calculator
# Emma Kilcoyne
# Make calculations in feet and inches. Convert between fractional inches, decimal, yards


def main():


def convert_inches(feet, inches):
    # returns total number of inches
    conversion = feet * 12
    inches += conversion
    return inches

def convert_fraction(decimal):
    # round decimal to the nearest fraction with 1/16" precision
    # returns numerator and denominator

    denominator = 16
    numerator = round(decimal * 16) 

    # TO DO: make sure numerator is never zero ... this function should not be called if numerator is 0
    # while numerator is even divide the denominator by 2
    while (numerator % 2 == 0):
        denominator = denominator // 2
        numerator = numerator // 2

    return numerator, denominator

def convert_decimal(numerator, denominator):
    # returns decimal version of fraction

    decimal = numerator / denominator
    return decimal


