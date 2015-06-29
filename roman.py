from sys import argv 
script, x,y = argv

def convertRomanToDec(r):
	numerals = {
		"I":1,
		"V":5,
		"X":10,
		"L":50,
		"C":100,
		"D":500,
		"M":1000
	}
	decimal = 0
	
	for i in reversed(list(r)):
		if decimal == 0:
			lastDigit = numerals[i]
			decimal = numerals[i]
		else:
			if numerals[i] >= lastDigit:
				decimal += numerals[i]
				lastDigit = numerals[i]

			elif numerals[i] < lastDigit:
				decimal -= numerals[i]
				lastDigit = numerals[i]

	return decimal
	#2888 MMDCCCLXXXVIII

def convertDecToRoman(d):
	numbers = [1,4,5,9,10,50,100,500,1000]
	numerals = {
		1000:"M",
		500:"D",
		400:"CD",
		100:"C",
		50:"L",
		40:"XL",
		10:"X",
		9:"IX",
		5:"V",
		4:"IV",
		1:"I"
	}
	result = ''
	#divide/ modulo in decending order? 
	for i in reversed(numbers):
		if d/i > 0:
			currentDigit = numerals[i]
			result += currentDigit*(d/i)
			d -= (d/i)*i 
	return result

def tester(x,y):
	for i in range(x,y):
		r =  convertDecToRoman(i)
		d = convertRomanToDec(convertDecToRoman(i))
		if (i != d):
			print i,r,d

tester(int(x),int(y))
