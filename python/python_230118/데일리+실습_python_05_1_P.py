import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list


trump_card_list = making_card_list()

count1 = 0
count2 = 0
alp = {'A':3, 'K':2, 'Q':1, 'J':0}
shp = {'spade':3, 'diamond':2, 'heart':1, 'clover':0}
while count1 !=6 or count2 != 6:
	random_choice = random.sample(trump_card_list, k=2)
	player1 = random_choice[0]
	player2 = random_choice[1]
	

