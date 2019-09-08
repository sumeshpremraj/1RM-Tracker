# 1RM+ tracker
This is a simple tracker that takes your AMRAP (As Many Reps As Possible) set numbers from Google Sheets as input and 
generates graphs showing progress of your 1RM over time. 

I wrote this for personal use, so it is very restrictive about the Sheets format, type of lifts etc. But customization 
options are in the works (see TO DO below).

#### Why spreadsheets and not an app?
For some weird reason, everyone seems to have defaulted to mobile apps even for use cases where something else like a 
website or a spreadsheet makes sense. My reasons for using spreadsheets are simple:
* No dependence on an app (many of which are abandoned in time)
* Easy to read, update and use
* Can be plugged into scripts and tools like this
* Can be printed out if you prefer to keep your phone away at gym but want to check the routine

#### Screenshots
![1RM+ sample graphs](screenshots/screenshot-1.png?raw=true)

#### Requirements
* Python 3
* requests, matplotlib and its dependencies (will be installed during the virtual env setup)
* [Sheets API key](https://developers.google.com/sheets/api/quickstart/python)

#### Usage
Enter your stats in the 531 spreadsheet (either the default from Reddit or my customized one which includes date)

Then, run the following commands:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ ./tracker.py
```

The script will trigger a Google Oauth flow to access your documents.

#### TO DO
- [ ] Process Google Drive folder of spreadsheets
- [ ] Accept local Excel files as data source
- [ ] Package Python as an executable (py2exe and py2app)