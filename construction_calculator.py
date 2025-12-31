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
    #round decimal to the nearest fraction with 1/16" precision
    #returns numerator and denominator

    denominator = 16
    numerator = round(decimal * 16) 

    if (numerator % 2 == 0):
        
