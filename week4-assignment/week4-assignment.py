try:
	file = open("data.txt", "r")
	data = file.read()
	file.close()

	modified_data = data.upper()
	new_file = open("modified.txt", "w")
	new_file.write(modified_data)

	new_file.close()

	print("The file was read, modified, and saved successfully.")

except FileNotFoundError:
	print("Oops! The file 'data.txt' was not found.")
