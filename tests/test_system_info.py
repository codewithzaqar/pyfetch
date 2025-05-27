import unittest
from pyfetch.system_info import get_system_info
from pyfetch.display import display_info
from pyfetch.config import load_config

class TestSystemInfo(unittest.TestCase):
    def test_get_system_info(self):
        info = get_system_info()
        self.assertIsInstance(info, dict)
        self.assertIn("OS", info)
        self.assertIn("CPU", info)
        self.assertIn("Memory", info)
        self.assertIn("Disk", info)
        self.assertIn("Shell", info)
        self.assertIn("Packages", info)

    def test_display_selected_fields(self):
        info = get_system_info()
        selected_fields = ["OS", "CPU", "Packages"]
        filtered_info = {k: v for k, v in info.items() if k in selected_fields}
        self.assertEqual(len(filtered_info), 3)
        self.assertIn("OS", filtered_info)
        self.assertIn("CPU", filtered_info)
        self.assertIn("Packages", filtered_info)

    def test_load_config_with_ascii(self):
        config = load_config()
        self.assertIsInstance(config, dict)
        self.assertIn("no_art", config)
        self.assertIn("color_key", config)
        self.assertIn("ascii_art", config)

if __name__ == "__main__":
    unittest.main()