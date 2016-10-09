# UnlimitMe #
<p align="center"><img src="http://image.prntscr.com/image/04456599e3564fa7853c59ce385d3ea1.png" /</p>


A Telegram utility, which allow you to send messages from a Telegram bot, useful if you are limited.
A simple GUI, and a bunch of lines of code.

# What is this repository for? #

This is a python script that allow you to:

* Send messages in groups even if you are limited.
* Send images in groups even if you are limited.
* Send stickers,documents in groups even if you are limited (Will be added SOON!).

***

# Requirements #

* Python (any version under 3.*) installed on your PC(Linux, OSX,Windows).
* A Telegram Boy (Create one using @BotFather on telegram).
* The Bot Token (Given to you by the @BotFather).
* Brain.

# How do I get set up? #

* Install [Python 2.*](https://www.python.org/download/releases/2.7/) or newer(i use 2.7.11)
* Clone this repository anywhere on your computer.
* Now, move to the directory where you saved the repo.

Running it from Windows:

* Run 'Start.bat'.

Running it from Linux:
Once moved to the directory where you cloned the repo with the terminal type:

* chmod +x Start.sh
* ./Start.sh

or

* python Unlimitme.py

# Finding Chat ID #

Getting the Chat ID of the Group where you want to send messages.

* Go to the chat group where you want the Bot to send messages.
* Add the Telegram BOT to the group or ask someone to do it for you.
* Send a dummy message to the bot (EX: /start@YourBot_bot)
* Copy the Bot Token to clipboard
* Get the list of updates for your Bot by going to https://api.telegram.org/botXXX:YYYY/getUpdates (Replace XXX:YYYY with your Bot token)
* Look for "chat":{"id":-zzzzzzzzzz,      (-zzzzzzzzzz is your chat id (with the negative sign))
* Then you're done, your chat ID is the negative number.
* You can test it using curl curl -X POST "https://api.telegram.org/botXXX:YYYY/sendMessage" -d "chat_id=-zzzzzzzzzz&text=my sample text"


# Using UnlimitMe #

Once you're done with setup, getting token and chat ID just follow those simple steps:

* If you have not started UnlimitMe yet start it by running the Start.bat file
* Now paste the Chat ID on it's textbox [(Screenshot)](http://prntscr.com/crmjwg)
* Paste the bot Token on it's textbot [(Screenshot)] (http://prntscr.com/crmk8k)
* Now click on Save CID(Chat ID) & Token button
* Next time you'll run the bot it will auotmagically load the bot token and the chat id on it's respectives textboxes.
* Now you're ready to rock!


# More #

You can find me on:

* [Holeboards](www.holeboards.eu)
* [Telegram](www.telegram.me/GooogIe)

Useful links:

* A more detailed guide on: [Creating a Telegram BOT](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* [Other useful Tools](http://neonn.ga)
