from app.io.input import input_text, read_file_builtin, read_file_pandas
from app.io.output import output_text, write_file_builtin

def main():
    # Input text from console
    text_console = input_text()

    # Read from a file using built-in Python capabilities
    file_path = "data/input/sample.txt"
    text_builtin = read_file_builtin(file_path)

    # Read from a file using pandas
    csv_file_path = "data/input/sample.csv"
    text_pandas = read_file_pandas(csv_file_path)

    # Output to console
    output_text(text_console)
    output_text(text_builtin)
    output_text(text_pandas)

    # Write to a file using built-in Python capabilities
    write_file_builtin(text_console, "data/output/console_output.txt")
    write_file_builtin(text_builtin, "data/output/builtin_output.txt")
    write_file_builtin(text_pandas, "data/output/pandas_output.txt")

if __name__ == "__main__":
    main()
