#!/usr/bin/env python
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import matplotlib.pyplot as plt

# If modifying these scopes, delete the file token.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1mp0x8AV7cTM45BqHzQ5uO-ga9JN48OA-yfNedcsnRkQ'
    ranges = ['PR Sheet!A2:P4', 'PR Sheet!A6:P8', 'PR Sheet!A10:P12', 'PR Sheet!A14:P16']
    values = service.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID,ranges=ranges,majorDimension='ROWS',valueRenderOption='UNFORMATTED_VALUE',dateTimeRenderOption='FORMATTED_STRING').execute()

    if not values:
        print('No data found.')
    else:
        plt.xlabel("Date")
        plt.ylabel("1RM")

        for i in range(0, 4):
            for rep, weight, date in zip(values['valueRanges'][i]['values'][0], values['valueRanges'][i]['values'][1],
                                         values['valueRanges'][i]['values'][2]):
                if weight == 'Rep max':
                    # First column contains Squat/Rep Max/Date as the data
                    # This is to print the name of the lift
                    print(rep)
                    continue
                elif weight != 0 and weight != '':
                    if not all([rep, weight, date]):
                        print("Missing data in the column, check spreadsheet")
                        continue
                    # print(rep, weight, date)

                    # Epley formula
                    rep_max = weight * (1 + rep / 30)
                    print(date, rep_max)
                    plt.plot(date, rep_max, 'go-', linewidth=2)
        plt.show()

if __name__ == '__main__':
    main()
