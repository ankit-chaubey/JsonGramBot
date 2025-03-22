import json
from telethon import TelegramClient, events

API_ID = 01234
API_HASH = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
BOT_TOKEN = "0123456789:ABCDEFGHIJKLMNOPRSTUVWXYZ"

client = TelegramClient('json_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage)
@client.on(events.MessageEdited(incoming=True))
async def handle_message(event):
    message_json = json.dumps(event.message.to_dict(), default=str, indent=4)
    await event.respond(f"```\n{message_json}\n```")

client.run_until_disconnected()
