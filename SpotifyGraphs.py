import matplotlib.pyplot as plt
import SpotifyData

df0 = SpotifyData.df0
songDateDict = {}

currentRow = 0

while currentRow < len(df0):
    if str((df0.loc[currentRow, 'endTime'][0:7])) in songDateDict:
        songDateDict[str((df0.loc[currentRow, 'endTime'][0:7]))] += 1
    else:
        songDateDict[str((df0.loc[currentRow, 'endTime'][0:7]))] = 1
    currentRow += 1

songDateDictKey = []
for i in songDateDict.keys():
    songDateDictKey.append(i[2:7])