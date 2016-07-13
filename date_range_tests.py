import mock
import unittest
import tempfile
import sys
import date_range
from datetime import date, datetime

class DateRange(unittest.TestCase):
    def test_delta_days(self):
        start = date(2014, 12, 28)
        end = date(2015, 01, 05)
        expected = '20141228\n20141229\n20141230\n20141231\n20150101\n20150102\n20150103\n20150104\n20150105\n'

        test_outfile = tempfile.NamedTemporaryFile()
        stdout_patch = mock.patch.object(sys, 'stdout', test_outfile)

        stdout_patch.start()
        date_range.delta_days(start, end)
        stdout_patch.stop()

        test_outfile.seek(0)
        actual = test_outfile.read()
        self.assertEqual(actual, expected)

    def test_delta_months(self):
        start = date(2014, 07, 01)
        end = date(2015, 02, 28)
        expected = '201407\n201408\n201409\n201410\n201411\n201412\n201501\n201502\n'

        test_outfile = tempfile.NamedTemporaryFile()
        stdout_patch = mock.patch.object(sys, 'stdout', test_outfile)

        stdout_patch.start()
        date_range.delta_months(start, end)
        stdout_patch.stop()

        test_outfile.seek(0)
        actual = test_outfile.read()
        self.assertEqual(actual, expected)

    def test_parse_date_day(self):
        input_date = '20140714'
        expected = date(2014, 07, 14)
        actual = date_range.parse_day(input_date)
        self.assertEqual(actual, expected)

    @mock.patch('calendar.monthrange')
    def test_parse_month_start(self, mock_monthrange):
        input_date = '201407'
        mock_monthrange.return_value = 31
        expected = date(2014, 07, 01)
        actual = date_range.parse_month(input_date)
        self.assertEqual(actual, expected)

    @mock.patch('calendar.monthrange')
    def test_parse_month_end(self, mock_monthrange):
        input_date = '201407'
        mock_monthrange.return_value = 31
        expected = date(2014, 07, 31)
        actual = date_range.parse_month(input_date, end_date=True)
        self.assertEqual(actual, expected)

    def test_check_date_string_month(self):
        date_string = '201505'
        date_range.check_date_string(date_string)

    def test_check_date_string_day(self):
        date_string = '20150510'
        date_range.check_date_string(date_string)

    def test_check_date_string_fail_format(self):
        date_string = '2015-05-10'
        with self.assertRaises(date_range.DateRangeException):
            date_range.check_date_string(date_string)

    def test_check_date_string_fail_typo(self):
        date_string = '20150510x'
        with self.assertRaises(date_range.DateRangeException):
            date_range.check_date_string(date_string)

    def test_error_check_pass_day(self):
        start_date = '20150501'
        end_date = '20150504'
        date_range.error_check(start_date, end_date)

    def test_error_check_pass_month(self):
        start_date = '201505'
        end_date = '201507'
        date_range.error_check(start_date, end_date)

    def test_error_check_month_day_mix(self):
        start_date = '201505'
        end_date = '20150501'
        with self.assertRaises(date_range.DateRangeException):
            date_range.error_check(start_date, end_date)

    def test_error_check_length(self):
        start_date = '201505001'
        end_date = '201505002'
        with self.assertRaises(date_range.DateRangeException):
            date_range.error_check(start_date, end_date)

if __name__ == '__main__':
    unittest.main()

