import SpotifyData
import SpotifyGraphs
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

# Create the window
root = tk.Tk()
root.title('Spotify Data')

# Place the window in the center of the screen
windowWidth = 1000
windowHeight = 550
notebookHeight = windowHeight-50
notebookWidth = 335
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call('source', 'azure-dark.tcl')

# Set the theme with the theme_use method
style.theme_use('azure-dark')

# Creating lists
option_list = ['', 'OptionMenu', 'Value 1', 'Value 2']
combo_list = ['Combobox', 'Editable item 1', 'Editable item 2']
readonlycombo_list = ['Readonly combobox', 'Item 1', 'Item 2']
# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.place(x=windowWidth-20, y=windowHeight-20)

# Notebook
notebook = ttk.Notebook(root)
notebookTab1 = ttk.Frame(notebook, width=notebookWidth, height=notebookHeight)
notebook.add(notebookTab1, text='Top Songs')
notebookTab2 = ttk.Frame(notebook, width=notebookWidth, height=notebookHeight)
notebook.add(notebookTab2, text='Top Artists')
notebookTab3 = ttk.Frame(notebook, width=notebookWidth, height=notebookHeight)
notebook.add(notebookTab3, text='Song Minutes')
notebookTab4 = ttk.Frame(notebook, width=notebookWidth, height=notebookHeight)
notebook.add(notebookTab4, text='Artist Minutes')
notebookTab5 = ttk.Frame(notebook, width=notebookWidth, height=notebookHeight)
notebook.add(notebookTab5, text='Time Listened')
notebook.place(relx=0.01, rely=0.045)
# notebook.place(x=420, y=20)

# Scrollbar
note1Scroll = ttk.Scrollbar(notebookTab1)
note1Scroll.pack(side='right', fill='y')
note2Scroll = ttk.Scrollbar(notebookTab2)
note2Scroll.pack(side='right', fill='y')
note3Scroll = ttk.Scrollbar(notebookTab3)
note3Scroll.pack(side='right', fill='y')
note4Scroll = ttk.Scrollbar(notebookTab4)
note4Scroll.pack(side='right', fill='y')
note5Scroll = ttk.Scrollbar(notebookTab5)
note5Scroll.pack(side='right', fill='y')

topSongText = tk.Text(notebookTab1, yscrollcommand = note1Scroll.set)
for x in reversed(SpotifyData.sortedSongDict):
    topSongText.insert(tk.END, str(x) + '\n')
topSongText.pack()
note1Scroll.config(command=topSongText.yview)

topArtistText = tk.Text(notebookTab2, yscrollcommand = note2Scroll.set)
for x in reversed(SpotifyData.sortedArtistDict):
    topArtistText.insert(tk.END, str(x) + '\n')
topArtistText.pack()
note2Scroll.config(command=topArtistText.yview)

topSongTimeText = tk.Text(notebookTab3, yscrollcommand = note3Scroll.set)
for x in reversed(SpotifyData.sortedSongTimeDict):
    topSongTimeText.insert(tk.END, str(x) + '\n')
topSongTimeText.pack()
note3Scroll.config(command=topSongTimeText.yview)

topArtistTimeText = tk.Text(notebookTab4, yscrollcommand = note4Scroll.set)
for x in reversed(SpotifyData.sortedArtistTimeDict):
    topArtistTimeText.insert(tk.END, str(x) + '\n')
topArtistTimeText.pack()
note4Scroll.config(command=topArtistTimeText.yview)

timeText = tk.Text(notebookTab5, yscrollcommand = note5Scroll.set)
timeText.insert(tk.END, SpotifyData.SecondsL + ' Seconds' + '\n')
timeText.insert(tk.END, '\n' + SpotifyData.MinutesL + ' Minutes' + '\n')
timeText.insert(tk.END, '\n' + SpotifyData.HoursL + ' Hours' + '\n')
timeText.insert(tk.END, '\n' + SpotifyData.DaysL + ' Days' + '\n')
timeText.insert(tk.END, '\n' + SpotifyData.totalPlays + ' Plays ' + '\n')
timeText.pack()
note5Scroll.config(command=timeText.yview)
topSongText.config(state='disabled')
topArtistText.config(state='disabled')
timeText.config(state='disabled')

# The Search Area
def search_switch_function():
    if whatSearch.get():
        searchSwitch.config(text='Artist')
    else:
        searchSwitch.config(text='Song')

def search_button_function():
    if whatSearch.get() == 0:
        if searchEntry.get() in SpotifyData.songDict:
            searchLabel.config(text= str(SpotifyData.songDict[searchEntry.get()]) + " Plays   |   " + str(SpotifyData.songTimeDict[searchEntry.get()]) + " Minutes")
        else:
            searchLabel.config(text='Invalid Search')
    else:
        if searchEntry.get() in SpotifyData.artistDict:
            searchLabel.config(text= str(SpotifyData.artistDict[searchEntry.get()]) + " Plays   |   " + str(SpotifyData.artistTimeDict[searchEntry.get()]) + " Minutes")
        else:
            searchLabel.config(text='Invalid Search')

searchFrame = ttk.LabelFrame(root, text='Search', width=420, height=150)
searchFrame.place(relx=0.75,rely=0.07,anchor='n')

searchEntry = ttk.Entry(searchFrame, text = 'Search Here', width = 30)
searchEntry.place(relx=0.5,rely=0.1,anchor='n')

searchButton = ttk.Button(searchFrame, text='Search', style='AccentButton', command=search_button_function)
searchButton.place(relx=0.7,rely=0.4,anchor='n')

whatSearch = tk.IntVar()
searchSwitch = ttk.Checkbutton(searchFrame,text='Artist', style='Switch', variable=whatSearch, offvalue=0, onvalue=1, command=search_switch_function)
searchSwitch.place(relx=0.3, rely=0.45,anchor='n')
searchSwitch.invoke()

searchLabel = tk.Label(searchFrame, text='Search Result')
searchLabel.place(relx=0.5,rely=0.7,relwidth = 0.7, anchor='n')      

graphFrame = ttk.LabelFrame(root, text='Listens per Month',width=550,height=410)
graphFrame.place(relx=0.95,rely=0.37,anchor='ne')

fig = Figure(figsize = (4, 3), dpi = 100)
timePlot = fig.add_subplot(111)
timePlot.barh(range(len(SpotifyGraphs.songDateDict)), list(SpotifyGraphs.songDateDict.values()), align='center',tick_label = SpotifyGraphs.songDateDictKey,color='blue')
graphCanvas = FigureCanvasTkAgg(fig, master = graphFrame)
graphCanvas.draw()
graphCanvas.get_tk_widget().pack()

root.mainloop()
