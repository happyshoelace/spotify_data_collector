# Spotify Data Analysis
Collects your Spotify listening data and then also analyses it! (Because who wants to use an external tool when you can do it yourself!)
<br>
<br>

## Python Set Up
1. Make sure you have [Python](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) installed
2. Install all the dependencies using `pip install -r requirements.txt`

## Setting It Up
1. Follow [the first three steps](https://developers.google.com/sheets/api/quickstart/python) to create a Google Sheets API project. (So enabling API, configuring OAuth and authorising credentials). **Make sure you put credentials.json in the directory with this code!!**
2. On that same dashboard, navigate to data access (You might need to click OAuth Consent Screen and then go to new experience to see this option). Click Add or Remove Scopes, then in the filter type in "Google Sheets API" and enable the scope called ".../auth/spreadsheets". Click save.
3. Then go to the [Spotify Developer page](https://developer.spotify.com/) and create an app. The name and description can be whatever you want. Set the redirect URI to http://localhost:8080 and agree to the terms.
4. Click on your app, then click settings. From there copy the Client ID and Client Secret into the clientsecret.py file.
5. Create a new spreadsheet, or use an existing one. Starting at A1 of Sheet1, Write the headings Artist, Album, Track, Date. **Case Sensitive!** Put the link of the spreadsheet in the browser into the clientsecret.py file too.
6. The spreadsheet also needs to be public, so make sure you set that in the share settings.
7. When you run the code for the first time, you will be prompted to allow your apps access to your account. This means it's worked!

## Compatible with Data from LastFM!
If you already have a history of scrobbles from LastFM, this program is compatible with that. Get a CSV of your data from [lastfm stats](https://lastfmstats.com) (it may take a while to load if you are a first time visitor) and import it into Google Sheets (file>import). This program will append data to the bottom of that list. Make sure you delete the #<username> bit in the Date column before you try to analyse the data

# Note
The collection will only append to the first sheet, but the wrapped portion works for any sheet. 

# Thanks
Repo was forked from [Liz Stippell](https://github.com/liz-stippell), but altered a lot because I didn't want to use IFTTTT and had pre-existing data from LastFM.