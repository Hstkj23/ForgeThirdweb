# test_forgethirdweb.py
"""
Tests for ForgeThirdweb module.
"""

import unittest
from forgethirdweb import ForgeThirdweb

class TestForgeThirdweb(unittest.TestCase):
    """Test cases for ForgeThirdweb class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ForgeThirdweb()
        self.assertIsInstance(instance, ForgeThirdweb)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ForgeThirdweb()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
