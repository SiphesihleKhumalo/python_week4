def read_file_content_safely():
  while True:
    file_name = input("please Enter the file name to read: ")

    try:
      with open(file_name, "r") as file:
        contents =file.read()
        print("\n Contents of the file:")
        print(contents)
        return contents
      
    except FileNotFoundError:
      print(f"Error: The file '{file_name}' was not found. Please try again.")
    except IsADirectoryError:
      print(f"Error: '{file_name}' is a directory, not a file. Please try again.")
    except PermissionError:
      print(f"Error: Permission denied to read the file '{file_name}'. Please try again.")
    except Exception as e:
      print(f"An unexpected error occurred: {e}. Please try again.")
    except UnicodeDecodeError:
      print(f"Error: The file '{file_name}' contains invalid characters. Please try again.")

if __name__ == "__main__":
  print("Welcome to the file reader program!")
  print("")
    file_contents = read_file_content_safely()

    if file_contents is not None:
        modified_contents = modify_content(file_contents)
        write_content_safely(modified_contents)