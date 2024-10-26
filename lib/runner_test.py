import unittest
from runner import Runner

class TestRunner(unittest.TestCase):
    def setUp(self):
        self.runner = Runner()
        
        def exampleRun() -> int:
            return 0

        def concatArgs(arg1:str, arg2:str) -> str:
            return ",".join([arg1, arg2])
        
        def concatList(args:list[str]) -> str: 
            return ",".join(args)

        self.runner.register("exampleRun", exampleRun)
        
        self.runner.register("concatArgs", concatArgs)
        
        self.runner.register("concatList", concatList)

    def test_exampleRun_no_args(self):
        result = self.runner.run("exampleRun", [])
        self.assertEqual(result, 0)

    def test_exampleRun_with_args(self):
        result = self.runner.run("concatArgs", ["arg1", "arg2"])
        self.assertEqual(result, "arg1,arg2")
        
    def test_exampleRun_with_listArg(self): 
        result = self.runner.run("concatList", [["arg1", "arg2"]])
        self.assertEqual(result, "arg1,arg2")

    def test_invalid_function_key(self):
        result = self.runner.run("nonExistentFunction", [])
        self.assertEqual(result, None)
            

if __name__ == "__main__":
    unittest.main()