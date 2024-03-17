def input_text():
    """
    Function to input text from console.
    """
    text = input("Enter text: ")
    return text

def read_file_builtin(file_path):
    """
    Function to read from a file using built-in Python capabilities.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def read_file_pandas(file_path):
    """
    Function to read from a file using the pandas library.
    """
    import pandas as pd
    df = pd.read_csv(file_path)
    text = df.to_string(index=False)
    return text
