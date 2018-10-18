# 1RM+ tracker
This is a simple tracker that takes your AMRAP (As Many Reps As Possible) set numbers from Google Sheets as input and 
generates graphs showing progress of your 1RM over time. 

I wrote this for personal use, so it is very restrictive about the Sheets format, type of lifts etc. If there is 
interest, I plan to package this into a Python module, enable different input sources (like Excel sheets on your local 
storage), different programs etc.

#### Why spreadsheets and not an app?
For some weird reason, everyone seems to have defaulted to mobile apps even for use cases where something else like a 
website or a spreadsheet makes sense. My reasons for using spreadsheets are simple:
* No dependence on an app (many of which are abandoned in time)
* Easy to read, update and use
* Can be plugged into scripts and tools like this
* Can be printed out if you prefer to keep your phone away at gym but want to check the routine

#### Requirements
* Python 3
* requests, matplotlib and its dependencies
* [Sheets API key](https://developers.google.com/sheets/api/quickstart/python)

#### Usage
```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ ./tracker.py
```

#### (Maybe) TO DO
* Make a pip module
* Accept local Excel files as data source
* Customizable location (sheet/row/column) for the required data
* Customizable 1RM formula (Epley, Brzycki, McGlothin)
* Make dates for AMRAP optional, for compatibility with standard Reddit template
