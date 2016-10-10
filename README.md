# UnlimitMe #
<p align="center"><img src="http://image.prntscr.com/image/41f753fda6a54e25984301d933e146e7.png" /</p>


A Telegram utility, which allow you to send messages from a Telegram bot, useful if you are limited.
A simple GUI, and a bunch of lines of code.

I am still a newbie with Python tkinter and git, i apologize for anything, bad code or something, any help is REALLY appreciated.

# What is this repository for? #

This is a python script that allow you to:

* Send messages (even with markdown *,_ etc...) in groups even if you are limited.
* Send images in groups even if you are limited.
* Send stickers,documents in groups even if you are limited (Will be added SOON!).

***

# Using UnlimitMe from the Compiled Version (.exe) #

Running the tool from the exe

# Requirements #

[How to create a Telegram BOT](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

* Brain
* The bot Token (Given to you by @BotFather) 

# How do I get set up? #

Once you have everything you need follow those steps:

* Go to the chat group where you want the Bot to send messages.
* Add the Telegram BOT you've created to the group or ask someone to do it for you.
* Send a dummy message to the bot (EX: /start@YourBot_bot)
* Now go to the [releases](https://github.com/GooogIe/UnlimitMe/releases) page.
* Download the latest Compiled Version available [(Screenshot)](http://image.prntscr.com/image/d3295f0a408f4aedad4b839a8ae82b33.png)
* Extract it in a folder.
* And run UlimitMe.exe [(Screenshot)](http://image.prntscr.com/image/a289c83bdaee4e59b98117dd902b26e4.png)

# Running UnlimitMe #

Once you're done with setup, getting token and chat ID just follow those simple steps:

* Once opened the tool, paste in the 'Token' textbox the token copied before.
* Click on 'Save CIDs & Token' .
* Click on Reload CIDs.
* Copy the Chat ID that you need to the Chat id Textbox.
* Type the message you want and click on the Send Button
* Done

***

# Using UnlimitMe from the sources #

Running the tool from the sources

# Requirements #

* Python (any version under 3.*) installed on your PC(Linux, OSX,Windows).
* A Telegram Bot (Create one using @BotFather on telegram).
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

If the auto chat ids loader doesn't find the chat id you was looking for you may have to do it manually.

* Go to the chat group where you want the Bot to send messages.
* Add the Telegram BOT you've created to the group or ask someone to do it for you.
* Send a dummy message to the bot (EX: /start@YourBot_bot)
* Copy the Bot Token to clipboard
* Get the list of updates for your Bot by going to https://api.telegram.org/botXXX:YYYY/getUpdates (Replace XXX:YYYY with your Bot token)
* Look for "chat":{"id":-zzzzzzzzzz,      (-zzzzzzzzzz is your chat id (with the negative sign))
* Then you're done, your chat ID is the negative number.
* You can test it using curl curl -X POST "https://api.telegram.org/botXXX:YYYY/sendMessage" -d "chat_id=-zzzzzzzzzz&text=my sample text"

# Running UnlimitMe #

Once you're done with setup, getting token and chat ID just follow those simple steps:

* Once opened paste in the 'Token' textbox the token copied before.
* Click on 'Save CIDs & Token' .
* Click on Reload CIDs.
* Copy the Chat ID that you need to the Chat id Textbox.
* Type the message you want and click on the Send Button
* Done

***
# More #

You can find me on:

* [Holeboards](www.holeboards.eu)
* [Telegram](www.telegram.me/GooogIe)

Useful links:

* Check my Unlimit Brother in C# [here](https://github.com/neon-loled/UnlimiTG)
* A more detailed guide on: [Creating a Telegram BOT](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* [Other useful Tools](http://neonn.ga/tgtools)
