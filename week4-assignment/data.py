def modify_line(line):
    # Example modification: convert text to uppercase
    return line.upper()

def main():
    input_file = input("Enter the name of the file to read from: ")
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        # Modify each line
        modified_lines = [modify_line(line) for line in lines]

        # Define output file name
        output_file = "modified_" + input_file
        
        with open(output_file, 'w') as f:
            f.writelines(modified_lines)
        
        print(f"Modified content written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(" Error: The file was not found.")
    except IOError:
        print(" Error: The file could not be read or written.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()