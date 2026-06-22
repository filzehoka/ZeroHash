# test_zerohash.py
"""
Tests for ZeroHash module.
"""

import unittest
from zerohash import ZeroHash

class TestZeroHash(unittest.TestCase):
    """Test cases for ZeroHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZeroHash()
        self.assertIsInstance(instance, ZeroHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZeroHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
