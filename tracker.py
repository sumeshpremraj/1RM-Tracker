#!/usr/bin/env python
from __future__ import print_function

import logging
from lib.tracker_base import TrackerBase

# If modifying these scopes, delete the file token.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('tracker.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():
    tracker = TrackerBase()
    values = tracker.get_data()
    if not values:
        logger.info('No data found.')
    else:
        tracker.plot_data(values)


if __name__ == '__main__':
    logger.info("Starting 1RM Tracker")
    main()
