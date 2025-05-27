import unittest
from pyfetch.system_info import get_system_info
from pyfetch.display import display_info

class TestSystemInfo(unittest.TestCase):
    def test_get_system_info(self):
        info = get_system_info()
        self.assertIsInstance(info, dict)
        self.assertIn("OS", info)
        self.assertIn("CPU", info)
        self.assertIn("Memory", info)
        self.assertIn("Shell", info)

    def test_display_selected_fields(self):
        # Simulate display with specific fields
        info = get_system_info()
        selected_fields = ["OS", "CPU"]
        filtered_info = {k: v for k, v in info.items() if k in selected_fields}
        self.assertEqual(len(filtered_info), 2)
        self.assertIn("OS", filtered_info)
        self.assertIn("CPU", filtered_info)

if __name__ == "__main__":
    unittest.main()