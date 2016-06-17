#!/usr/bin/env python2.7
"""
Script for outputting either monthly or daily values for a range of dates
"""

from datetime import date, datetime, timedelta
from calendar import monthrange
import argparse
import sys

class DateRangeException(Exception):
    pass

def delta_days(start, end):
    """
    Function to print out days given a range
    start and end arguments are date objects
    """
    while start <= end:
        sys.stdout.write(start.strftime('%Y%m%d') + '\n')
        start += timedelta(days=1)

def delta_months(start, end):
    """
    Function to print out months given a range
    start and end arguments are date objects
    """
    while start <= end:
        sys.stdout.write(start.strftime('%Y%m') + '\n')
        start += timedelta(days=monthrange(start.year, start.month)[1])

def parse_day(input_date):
    """
    Read in day string and output date object
    input_date is a string date 'YYYYMMDD'
    """
    year = int(input_date[:4])
    month = int(input_date[4:6])
    day = int(input_date[6:8])
    return date(year, month, day)

def parse_month(input_date, end_date=False):
    """
    Read in month string and output date object
    input_date is a string date 'YYYYMM'
    """
    year = int(input_date[:4])
    month = int(input_date[4:6])
    day = 1
    if end_date:
        day = monthrange(year, month)[1]
    return date(year, month, day)

def check_date_string(date_string):
    """
    Helper function to validate proper date format
    """
    try:
        if len(date_string) == 6:
            datetime.strptime(date_string, '%Y%m')
        else:
            datetime.strptime(date_string, '%Y%m%d')
    except:
        raise DateRangeException("Date format error. Expected date format: YYYYMM or YYYYMMDD")

def error_check(start_date, end_date):
    """
    Check for input errors
    """
    if len(start_date) != len(end_date) and (len(start_date) != 6 or len(start_date) != 8):
        raise DateRangeException("Start and end date must have the same format (YYYYMM or YYYYMMDD)")

    check_date_string(start_date)
    check_date_string(end_date)

def output_dates(start_date, end_date):
    """
    Output either days or months
    """
    if len(start_date) == 8:
        start_date = parse_day(start_date)
        end_date = parse_day(end_date)
        delta_days(start_date, end_date)
    else:
        start_date = parse_month(start_date, end_date=False)
        end_date = parse_month(end_date, end_date=True)
        delta_months(start_date, end_date)

def main():
    parser = argparse.ArgumentParser("Usage: %prog YYYYMM YYYYMM or %prog YYYYMMDD YYYYMMDD")
    parser.description="Output a range of dates given start and end dates."
    parser.add_argument("start_date", help="Start date")
    parser.add_argument("end_date", help="End date")
    args = parser.parse_args()

    # Check for formatting errors and output data
    error_check(args.start_date, args.end_date)
    output_dates(args.start_date, args.end_date)

if __name__ == '__main__':
    main()

