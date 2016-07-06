README for date_range
=====================

Small command line utility used to print consecutive days or months given start and end dates in the form of YYYYMM or YYYYMMDD

Usage
-----

.. code-block:: bash

    usage: date_range.py [-h] start_date end_date

    Output a range of dates given start and end dates.

    positional arguments:
      start_date  Start date, YYYYMM or YYYYMMDD
      end_date    End date, YYYYMM or YYYYMMDD

    optional arguments:
      -h, --help  show this help message and exit

Examples
--------

.. code-block:: bash

    # Months
    $ date_range.sh 201310 201401
    201310
    201311
    201312
    201401
    # Days
    $ date_range.sh 20131021 20131102
    20131027
    20131028
    20131029
    20131030
    20131031
    20131101
    20131102

