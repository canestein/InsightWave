# test_insightwave.py
"""
Tests for InsightWave module.
"""

import unittest
from insightwave import InsightWave

class TestInsightWave(unittest.TestCase):
    """Test cases for InsightWave class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InsightWave()
        self.assertIsInstance(instance, InsightWave)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InsightWave()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
