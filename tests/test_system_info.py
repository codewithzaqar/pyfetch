import unittest
from pyfetch.system_info import get_system_info

class TestSystemInfo(unittest.TestCase):
    def test_get_system_info(self):
        info = get_system_info()
        self.assertIsInstance(info, dict)
        self.assertIn("OS", info)
        self.assertIn("CPU", info)
        self.assertIn("Memory", info)

if __name__ == "__main__":
    unittest.main()