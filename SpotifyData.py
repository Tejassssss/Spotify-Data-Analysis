import pandas as pd
import numpy as np
import decimal

# pylint: disable=anomalous-backslash-in-string
df0 = pd.read_json("MyData\StreamingHistoryTotal.json")
songDict = {}
artistDict = {}
songTimeDict = {}
artistTimeDict = {}
totalSeconds = 0

currentRow = 0
while currentRow < len(df0):
    currentSong = str(df0.loc[currentRow, "trackName"])
    currentArtist = str(df0.loc[currentRow, "artistName"])
    totalSeconds = totalSeconds + df0.loc[currentRow, "msPlayed"]/1000
    if currentSong in songDict:
        songDict[currentSong] = songDict[currentSong] + 1 
        songTimeDict[currentSong] = songTimeDict[currentSong] + df0.loc[currentRow,"msPlayed"] / 60000
    else:
        songDict[currentSong] = 1
        songTimeDict[currentSong] = df0.loc[currentRow, "msPlayed"] / 60000
    if currentArtist in artistDict:
        artistDict[currentArtist] = artistDict[currentArtist] + 1
        artistTimeDict[currentArtist] = artistTimeDict[currentArtist] + df0.loc[currentRow,"msPlayed"] / 60000
    else:
        artistDict[currentArtist] = 1
        artistTimeDict[currentArtist] = df0.loc[currentRow,"msPlayed"] / 60000
    currentRow += 1

for i in songTimeDict:
    songTimeDict[i] = round(songTimeDict[i])
for i in artistTimeDict:
    artistTimeDict[i] = round(artistTimeDict[i])

sortedSongDict = sorted(songDict.items(), key=lambda songDict: songDict[1])
sortedArtistDict = sorted(artistDict.items(), key=lambda artistDict: artistDict[1])
sortedSongTimeDict = sorted(songTimeDict.items(), key=lambda songTimeDict: songTimeDict[1])
sortedArtistTimeDict = sorted(artistTimeDict.items(), key=lambda artistTimeDict: artistTimeDict[1])

SecondsL = "{:,}".format(int(totalSeconds))
MinutesL = "{:,}".format(int(totalSeconds/60))
HoursL = "{:,}".format(int(totalSeconds/3600))
DaysL = "{:,}".format(int(totalSeconds/(3600*24)))

totalPlays = "{:,}".format(len(df0))

def TopSongs(top):
    counter = 0
    for k in reversed(sortedSongDict):
        if counter < top:
            print(k)
            counter +=1
def TopArtists(top):
    counter = 0
    for k in reversed(sortedArtistDict):
        if counter < top:
            print(k)
            counter +=1
def TopSongTime(top):
    counter = 0
    for k in reversed(sortedSongTimeDict):
        if counter < top:
            # k = "{:.1f}".format(k)
            print(k)
            counter +=1
def TopArtistTime(top):
    counter = 0
    for k in reversed(sortedArtistTimeDict):
        if counter < top:
            print(k)
            counter +=1