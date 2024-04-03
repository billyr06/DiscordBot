# MetaBot for Call of Duty: Warzone

## Description
MetaBot is a Discord bot designed for Call of Duty: Warzone players, providing streamlined access to the best gun attachments based on recommendations from Teepee, a well-known Warzone streamer. This bot queries Teepee's public Google Docs spreadsheet for the latest attachment setups, ensuring players have the most effective loadouts. By simply typing `!` followed by the gun name, players receive Teepee's recommended attachments for their specified weapon.

## Features
- **Real-time Attachment Recommendations:** Users can easily fetch Teepee's recommended gun attachments by entering `!` followed by the gun name (e.g., `!ram7`). MetaBot responds with a curated list of attachments, sourced directly from Teepee's up-to-date spreadsheet.

## Installation Instructions
To deploy MetaBot in your Discord server, please follow these instructions:

1. **Clone the Repository:** Download this project to your local environment or use a cloud-based IDE such as Replit.
2. **Python Installation:** Ensure Python is installed on your system. This bot was developed with Python 3.8.
3. **Dependency Installation:** Run `pip install discord requests` to install the necessary libraries.
4. **Discord Bot Setup:** Generate a new bot token in the [Discord Developer Portal](https://discord.com/developers/applications) and note it down.
5. **Token Security:** Safely store your Discord bot token in an environment variable named `TOKEN`.
6. **Start the Bot:** Execute `python bot.py` in your terminal to initiate MetaBot.

## Usage
Engage with MetaBot on any Discord server it's part of by typing `!` followed by the gun name. For example:

![User command](screenshots/Screenshot%20from%202024-04-03%2017-19-53.png)

MetaBot will reply with Teepee's recommended attachments for the MTZ-556, structured as follows:

![User command](screenshots/Screenshot%20from%202024-04-03%2017-20-08.png)




