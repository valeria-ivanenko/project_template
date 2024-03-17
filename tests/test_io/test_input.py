import unittest
from app.io.input import read_file_builtin, read_file_pandas

class TestReadFile(unittest.TestCase):
    def test_read_file_builtin(self):
        file_path = "../../data/input/sample.txt"
        expected_text = "Hello World! This .txt was created by Valeriia Ivanenko"
        actual_text = read_file_builtin(file_path)
        self.assertEqual(actual_text.strip(), expected_text)

    def test_read_file_pandas(self):
        csv_file_path = "../../data/input/sample.csv"
        expected_text = "Empty DataFrame\nColumns: [Hello]\nIndex: []"
        actual_text = read_file_pandas(csv_file_path)
        self.assertEqual(actual_text.strip(), expected_text)

if __name__ == "__main__":
    unittest.main()
