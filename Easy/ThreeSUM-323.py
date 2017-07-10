challenge_input1 = [4,5,-1,-2,-7,2,-5,-3,-7,-3,1]
challenge_input2 = [-1,-6,-3,-7,5,-8,2,-8,1]
challenge_input3 = [-5,-1,-4,2,9,-9,-6,-1,-7]


def threesum(inp):
	output = set() # container for the output
	inp.sort() # sort the input so we aren't looking everywhere
	for idx in range(len(inp) - 3):
		sdx = idx + 1 # start index
		edx = len(inp) - 1 # end index
		a = inp[idx]
		while sdx < edx:
			b = inp[sdx]
			c = inp[edx]
			if a+b+c == 0:
				output.add((a,b,c))
				edx -= 1
			elif a+b+c > 0:
				edx -= 1
			else:
				sdx += 1
	return output

print(threesum(challenge_input1))
print(threesum(challenge_input2))
print(threesum(challenge_input3))
