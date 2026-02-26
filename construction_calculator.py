# construction_calculator
# Emma Kilcoyne
# Make calculations in feet and inches. Convert between fractional inches, decimal, yards
import tkinter as tk

def main():

    calculation = ""

    while(true):
        #recieve input
        
        window = tk.Tk()
        window.geometry("300x300")
        display = tk.Text(window, height=2, width=21, font=("Times New Roman", 20))
        display.grid(row=1, column=1, columnspan=4)
        window.mainloop()
        #do something with the input


def convert_inches(feet, inches):
    # returns total number of inches
    conversion = feet * 12
    inches += conversion
    return inches

def convert_sixteenths(feet, inches, numerator):
    # converts everything to sixteenths of an inch for calculations
    inches = convert_inches(feet, inches)
    total = (inches * 16) + numerator
    return total

    
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


def process_input(input):
# process input and update display
    global display
    display = display + str(input)
    display.delete("1.0", "end")
    display.insert("1.0", display)
    return

def calculate():
# calculate what is currently displayed
# TO DO : change calculation based on mode...(fraction, decimal etc.)
    global display
    calculation = str(display)
    
    display.delete("1.0", "end")
    display.insert("1.0", result)

def clear_input():
# 
    return