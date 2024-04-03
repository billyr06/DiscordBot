import os
import discord
import requests
import csv
from io import StringIO

# Initialize the Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Function to fetch data from the public spreadsheet
def fetch_spreadsheet_data(spreadsheet_id, gid='0'):
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={gid}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data, status code: {response.status_code}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        # Extract the gun name from the command
        gun_name = message.content[1:].strip().lower()

        try:
            # Fetch the data from the spreadsheet as CSV
            csv_data = fetch_spreadsheet_data('10uE2AoXbZpy6C9sdRdJ8GzQGPYNzg-xrNrEoM6V1-jE')

            # Convert the CSV data into a list of rows
            f = StringIO(csv_data)
            reader = csv.reader(f, delimiter=',')
            data = list(reader)

            # Start capturing the attachments after we find the gun name
            capture = False
            # Dictionary to hold the attachments
            attachments_dict = {}

            # Iterate over each row
            for row in data:
                if capture:
                    # If we find an empty row or a row with empty first cell, stop capturing
                    if not row or not row[0].strip():
                        break
                    # Add the attachment details to the dictionary
                    category, attachment_name = row[0].strip(), row[1].strip()
                    attachments_dict[category] = attachment_name
                elif gun_name in row[0].strip().lower():
                    # We found the row with the gun name, so we start capturing the next rows
                    capture = True

            # If we found the attachments, format and send them as a message
            if attachments_dict:
                # Format the attachments into a string with code block formatting
                attachments_list = [f"{category}: {attachments_dict[category]}" for category in attachments_dict]
                response = '\n'.join(attachments_list)
                # Send the message wrapped in triple backticks for a code block
                await message.channel.send(f"Attachments for {gun_name.upper()}:\n```{response}```")
            else:
                await message.channel.send(f'Sorry, I could not find the {gun_name.upper()} weapon in the data.')


        except Exception as e:
            await message.channel.send(f'An error occurred: {e}')

try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    client.run(token)
except discord.HTTPException as e:
  if e.status == 429:
    print("The Discord servers denied the connection for making too many requests.")
    print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests.")
  else:
    raise e
