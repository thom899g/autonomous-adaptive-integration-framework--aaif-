import unittest
from aaif import AAIF
from adapter_base import BaseAdapter

class TestAAIF(unittest.TestCase):
    
    def setUp(self):
        self.aaif = AAIF()
        
    def test_initialize(self):
        config = {
            "adapters": [
                {"name": "test_adapter", "type": "test"}
            ]
        }
        self.aaif.initialize(config)
        self.assertEqual(len(self.aaif.adapters), 1)
        
    def test_get_adapter(self):
        self.aaif.initialize({
            "adapters": [{"name": "adapter1"}]
        })
        adapter = self.aaif.get_adapter("adapter1")
        self.assertIsNotNone(adapter)
        
if __name__ == "__main__":
    unittest.main()