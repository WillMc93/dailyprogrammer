"""
Define translation dictionaries
"""
hour_num = {'00': 'twelve',	'01': 'one', '02': 'two', '03': 'three', '04': 'four',
			'05': 'five', '06': 'six', '07': 'seven', '08': 'eight', '09': 'nine',
			'10': 'ten', '11': 'eleven'}

min_one = {'0': 'oh', '1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty'}
min_two = {'0': ''}
min_teens = {'11': 'eleven', '12': 'twelve', '13': 'thirteen', '15':'fifteen', '18': 'eighteen'}

"""
Define generator functions for translation dictionaries
"""
def gen_hour_num():
	# Hours > 11 are already entered into hour num, so all we have to do is
	# add the existing value to the dictionary
	for i in range(12, 24):
		val = i - 12
		prev = str(val)
		# add the zero if necessary
		if val < 10:
			prev = '0' + prev
		hour_num[str(i)] = hour_num[prev]
	return hour_num


def gen_min_num():
	# The numbers we're looking for already exist in hour_nums, so all we
	# have to do if format and add them to the dicationary
	for i in range(1, 10):
		prev = '0' + str(i)
		min_two[str(i)] = hour_num[prev]

	for i in range(14, 20):
		if str(i) not in min_teens.keys():
			min_teens[str(i)] = hour_num['0' + str(i)[1]] + 'teen'

"""
Define the translator function
"""
def talk_clk(time):
	# Initialize output and am/pm
	output = 'It\'s '
	am_pm = 'am'

	# Check our dictionaries and initialize if necessary
	if len(hour_num) < 24:
		gen_hour_num()
	if len(min_two) < 10 or len(min_teens) < 9:
		gen_min_num()

	# Split the input at the colon and store appropriately
	time = time.split(':')
	assert len(time[0]) > 0 and len(time[0]) < 3, "The input string was formated incorrectly."
	assert len(time[1]) > 0 and len(time[1]) < 3, "The input string was formated incorrectly."
	hour = time[0]
	minutes = time[1]

	# If past twelve set am/pm to pm
	if int(hour) > 11:
		am_pm = 'pm'

	# Add hours to output
	output += hour_num[str(hour)] + ' '

	# If minutes is a teen add the proper value
	if int(minutes) > 10 and int(minutes) < 20:
		output += min_teens[minutes] + ' '
	# Else figure out what values we need
	else:
		output += min_one[minutes[0]] + ' '

		if len(minutes) > 1:
			output += min_two[minutes[1]] + ' '

	output += am_pm
	return output


# Run test
sample = ['00:00', '01:30', '12:05', '14:01', '20:29', '21:00', '12:12']

for smpl in sample:
	print(talk_clk(smpl))
