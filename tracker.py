from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

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
    ranges = ['PR Sheet!B3:P4', 'PR Sheet!B7:P8', 'PR Sheet!B11:P12', 'PR Sheet!B15:P16']
    values = service.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID,ranges=ranges,majorDimension='ROWS',valueRenderOption='UNFORMATTED_VALUE',dateTimeRenderOption='FORMATTED_STRING').execute()

    if not values:
        print('No data found.')
    else:
        for i in range(0, 4):
            for x, y in zip(values['valueRanges'][i]['values'][0], values['valueRanges'][i]['values'][1]):
                if x != 0 and x != '':
                    print(x, y)


if __name__ == '__main__':
    main()
