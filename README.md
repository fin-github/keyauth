# Key Authentication Discord Interaction Bot
A key auth bot with discord interactions like: Modals, Slash Commands, and Buttons.

# Modification
This will help you get the bot ready for use.
1. Put all of your keys in the validkeys.txt file. It should be formatted like this: KEY;ANOTHERKEY;LASTKEY;
2. Add all staff IDS in the devs list at the top of the main.py script. The line should look like this:
   
`devs = [devIDhere,anotherdevIDhere,andanotheronehere]`

3. Put your bot token in the bot.start at the very last line. Like this:

`bot.start(TOKENHERE)`

# Installation
1. Install all of the files in the Bot directory, into the same directory.
2. Do all of the steps in the Modification Section.


# Usage
1. Start the bot by running `main.py` in the cmd (THE CMD MUST BE IN THE DIRECTORY OF ALL YOUR OTHER FILES).
2. In the server you want the bot to work in, run /role_calibration (role),  inside the (role) you should put the role you want people to get when they successfully authenticate.
3. Run /load.
4. Test it.
5. Done

# Logging
Logs will be saved of every users action, open the logs.txt file to read the logs.


# Examples
![example](https://raw.githubusercontent.com/fin-github/keyauth/main/Screenshot%202023-11-22%20175427.png)
