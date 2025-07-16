import unittest
from unittest.mock import patch
from arg_parser import ArgParser


class TestArgParser(unittest.TestCase):
    def test_argparser_valid_args(self):
        test_args = [
            'script_name',
            '--latitude', '33.69',
            '--longitude', '72.97',
            '--start', '2025-07-01',
            '--end', '2025-07-05',
            '--task', 'average'
        ]

        with patch('sys.argv', test_args):
            parser = ArgParser()
            args = parser.parse()

            self.assertEqual(args.latitude, 33.69)
            self.assertEqual(args.longitude, 72.97)
            self.assertEqual(args.start, '2025-07-01')
            self.assertEqual(args.end, '2025-07-05')
            self.assertEqual(args.task, 'average')


if __name__ == '__main__':
    unittest.main()
