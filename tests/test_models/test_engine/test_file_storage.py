#!/usr/bin/python3
"""
Test for storage
"""
import os
import sys
import unittest
from datetime import datetime
from time import sleep
import json
from models.engine.file_storage import FileStorage
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."","".."","".."))
sys.path.append(project_root)


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""
    def test_instances(self):
        """chequeamos instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()
