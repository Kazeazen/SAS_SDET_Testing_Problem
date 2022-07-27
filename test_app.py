import unittest
from app import DateTimeValidation

class TestApp(unittest.TestCase):

    def setUp(self):
        self.validator1 = DateTimeValidation()

    def test_load_file_data_nodupes(self):
        # Testing data reading into class with the .txt that does NOT have duplicate datetimes.
        self.validator1.load_file("data/data_nodups.txt")
        self.assertNotEqual(self.validator1.data, [])
        self.assertIsNotNone(self.validator1.data)

    def test_load_file_data_dupes(self):
        # Testing data reading into class with the .txt that DOES have duplicate datetimes
        self.validator1.load_file("data/data_dupes.txt")
        self.assertNotEqual(self.validator1.data, [])
        self.assertIsNotNone(self.validator1.data)
    
    def test_load_file_no_file(self):
        self.validator1.load_file("")
        self.assertEqual(0, len(self.validator1.data))
    
    def test_unique_or_not_with_data_nodups_txt(self):
        # Since the data_nodups.txt file has unique data, as well as the properly formatted data, any tests with no_dups.txt should NOT fail.
        self.validator1.load_file("data/data_nodups.txt")
        self.assertEqual(self.validator1.unique_or_not(self.validator1.data), True)
        self.assertTrue(self.validator1.unique_or_not(self.validator1.data), True)
        self.assertIsNot(self.validator1.unique_or_not(self.validator1.data), False)

    def test_unique_or_not_with_data_dupes_txt(self):
        self.validator1.load_file("data/data_dupes.txt")
        self.assertFalse(self.validator1.unique_or_not(self.validator1.data), True)
        self.assertEqual(self.validator1.unique_or_not(self.validator1.data), False)

    def test_in_iso8601_format(self):
        self.validator1.load_file("data/data_nodups.txt")
        for datetime_string in self.validator1.data:
            self.assertTrue(self.validator1.in_iso8601_format(datetime_string))
            self.assertNotEqual(self.validator1.in_iso8601_format(datetime_string), False)
    
    def test_in_iso8601_format_dupes(self):
        self.validator1.load_file("data/data_dupes.txt")
        for datetime_string in self.validator1.data:
            self.assertTrue(self.validator1.in_iso8601_format(datetime_string))
    
    def test_in_iso_8601_format_empty_string(self):
        self.assertEqual(self.validator1.in_iso8601_format(""), False)


if __name__ == '__main__':
    unittest.main()