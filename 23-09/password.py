def get_new_password():

	password = input("Enter new password: ")
	count = 0
	try:	
		if len(password) < 8:
			raise ValueError

		for i in list(password):
			if i in ['0','1','2','3','4','5','6','7','8','9','0']:
				break
			else:
				count+=1

		if count == len(password):
			raise TypeError
		else:
			password_sec = input("Enter password second time: ")
			if password != password_sec:
				raise IOError
			else:
				print("Fine. Remember ur password: ", password_sec)
	except KeyboardInterrupt:
		print("Not so quickly, dude! First enter the valid password! Try again.")
		get_new_password()
	except IOError:
		print('IOError. Match failed. Try again.')
		get_new_password()
	except ValueError:
		print('ValueError. Lenght should be bigger than 8. Try again.')
		get_new_password()
get_new_password()
