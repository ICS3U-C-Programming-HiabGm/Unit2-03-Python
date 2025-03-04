# Created by: Hiab G
# Date: Wed, Feb. 28th
# This program 
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process 
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    tax = constants.HST * subtotal
    total = subtotal + tax

    #output 
    print("")
    print("The total cost is = ${:.2f}".format(total))

if __name__ == "__main__":
    main()
