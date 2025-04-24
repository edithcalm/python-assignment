# Step 1: Define a function to read from a file
def read_file(filename):
    filename = filename  # The name of the file to read
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            content = file.read()         # Read the entire file content
        return content                    # Return the content
    except FileNotFoundError:
        print(f" Error: The file '{filename}' was not found.")
        return None
    except IOError:
        print(f" Error: Could not read the file '{filename}'.")
        return None


# Step 2: Define a function to modify the content
def modify_content(content):
    # Example modification: Convert content to uppercase and add a header
    modified = "=== Modified File Content ===\n" + content.upper()
    return modified


# Step 3: Define a function to write to a new file
def write_to_file(new_filename, content):
    try:
        with open(new_filename, 'w') as file:  # Open the new file in write mode
            file.write(content)               # Write modified content to the file
        return True
    except IOError:
        print(f" Error: Could not write to the file '{new_filename}'.")
        return False


# Step 4: Main program logic to call the functions in sequence
def main():
    # Ask the user to input the filename
    original_filename = input("Enter the name of the file to read: ")

    # Step 4.1: Read the file
    content = read_file(original_filename)
    if content is None:
        return  # Exit if file couldn't be read

    # Step 4.2: Modify the content
    modified = modify_content(content)

    # Step 4.3: Ask for the output filename
    new_filename = input("Enter the name for the new file to save modified content: ")

    # Step 4.4: Write to the new file
    if write_to_file(new_filename, modified):
        print(f" Success! Modified content has been saved to '{new_filename}'.")


# Step 5: Run the program
if __name__ == "__main__":
    main()
