#!/usr/bin/python3
"""Tests for the base model"""

from models.base_model import BaseModel
from datetime import datetime
import time
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests for the base model class"""

    def test_objects(self):
        self.t1 = BaseModel()
        self.assertIsInstance(self.t1, BaseModel)

    def test_to_dict(self):
        """To test the to_dict method"""
        model1 = BaseModel()
        self.assertIsInstance(model1.to_dict(), dict)

    def test_to_save(self):
        """To test the save method"""
        model = BaseModel()
        prev_updated_at = model.updated_at
        time.sleep(2)
        model.save()
        # Check if the updated_at attr is now greater than the previous one
        self.assertGreater(model.updated_at, prev_updated_at)


if __name__ == "__main__":
    unittest.main()
