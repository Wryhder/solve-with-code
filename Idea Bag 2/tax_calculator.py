"""
Problem Statement: 

Develop a program that asks the user to enter a cost and either a country or state tax. 
It then returns the tax plus the total cost with tax.

Source: https://play.google.com/store/apps/details?id=com.alansa.ideabag2
"""

def tax_calculator():
    cost = int(raw_input("enter cost:"))
    tax = int(raw_input("enter country/state tax:"))
    print "tax =", tax, "\n", "total =", cost + tax

tax_calculator()
