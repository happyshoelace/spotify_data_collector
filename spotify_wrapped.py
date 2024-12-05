import pandas as pd
import time
from collections import Counter
from urltool import convert_google_sheet_url
from datetime import datetime
import time


def date_to_unix_timestamp_millis(day=None, month=None, year=None):
    # Get the current date
    now = datetime.now()
    
    # Use current day, month, and year if not provided
    day = day if day is not None else now.day
    month = month if month is not None else now.month
    year = year if year is not None else now.year
    
    # Create a datetime object with the provided or current date
    date = datetime(year, month, day)
    
    # Convert the datetime object to a Unix timestamp in milliseconds
    unix_timestamp_millis = int(time.mktime(date.timetuple()) * 1000)
    
    return unix_timestamp_millis


pandas_url = convert_google_sheet_url()[0]

df = pd.read_csv(pandas_url)

counts = Counter(df.Artist)
intdates = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12]]
unixdates = [date_to_unix_timestamp_millis(dates[0], dates[1]) for dates in intdates]
unixdates.append(date_to_unix_timestamp_millis(1,1,2025))

strMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print("\n")


for x, month in enumerate(strMonths):
    print(f"{month.upper()} SONG NUMBER: {len(df[df.Date.between(unixdates[x], unixdates[x+1])])} (ROUGHLY {3*len(df[df.Date.between(unixdates[x], unixdates[x+1])]) / 60} HOURS)")


print("\n")

counts_1 = Counter(df.Artist[df.Date.between(unixdates[0], unixdates[-1])])
counts_2 = Counter(df.Track[df.Date.between(unixdates[0], unixdates[-1])])



most_popular_artist = dict()
most_popular_song = dict()

print(f"I LISTENED TO {len(counts_1.items())} DIFFERENT ARTISTS IN 2024\n")

print(f"I LISTENED TO {len(df[df.Date.between(unixdates[0], unixdates[-1])])} SONGS IN 2024 (ROUGHLY {3*len(df[df.Date.between(unixdates[0], unixdates[-1])])} MINUTES OR {3*len(df[df.Date.between(unixdates[0], unixdates[-1])])/ 60} HOURS OR {round(3*len(df[df.Date.between(unixdates[0], unixdates[-1])]) / 60 / 60,2)} DAYS) \n")

print(f"I LISTENED TO {len(counts_2.items())} DIFFERENT SONGS IN 2024\n")

print("_________________________________________________________\n")

for key, value in counts_1.items():
    if value >= 10: # Looks at how many artists you've listened to more than ten times
        most_popular_artist[key] = value

for key, value in counts_2.items():
    if value >= 15: # Looks at how many songs you've listened to more than fifteen times
        most_popular_song[key] = value


most_popular_artist = (dict(sorted(most_popular_artist.items(), key=lambda x:x[1], reverse = True)))
most_popular_song = (dict(sorted(most_popular_song.items(), key=lambda x:x[1], reverse = True)))

keys_list_artist = list(most_popular_artist.keys())
values_list_artist = list(most_popular_artist.values())

#print(f"ARTISTS WITH MORE THAN 10 PLAYS IN {current_month}:\n")

print("MY TOP TEN ARTISTS ON SPOTIFY OF 2024")

for i in range(0, 10): #range(len(keys_list_artist)): # Provides your top ten artists, if you want all artists more >= 10, change range to commented
    print(values_list_artist[i], keys_list_artist[i])

keys_list_song = list(most_popular_song.keys())
values_list_song = list(most_popular_song.values())

print("_________________________________________________________\n")

#print(f"SONGS WITH MORE THAN 5 PLAYS IN {current_month}:\n")
print("MY TOP TEN SONGS ON SPOTIFY OF 2024")

for i in range(0, 10): #range(len(keys_list_song)): # Provides top ten songs, if you want all songs >= 15, change range to commented
    print(values_list_song[i], keys_list_song[i])

for key, value in counts_1.items():
    if value == 1: # Counts artists you've only played one time
        most_popular_artist[key] = value

for key, value in counts_2.items():
    if value == 1: # Counts number of songs only played one time
        most_popular_song[key] = value


most_popular_artist = (dict(sorted(most_popular_artist.items(), key=lambda x:x[1], reverse = True)))
most_popular_song = (dict(sorted(most_popular_song.items(), key=lambda x:x[1], reverse = True)))

keys_list_artist = list(most_popular_artist.keys())
values_list_artist = list(most_popular_artist.values())

keys_list_song = list(most_popular_song.keys())
values_list_song = list(most_popular_song.values())


print("\n")
print("_________________________________________________________\n")
print("\n")
print(f"I LISTENED TO {len(keys_list_artist)} ARTISTS ONLY ONE TIME IN 2024")
print("\n")
print(f"I LISTENED TO {len(keys_list_song)} SONGS ONLY ONE TIME IN 2024")
print("\n")


artist_counts = Counter(df.Artist[df.Date.between(unixdates[0], unixdates[-1])])
count_taylor_swift = artist_counts["Taylor Swift"] # Can change "Taylor Swift" to any artist
print(f"TAYLOR SWIFT COUNT: {count_taylor_swift}")
print("\n")
