import unittest
import runner 

class TestRunner(unittest.TestCase):

    def setUp(self):
        self.runner = runner.Runner()

    def test_exampleRun_no_args(self):
        result = self.runner.run("exampleRun", [])
        self.assertEqual(result, 0)

    def test_exampleRun_with_args(self):
        result = self.runner.run("concatArgs", ["arg1", "arg2"])
        self.assertEqual(result, "arg1,arg2")

    def test_invalid_function_key(self):
        with self.assertRaises(KeyError):
            self.runner.run("nonExistentFunction", [])

if __name__ == "__main__":
    unittest.main()