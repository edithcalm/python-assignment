try:
	file = open('data.txt', "r")
	data = file.read()
	file.close()

	modified_data = data.upper()
	file = open('modified.txt', "w")
	file.write(modified_data)

	file.close()

	print("The file was read, modified, and saved successfully.")

except FileNotFoundError:
	print("Oops! The file 'data.txt' was not found.")

filename = input("Enter the name of the file you want to read: ")
try:
	file = open("filename", "r")
	print("\n:Here is the content of the file:")
	print(file.read())
	file.close()
except FileNotFoundError:
    print("Sorry, that file does not exist. Please check the name and try again.")
except Exception as error:
    print(f"Something went wrong: {error}")

