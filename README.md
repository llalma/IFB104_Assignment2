# IFB104_Assignment2
1st year software engineering course using python

####Task 1

Your “News Archivist” application will be a Python program with a Graphical User Interface.
Under the user’s control, it extracts individual elements from web documents stored in an “archive” (a folder of previously downloaded HTML/XML documents) and uses these elements
to construct an entirely new HTML document which summarises a particular days’ top stories
in a form which can be viewed in a standard web browser. It also allows the user to download
the current version of the source web page and store it in the archive as the “latest” news.

####Task 2

In this extension you will create your own “event logging” capability which records information about the way your program is used. This information is to be stored in a relational
database, for later perusal using a tool such as the DB Browser for SQLite. Your solution must
have the following features:
• Some form of interactive widget, or collection of widgets, must be added to your program’s GUI to allow the user to control whether or not events should be logged, and to
see whether or not event logging is currently enabled.
• As long as this function is activated by the user, your program must save a record of all
user interactions with the GUI in a supplied SQLite database, event_log.db. A
copy of this database accompanies these instructions. It contains a single table,
Event_Log, which has two columns, Event_Number and Description. Your
program must insert descriptions of the GUI events initiated by the user into this table
for as long as the event logging feature is switched on. You should assume the database
table exists but is empty when your program is started.
