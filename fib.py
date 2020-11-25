fir = 0
sec = 1

fg = input("Enter 'f' for Fibonacci's sequence or 'g' for Golden Ratio sequence: ").lower()

# Text will be shown in red in the terminal
ip = input("Enter how far you want to see the sequence go, or don't specify any value to make it go on forever: ")

if fg == "f":

	# Printing the start of the seq
	print(fir)
	print(sec)

	# If no input given then go on forever
	if ip == "":
	    while True:
	        j = fir + sec 

	        print(j) 

	        # Give fir, sec's value because sec is now fir
	        fir = sec 
	        # Make sec = fir + sec
	        sec = j 

	# Else go only till specified input
	else:
	    for i in range(int(ip) - 2):
	        f = fir + sec 
 
	        print(f) 
	        
	        # Give fir, sec's value because sec is now fir
	        fir = sec 
	        # Make sec = fir + sec
	        sec = f 

# Golden Ration - bigger/smaller numbers in the sequence. 
# As sequence progresses, this number tends towards 1.618 --> The Golden Ratio       
else:
	if ip == "":
		while True:
			f = fir + sec 

			# To show the GOLDEN RATIO
			try:
				g = sec / fir # Golden Ratio
				print(g)
			except ZeroDivisionError:
				print("-")    
			
			# Give fir, sec's value because sec is now fir
			fir = sec 
			# Make sec = fir + sec
			sec = f 
	else:
		for i in range(int(ip) - 2):
			f = fir + sec 

			# To show the GOLDEN RATIO
			try:
				g = sec / fir # Golden Ratio
				print(g)
			except ZeroDivisionError:
				print("-")    
			
			# Give fir, sec's value because sec is now fir
			fir = sec 
			# Make sec = fir + sec
			sec = f 