
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N9960392
#    Student name: Liam Hulsman-Benson
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function6
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path-naming conventions used on this
# computer.  Apply this function to the full name of your
# HTML document so that your program will work on any
# operating system.
from os.path import normpath
    
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date and time function.
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.


################ PUT YOUR SOLUTION HERE #################

# Html for the top of the document e.g. title of source to archivist name
html_top = """<!DOCTYPE html>
<html>
  <head>
    <title>***Date***</title>
  </head>
  <body style="background-color:#EEF313;">
      <center>
          <h1>ABC Sports NEWS Archive</h1>
             <p></p>
             <h2>***Date***</h2>
             <img border="2" src = https://vignette.wikia.nocookie.net/logopedia/images/9/9a/AbcSports.jpg/revision/latest?cb=20140306150555 alt = 'ABC Sports Logo'  height = "200" width = "600">
             <p style="font-size:20px">NEWS source:<a href="http://www.abc.net.au/news/feed/45924/rss.xml">http://www.abc.net.au/news/feed/45924/rss.xml</p></a>
             <p style="font-size:20px">Archivist: Liam Hulsman-Benson</p>
"""          

# Html for each story, a new template is added for each story in the list
html_template = """<!DOCTYPE html>

     <center><a href="***Link***"><h2>***Story_num*** ***TITLE***</h2></a></center>
      <table style = "border-bottom: 1px solid black">
          <tr>
              <th width = 5%  style="font-size:12px"><img border="2" src = ***Image*** alt = '***Alt_Image***'  height = "400" width = "600"></th>
              <th ><p style="font-size:20px">***Paragraph***</p></th>
          </tr>
          <tr>
              <th width = 8%></th>
              <th width = 8% ><p style="font-size:12px">Written: ***TIME***</p></th>
      </table>
  </body>

</html>
"""

##### Functions #####
def Event_logger_toggle():
    #Get general path for db
    path = getcwd()
    general_path =normpath(path)
    
    if state.get() == 1:
        #Button in checked state
        state.set(1)
        conn = connect(general_path+'\event_log.db')
        sql =  "INSERT INTO Event_Log(Description) VALUES('Event logging switched on')"
        conn.execute(sql)
        conn.commit()
        conn.close()
    elif state.get() == 0:
        #Button in unchecked state
        state.set(0)
        conn = connect(general_path+'\event_log.db')
        sql =  "INSERT INTO Event_Log(Description) VALUES('Event logging switched off')"
        conn.execute(sql)
        conn.commit()
        conn.close()
        
def view_html():
    # View HTML just created
    path = getcwd()
    general_path =normpath(path)
    webopen(general_path+'\Extracted.html')

    ###Part B###
    #Get general path for db
    path = getcwd()
    general_path =normpath(path)
    if state.get() == 1:
        conn = connect(general_path+'\event_log.db')
        sql =  "INSERT INTO Event_Log(Description) VALUES('Extracted news displayed in web browser')"
        conn.execute(sql)
        conn.commit()
        conn.close()
    
def get_latest():
    #Execute downloader file
    global stories_per_date
    path = getcwd()
    general_path =normpath(path)
    exec(open(general_path+'\downloader.py').read())#Execute downloader file
    saveas = str(datetime.now())
    if saveas[0:10] not in stories_per_date:
        stories_per_date =  stories_per_date + [saveas[0:10]]
        last =  len(stories_per_date)
        days.insert(END,stories_per_date[last-1])
        
    ###Part B###
    path = getcwd()
    general_path =normpath(path)
    if state.get() == 1:
        conn = connect(general_path+'\event_log.db')
        sql =  "INSERT INTO Event_Log(Description) VALUES('The latest news downloaded and archived')"
        conn.execute(sql)
        conn.commit()
        conn.close()

def generate_html(titles,paragraphs,dates,images,links):
        #Replace the blanks in the HTML template
        html_code = html_top+html_template
        Story_num = 1
        for All in range(len(titles)):
            html_code = html_code.replace('***TITLE***', titles[All])
            html_code = html_code.replace('***Story_num***',str(Story_num)+"." )
            html_code = html_code.replace('***Date***', dates[0][0:16])
            html_code = html_code.replace('***Paragraph***', paragraphs[All])
            html_code = html_code.replace('***TIME***', dates[All])
            html_code = html_code.replace('***Image***', images[All][0])
            html_code = html_code.replace('***Alt_Image***',"Image: " + images[All][0][33:56] + " could not be reached")
            html_code = html_code.replace('***Link***', links[All])
            if All != len(titles)-1:
                html_code = html_code + html_template
            Story_num = Story_num + 1
            
        # Write the HTML code to a file
        html_file = open("Extracted" + '.html', 'w')
        html_file.write(html_code)
        html_file.close()

def extract_method(): #Extract th required data from the archived html file
    #Make display extracted button clickable
    display['state'] = 'normal'
    
    # Find date that was selected in the GUI
    selected = days.curselection()
    date = days.get(selected)

    ##### Seperate each story #####
        
    html = open('InternetArchive/'+date+'.html', 'r', encoding = 'UTF-8')
    linenum = 1
    story_start_pos = []
    story_end_pos = []

    for line in html:
        if line.find('<item>') != -1:
            story_start_pos = story_start_pos + [linenum]
        elif line.find('</item>') != -1:
            story_end_pos = story_end_pos + [linenum]
        linenum = linenum + 1

    linenum = 1
    story = ''
    stories = []

    for All in range(len(story_start_pos)):
        linenum = 1
        story = ''
        html = open('InternetArchive/'+date+'.html', 'r', encoding = 'UTF-8')  # FInd a better way of doing this instead of repetedly openonmg html file
        for line in html:
            if story_start_pos[All] <= linenum <= story_end_pos[All]:
                story = story + line
            linenum = linenum + 1
        stories = stories + [story]

    ##### Title  #####
    titles = []
    title_regex = '<title>.*\</title>'

    for All in range(len(stories)):
        title = findall(title_regex, stories[All])
        title = title[0][7:len(title)-9] # Start at 7 as <title> is 7 long, similar for the -9
        titles = titles + [title]

    ##### Image  #####
    images = []
    image_regex = 'http.*627.jpg'
    image_regex2 = 'http.*627.png'

    for All in range(len(stories)):
        image = findall(image_regex, stories[All])
        if image == []:
            image = findall(image_regex2, stories[All])
        if image == []:
            image = ['No Image assosiated with story']
        images = images + [image]     

    ##### Paragraphs  #####
    paragraphs = []
    paragraph_regex = '<p>.*</p>'

    for All in range(len(stories)):
        paragraph = findall(paragraph_regex, stories[All])
        paragraph = paragraph[0][3:len(paragraph)-5]
        paragraphs = paragraphs + [paragraph]

    ##### Date  #####
    dates = []
    date_regex = '<pubDate>.*?</pubDate>'

    for All in range(len(stories)):
        date = findall(date_regex, stories[All])
        date = date[0][9:len(date)-11]
        dates = dates + [date]
        
    ##### Link  #####
    links = []
    link_regex = '<link>.*<'

    for All in range(len(stories)):
        link = findall(link_regex, stories[All])
        link = link[0][6:len(link)-2]
        links = links + [link]

    ##### Print to Html doc #####   
    generate_html(titles[0:10],paragraphs[0:10],dates[0:10],images[0:10],links[0:10])

    #Show an extracted date on the GUI
    Extracted_date.set("The date extracted is: "+dates[0][0:16])

    ###Part B###
    path = getcwd()
    general_path =normpath(path)
    if state.get() == 1:
        conn = connect(general_path+'\event_log.db')
        sql =  "INSERT INTO Event_Log(Description) VALUES('NEWS from " +dates[0][5:16]+ " extracted from archive')"
        conn.execute(sql)
        conn.commit()
        conn.close()

##### GUI #####
# Create a window
window = Tk()
# Give the window a title
window.title('ABC Sports NEWS Archive')

Extracted_date = StringVar()
stories_per_date = ['2017-10-18','2017-10-19','2017-10-20','2017-10-21','2017-10-22','2017-10-23','2017-10-24']

#Labels
Title = Label(window,text = "ABC Sports Archive",fg="blue",font=("Helvetica", 20))
Date_extaracted = Label(window,textvariable = Extracted_date,fg="black",font=("Helvetica", 15))

#Buttons
extract = Button(window,text = 'Extract news from highlighted day', command = extract_method,height=2,width=20,fg = "blue",bg="yellow",font=("Helvetica", 16),wraplength=200)
display = Button(window,text = 'Display extracted', command = view_html,height=2,width=20,fg = "blue",bg="yellow",font=("Helvetica", 16),wraplength=200, state=DISABLED) #If file has not been extracted do not allow button to be clicked
get_latest = Button(window,text = 'Get latest', command  = get_latest,height=2,width=20,fg = "blue",bg="yellow",font=("Helvetica", 16),wraplength=200)

#Listbox
days = Listbox(window,height=8,width=20,font=("Helvetica", 15))

#Checkbox
state = IntVar()
Event_logger = Checkbutton(window, text = "Event Logger", command = Event_logger_toggle, variable = state)

#Place widgets in window
Title.grid(row = 0, column = 1, columnspan = 2)
Date_extaracted.grid(row=1, column = 1,columnspan=2)
extract.grid(row = 2, column = 2)
display.grid(row = 3, column = 2)
get_latest.grid(row = 4, column = 2)
days.grid(row = 2, column = 1,rowspan=3)
Event_logger.grid(row = 5, column = 2)

#Populate listbox with dates to select
for All in range(len(stories_per_date)):
    days.insert(END,stories_per_date[All])
    
#Select default option for listbox
days.selection_set( first = END )

#Start mainloop
window.mainloop()








