"""
FILE:		Currency Conversion Functions
TITLE:		Create specilized functions from a general function
AUTHOR:		Daniel R. South

DESCRIPTION:	From a general function that returns the product of two numbers,
		create specific-purpose functions what will return an amount in
		US Dollars when passed a value in their specific currency.

		dollars_from_cad returns a value in USD equivalent to an amount of Canadian dollars.
		etc.

PROGRAM OUTPUT:

Canadian dollars
CAD 10.00 = USD 7.30
CAD 100.00 = USD 73.00
CAD 1000.00 = USD 730.00
CAD 10000.00 = USD 7300.00
CAD 100000.00 = USD 73000.00
CAD 1000000.00 = USD 730000.00

Euro currency
EUR 10.00 = USD 10.90
EUR 100.00 = USD 109.00
EUR 1000.00 = USD 1090.00
EUR 10000.00 = USD 10900.00
EUR 100000.00 = USD 109000.00
EUR 1000000.00 = USD 1090000.00

Indian Rupies
INR 10.00 = USD 0.12
INR 100.00 = USD 1.20
INR 1000.00 = USD 12.00
INR 10000.00 = USD 120.00
INR 100000.00 = USD 1200.00
INR 1000000.00 = USD 12000.00

Japanese Yen
JPY 10.00 = USD 0.07
JPY 100.00 = USD 0.66
JPY 1000.00 = USD 6.60
JPY 10000.00 = USD 66.00
JPY 100000.00 = USD 660.00
JPY 1000000.00 = USD 6600.00

"""

dollars_to_cad	= 0.73
dollars_to_eur	= 1.09
dollars_to_inr	= 0.012
dollars_to_jpy	= 0.0066

powers_of_ten 	= [10**x for x in range(7) if x > 0]

# Define a general function that returns the product of two numbers
def convert_curr(rate):
	return lambda amount : amount * rate

# Define a function for each currency.
dollars_from_cad = convert_curr(dollars_to_cad)
dollars_from_eur = convert_curr(dollars_to_eur)
dollars_from_inr = convert_curr(dollars_to_inr)
dollars_from_jpy = convert_curr(dollars_to_jpy)

# Demonstrate each of the specialized functions in action
print("\nCanadian dollars")
for in_cad in powers_of_ten:
	in_usd = dollars_from_cad(in_cad)
	print("CAD {:.2f} = USD {:.2f}".format(in_cad, in_usd))

print("\nEuro currency")
for in_eur in powers_of_ten:
	in_usd = dollars_from_eur(in_eur)
	print("EUR {:.2f} = USD {:.2f}".format(in_eur, in_usd))

print("\nIndian Rupies")
for in_inr in powers_of_ten:
	in_usd = dollars_from_inr(in_inr)
	print("INR {:.2f} = USD {:.2f}".format(in_inr, in_usd))

print("\nJapanese Yen")
for in_jpy in powers_of_ten:
	in_usd = dollars_from_jpy(in_jpy)
	print("JPY {:.2f} = USD {:.2f}".format(in_jpy, in_usd))
