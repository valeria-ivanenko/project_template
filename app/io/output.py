def output_text(text):
    """
    Function to output text to console.
    """
    print(text)

def write_file_builtin(text, file_path):
    """
    Function to write to a file using built-in Python capabilities.
    """
    with open(file_path, 'w') as file:
        file.write(text)
