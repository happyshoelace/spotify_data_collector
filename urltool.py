import re
from clientsecret import SPREADSHEET_URL

def convert_google_sheet_url():
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'
    
    # Replace function to construct the new URL for CSV export
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'
    
    # Replace using regex
    new_url = re.sub(pattern, replacement, SPREADSHEET_URL)
    
    # Extract the spreadsheet ID and gid
    match = re.match(pattern, SPREADSHEET_URL)
    SPREADSHEET_ID = match.group(1) if match else None
    gid = match.group(3) if match and match.group(3) else None
    
    return new_url, SPREADSHEET_ID, gid