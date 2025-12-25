import sys

# make a fraction more intuitive
# output : number out of 100
def intuitive(number):
	if float(number) <= 1 and float(number) >= 0:
		int_number =  int(float(number)*100)
		str_number = str(int_number),"out of 100"
		converted = " ".join(str_number)
		return converted
	else :
		return "Number must be between 0 and 1"

# test 
print(intuitive(sys.argv[1]))
