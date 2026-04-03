import asyncio
import base64
import os

from telethon import TelegramClient, events

API_ID    = 28244341
API_HASH  = 'e34576e953e0d0b9810cbbaeaafdd535'
SOURCE_ID = -3487208937
DEST_ID   = 1026720092

SESSION_B64 = os.environ.get('SESSION_B64', '')
if SESSION_B64:
        with open('ricarroh_forwarder.session', 'wb') as f:
                    f.write(base64.b64decode(SESSION_B64))
                print("Session file written")

async def main():
        async with TelegramClient('ricarroh_forwarder', API_ID, API_HASH) as client:
                    @client.on(events.NewMessage(chats=SOURCE_ID))
                    async def handler(event):
                                    await client.forward_messages(DEST_ID, event.message)
                                    print("Forwarded message")

                    print("Forwarder running...")
                    await client.run_until_disconnected()

asyncio.run(main())
