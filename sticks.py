import random

def player_vs_player():
	sticks_num = 20
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

def initialize_array(sticks_num):
	ai_array = []
	for i in range(0,sticks_num + 1,1):
		ai_array.append([])
	return ai_array
		
	

def player_vs_AI(ai_dict):
	sticks_num = 20
	temp_value_save = initialize_array(sticks_num)
	
	human_turn = True
	while(sticks_num > 0):
		if(human_turn == True):
			sticks_num = take_sticks(None,sticks_num)
			human_turn = False
		else:
			chosen_value = random.choice(ai_dict[sticks_num])
			print("AI chose %d" % (chosen_value))
			temp_value_save[sticks_num].append(chosen_value)
			sticks_num -= chosen_value
			human_turn = True
	if(human_turn == False):
		ai_dict = save_choices(temp_value_save,ai_dict)
	return human_turn
		
def save_choices(temp_value_save,ai_dict):
	for i in range(0,len(temp_value_save)):
		for	value in temp_value_save[i]:
			ai_dict[i].append(value)
	return ai_dict

def train_AI(ai_dict):
	sticks_num = 20
	comp_array = initialize_array(sticks_num)
	trainer_dict = initialize_dict(sticks_num)
	trainer_array = initialize_array(sticks_num)
	player_num = 1
	chosen_value = 0
	for i in range(0,100000,1):
		
		while(sticks_num > 0):
			if(player_num == 1):
				chosen_value = random.choice(trainer_dict[sticks_num])
				trainer_array[sticks_num].append(chosen_value)
				
				player_num = 2
			else:
				chosen_value = random.choice(ai_dict[sticks_num])
				player_num = 1
				comp_array[sticks_num].append(chosen_value)
				
			sticks_num -= chosen_value
		if(player_num == 2):
			ai_dict = save_choices(comp_array,ai_dict)
		else:
			trainer_dict = save_choices(trainer_array,trainer_dict)
		
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
	while(continue_game == 1):
		print("Welcome to Sticks! Please select a game mode:\n1. Player vs. Player\n2.Train an AI\n3.Play Against a Pre-Trained AI\n4.Quit")
		choice = int(input())
		if(choice == 1):
			winner = player_vs_player()
			print("Player %d Wins!" % winner)
		elif(choice == 2):
			is_player_winner = player_vs_AI(ai_dict)
			if(is_player_winner == False):
				print("AI wins! Better luck next time!")
			else:
				print("You win!")
		elif(choice == 3):
			print("Training AI...")
			ai_dict = train_AI(ai_dict)
			print("AI trained. Starting game...")
			is_player_winner = player_vs_AI(ai_dict)
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
	


main()
