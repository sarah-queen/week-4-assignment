def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write the file {input_filename} or {output_filename}.")
    except IOError:
        print(f"Error: An I/O error occurred while processing the file(s).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input filename and output filename
    input_filename = input("Enter the filename to read: ")
    output_filename = input("Enter the filename to write the modified content: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
