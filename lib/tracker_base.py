#!/usr/bin/env python
from __future__ import print_function

import logging
import matplotlib.pyplot as plt

from collections import OrderedDict
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('tracker.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Example data structure
# stats =
#         {
#             'Squat': {
#                 112.0: '8/10/2018',
#                 124.66666666666667: '15/10/2018',
#                 120.0: '12/10/2018'
#             },
#             'Bench': {
#                 80.16666666666667: '15/10/2018',
#                 78.0: '8/10/2018',
#                 82.0: '12/10/2018'
#             },
#             'Deadlift': {
#                 113.33333333333333: '12/10/2018',
#                 105.0: '10/10/2018'
#             },
#             'Press': {
#                 57.0: '10/10/2018',
#                 66.66666666666666: '12/10/2018'
#             }
#         }

class TrackerBase(object):
    def auth(self):
        logger.info("Initiating Sheets authorization")
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))
        return service


    def get_data(self, spreadsheet_id='1mp0x8AV7cTM45BqHzQ5uO-ga9JN48OA-yfNedcsnRkQ',
                 ranges=['PR Sheet!A2:P4', 'PR Sheet!A6:P8', 'PR Sheet!A10:P12', 'PR Sheet!A14:P16']):
        service = self.auth()

        logger.info("Getting data from Sheets")
        values = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges=ranges,
                                                          majorDimension='ROWS', valueRenderOption='UNFORMATTED_VALUE',
                                                          dateTimeRenderOption='FORMATTED_STRING').execute()
        return values


    def plot_data(self, values):
        stats = {}
        plt.xlabel("Date")
        plt.ylabel("1RM")

        for i in range(0, 4):
            lift = ''
            for rep, weight, date in zip(values['valueRanges'][i]['values'][0], values['valueRanges'][i]['values'][1],
                                         values['valueRanges'][i]['values'][2]):
                if weight == 'Rep max':
                    # First column contains Squat/Rep Max/Date as the data
                    # This is to get the name of the lift
                    lift = rep
                    logger.debug("Lift: " + lift)
                    stats[lift] = {}
                    continue

                elif weight not in (0, ''):
                    if not all([rep, weight, date]):
                        logger.info("Missing data in the column, check spreadsheet")
                        continue

                    # Epley formula
                    rep_max = weight * (1 + rep / 30)
                    logger.debug(date + " " + str(rep_max))

                    # TODO: Convert string to Python date objects OR check Sheets API for Date type
                    stats[lift][date] = rep_max

            logger.info("Plotting " + lift)
            x = OrderedDict(sorted(stats[lift].items(), key=lambda t: t[0]))
            logger.debug(x)
            plt.title(lift)
            plt.plot(x.keys(), x.values())  # (x-axis: date, y-axis: 1RM)
            plt.show()

        logger.debug("Stats: ")
        logger.debug(stats)