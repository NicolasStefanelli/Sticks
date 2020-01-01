import random

def player_vs_player(num):
	sticks_num = num
	player_num = 1
	while(sticks_num > 0):
		sticks_num = take_sticks(player_num,sticks_num)
		if(player_num == 2):
			player_num = 1
		else:
			player_num = 2
	
	return player_num
	
def initialize_dict(sticks_num):
	ai_dict = {}
	for i in range(1,sticks_num + 1,1):
		#print(i)
		if(i >= 3):
			ai_dict[i] = [1,2,3]
		elif(i == 2):
			ai_dict[i] = [1,2]
		elif(i == 1):
			ai_dict[i] = [1]
	#print(ai_dict)
	return ai_dict

def initialize_bdict(sticks_num):
	ai_dict = {}
	for i in range(1,sticks_num + 1,1):
		ai_dict[i] = []
	return ai_dict
		
	

def player_vs_AI(ai_dict,num):
	sticks_num = num
	besides_dict = initialize_bdict(sticks_num)
	
	human_turn = True
	while(sticks_num > 0):
		if(human_turn == True):
			sticks_num = take_sticks(None,sticks_num)
			human_turn = False
		else:
			chosen_value = random.choice(ai_dict[sticks_num])
			print(ai_dict[sticks_num])
			print("AI chose %d" % (chosen_value))
			besides_dict[sticks_num].append(chosen_value)
			ai_dict[sticks_num].remove(chosen_value)
			sticks_num -= chosen_value
			human_turn = True
	if(human_turn == False):
		ai_dict = update_hats(besides_dict,ai_dict,True)
	else:
		ai_dict = update_hats(besides_dict,ai_dict,False)
	return human_turn
		
def update_hats(temp_value_save,ai_dict,winner):
	
	for i in temp_value_save.keys():
		for	value in temp_value_save[i]:
			if(winner == True):
				ai_dict[i].append(value)
				ai_dict[i].append(value)
			else:
				if value not in ai_dict[i]:
					ai_dict[i].append(value)

	return ai_dict

def train_AI(ai_dict,num):
	sticks_num = num
	comp_besides = initialize_bdict(sticks_num)
	comp_besides_blank = comp_besides
	print(comp_besides_blank)
	trainer_dict = initialize_dict(sticks_num)
	trainer_besides = initialize_bdict(sticks_num)
	trainer_besides_blank = trainer_besides
	player_num = 1
	chosen_value = 0
	for i in range(1000):
		#print(i)
		while(sticks_num > 0):
			if(player_num == 1):
				chosen_value = random.choice(trainer_dict[sticks_num])
				trainer_dict[sticks_num].remove(chosen_value)
				#print(" 1 Number Searched: %d" % sticks_num)
				trainer_besides[sticks_num].append(chosen_value)
				sticks_num -= chosen_value
				player_num = 2
			else:
				chosen_value = random.choice(ai_dict[sticks_num])
				#print(" 2 Number Searched: %d" % sticks_num)
				comp_besides[sticks_num].append(chosen_value)
				ai_dict[sticks_num].remove(chosen_value)
				sticks_num -= chosen_value
				player_num = 1
			

		# print("Game: %d" % (i))
		if(len(comp_besides[1]) == 0):
			#print("AI Dict win")
			ai_dict = update_hats(comp_besides,ai_dict,True)
			trainer_dict = update_hats(trainer_besides,trainer_dict,False)
		elif ((len(trainer_besides[1])) == 0):
			#print("trainer win")
			trainer_dict = update_hats(trainer_besides,trainer_dict,True)
			ai_dict = update_hats(comp_besides,ai_dict,False)
		else:
			print("WARNING: no hats updated")
			print(trainer_besides[1])
			print(comp_besides[1])

		
		
		sticks_num = num
		player_num = 1
		comp_besides = initialize_bdict(sticks_num)
		trainer_besides = initialize_bdict(sticks_num)
	return ai_dict

def take_sticks(player_num,sticks_num):
	sticks_to_take = 3
	
	if(sticks_to_take > sticks_num):
		sticks_to_take = sticks_num
		
	print("\n%d sticks remain." % sticks_num)
	if(player_num != None):
		print("Player %d, please select the number of sticks you would like to remove (1-%d)." % (player_num,sticks_to_take))
	else:
		print("Player, please select the number of sticks you would like to remove (1-%d)." % (sticks_to_take))
	removed_sticks = int(input())
	
	while(removed_sticks > sticks_num or removed_sticks > 3 or removed_sticks <= 0):
		print("Please input an appropriate number of sticks (1-3)")
		removed_sticks = int(input())
		
	sticks_num -= int(removed_sticks)
	return sticks_num


	
	
		
def main():
	continue_game = 1
	ai_dict = initialize_dict(20)
	trained_dict = False
	print("Welcome to the Game of Sticks\nHow many sticks are there on the table initially (10-100)?")
	sticks_num = int(input())
	ai_dict = initialize_dict(sticks_num)
	while(continue_game == 1):
		print("Options\n1. Player vs. Player\n2.Train an AI\n3.Play Against a Pre-Trained AI\n4.Quit")
		choice = int(input())
		if(choice == 1):
			winner = player_vs_player(sticks_num)
			print("Player %d Wins!" % winner)
		elif(choice == 2):
			is_player_winner = player_vs_AI(ai_dict,sticks_num)
			if(is_player_winner == False):
				print("AI wins! Better luck next time!")
			else:
				print("You win!")
		elif(choice == 3):
			if(trained_dict == False):
				print("Training AI...")
				ai_dict = train_AI(ai_dict,sticks_num)
				trained_dict = True
				print("AI trained. Starting game...")
			print_ai(ai_dict)
			is_player_winner = player_vs_AI(ai_dict,sticks_num)
			if(is_player_winner == False):
				print("AI wins! Better luck next time!")
			else:
				print("You win!")
			pass
		elif(choice == 4):
			break
	
		print("Play again?\n\t1 = yes\n\t0 = no")
		continue_game = int(input())
	print("Thank you for Playing Sticks")
	
def print_ai(ai_dict):
	out_file = open("dict_analysis.txt","w")
	for item in ai_dict.keys():
		out_file.write("Hat:" + " "  + str(item)+ " " + "(")
		out_file.write(str(ai_dict[item].count(1)) + " " +",")
		out_file.write(str(ai_dict[item].count(2)) + " " + ",")
		out_file.write(str(ai_dict[item].count(3)))
		out_file.write(")\n")
	out_file.close()
	return 0

main()
