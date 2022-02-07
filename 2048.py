# 2048.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic

# Driver code
if __name__ == '__main__':
	
# calling start_game function
# to initialize the matrix
	mat = logic.start_game()

while(True):

	# taking the user input
	# for next step
	x = input("Press the command : ")

	# we have to move left
	if(x == '1' ):

		# call the move_up function
		mat, flag = logic.move_left(mat)

		# get the current state and print it
		status = logic.get_current_state(mat)
		print(status)

		# if game not ove then continue
		# and add a new two
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)

		# else break the loop
		else:
			break

	# the above process will be followed
	# in case of each type of move
	# below

	# to move right
	elif(x == '2'):
		mat, flag = logic.move_right(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# to move up
	elif(x == '3'):
		mat, flag = logic.move_up(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# to move right
	elif(x == '4'):
		mat, flag = logic.move_down(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break
	else:
		print("Invalid Key Pressed")

	print(mat)
