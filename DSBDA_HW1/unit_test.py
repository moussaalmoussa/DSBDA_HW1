import subprocess
import unittest

class MapReduceTest(unittest.TestCase):
    def test_mapper(self):
        # Test your Mapper code
        input_data = ""
        try:
            cat_command = "hadoop fs -cat /user/mouss/input/test1.txt"
            process = subprocess.Popen(cat_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if not error:
                input_data = output.decode()
        except subprocess.CalledProcessError as e:
            print(f"Error running Hadoop fs -cat for test1.txt: {e}")

        # Split the input into lines and search for the expected output in each line
        expected_output = "example"  # "example" represents the expected word
        input_lines = input_data.split('\n')
        found = False
        for line in input_lines:
            if expected_output in line:
                found = True
                break
        self.assertTrue(found)

    def test_reducer(self):
        # Test your Reducer code
        input_data = ""
        try:
            cat_command = "hadoop fs -cat /user/mouss/input/test2.txt"
            process = subprocess.Popen(cat_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if not error:
                input_data = output.decode()
        except subprocess.CalledProcessError as e:
            print(f"Error running Hadoop fs -cat for test2.txt: {e}")

        # Split the input into lines and search for the expected output in each line
        expected_output = "turquoise"  # "turquoise" represents the expected word
        input_lines = input_data.split('\n')
        found = False
        for line in input_lines:
            if expected_output in line:
                found = True
                break
        self.assertTrue(found)

if __name__ == "__main__":
    unittest.main()
