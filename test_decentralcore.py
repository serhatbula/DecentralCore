# test_decentralcore.py
"""
Tests for DecentralCore module.
"""

import unittest
from decentralcore import DecentralCore

class TestDecentralCore(unittest.TestCase):
    """Test cases for DecentralCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentralCore()
        self.assertIsInstance(instance, DecentralCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentralCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
