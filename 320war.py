#https://www.reddit.com/r/dailyprogrammer/comments/6ilyfi/20170621_challenge_320_intermediate_war_card_game/


p1 = []
p2 = []

# Challenge Inputs
input1a = "5 1 13 10 11 3 2 10 4 12 5 11 10 5 7 6 6 11 9 6 33 13 6 1 8 1"
input1b = "9 12 8 3 11 10 1 4 2 4 7 9 13 8 2 13 7 4 2 8 9 12 3 12 7 5"
input1a = [int(i) for i in input1a.split(' ')]
input1b = [int(i) for i in input1b.split(' ')]

input2a = "3 11 6 12 2 13 5 7 10 3 10 4 12 11 1 13 12 2 1 7 10 6 12 5 8 1"
input2b = "9 10 7 9 5 2 6 1 11 11 7 9 3 4 8 3 4 8 8 4 6 9 13 2 13 5"
input2a = [int(i) for i in input2a.split(' ')]
input2b = [int(i) for i in input2b.split(' ')]

input3 = "1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13"
input3 = [int(i) for i in input3.split(' ')]

def compare(card1, card2):
	global p1, p2
	print("Compare: ", card1, ", ", card2)
	if card1 > card2: # player1 wins
		p1 = p1 + [card1, card2]
		return 1
	elif card2 > card1: #player2 wins
		p2 = p2 + [card2, card1]
		return 2
	else: # draw
		return(war(card1, card2))

def play():
	global p1, p2
	while p1 and p2:
		card1 = p1.pop(0)
		card2 = p2.pop(0)
		compare(card1, card2)

	if not p1 and p2:
		return 2 # p2 wins
	elif not p2 and p1:
		return 1 # p1 wins
	else:
		return 0 # no one wins

def war(wp1, wp2):
	global p1, p2

	# determine size of war
	warNum = 4
	if len(p1) > 0 and len(p2) > 0: # incase player out of cards
		if len(p1) < 4 or len(p2) < 4:
			warNum = min(len(p1), len(p2))
	else: # if somebody is out of cards at this stage they lose
		if len(p1) != 0:
			return 1
		elif len(p2) != 0:
			return 2
		else:
			return 0

	# format card1 and card2 into list, where
	# wp1 and wp2 are the war 'decks'
	if isinstance(wp1, int) and isinstance(wp2, int):
		wp1 = [wp1]
		wp2 = [wp2]

	# draw wager
	for i in range(warNum):
		wp1.insert(0, p1.pop(0))
		wp2.insert(0, p2.pop(0))

	# determine who wins war
	card1 = p1.pop(0)
	card2 = p2.pop(0)
	result = compare(card1, card2)

	assert len(wp1) == len(wp2), "Length of war piles do not match."
	# winner take all
	if result == 1:
		p1 += [card1, card2]
		p1 += [card for tupl in zip(wp1, wp2) for card in tupl]
		return 1

	elif result == 2:
		p2 += [card2, card1]
		p2 += [card for tupl in zip(wp2, wp1) for card in tupl]
		return 2

	else: # draw state
		return 0

def result(winner):
	if winner:
		print("Player ", winner, " wins!")
	else:
		print("DRAW!")

def runChallenge():
	global p1, p2
	print("Challenge 1:")
	p1 = input1a
	p2 = input1b
	result(play())

	p1 = input2a
	p2 = input2b
	result(play())

	p1 = p2 = input3
	result(play())


runChallenge()
