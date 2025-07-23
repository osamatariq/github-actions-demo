from main import backwards_string, get_mode
import unittest
import os


class TestMain(unittest.TestCase):
    def test_backward_string(self):
        random_string = "This is a Test String"
        reversed_string = "gnirtS tseT a si sihT"
        self.assertEqual(reversed_string, 
                         backwards_string(random_string))
        
    def test_get_env(self):
        self.assertEqual(os.environ.get("MODE"), get_mode())

    
if __name__ == "__main__":
    unittest.main()