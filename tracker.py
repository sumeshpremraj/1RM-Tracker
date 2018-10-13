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
    ranges = ['PR Sheet!B3:P3', 'PR Sheet!B7:P7', 'PR Sheet!B11:P11', 'PR Sheet!B15:P15']
    values = service.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID,ranges=ranges,majorDimension='ROWS',valueRenderOption='UNFORMATTED_VALUE').execute()

    if not values:
        print('No data found.')
    else:
        print("Squat")
        for v in values['valueRanges'][0]['values'][0]:
            if v != 0 and v != '':
                print(v)

        print("Bench")
        for v in values['valueRanges'][1]['values'][0]:
            if v != 0 and v != '':
                print(v)

        print("Deadlift")
        for v in values['valueRanges'][2]['values'][0]:
            if v != 0 and v != '':
                print(v)

        print("Press")
        for v in values['valueRanges'][3]['values'][0]:
            if v != 0 and v != '':
                print(v)


if __name__ == '__main__':
    main()
