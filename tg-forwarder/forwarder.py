import asyncio
from telethon import TelegramClient, events

API_ID    = 28244341
API_HASH  = 'e34576e953e0d0b9810cbbaeaafdd535'
SOURCE_ID = -3487208937   # RICARROH BROADCAST TA
DEST_ID   = 1026720092    # Nasdaq_scanner bot chat

async def main():
    async with TelegramClient('ricarroh_forwarder', API_ID, API_HASH) as client:
        @client.on(events.NewMessage(chats=SOURCE_ID))
        async def handler(event):
            await client.forward_messages(DEST_ID, event.message)
            print(f"✅ Forwarded: {event.message.text[:80] if event.message.text else '[media]'}")

        print("🚀 Forwarder running... Press Ctrl+C to stop")
        await client.run_until_disconnected()

asyncio.run(main())
