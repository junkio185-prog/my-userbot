from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID", "30392887"))
API_HASH = os.environ.get("API_HASH", "f8a147e34aa2fca7ea146ea3e6f00717")

app = Client("my_userbot", api_id=API_ID, api_hash=API_HASH)

target_users = {}

@app.on_message(filters.command("ngo", prefixes="") & filters.reply & filters.me)
async def set_target(client, message):
    chat_id = message.chat.id
    target_user = message.reply_to_message.from_user
    if not target_user:
        return
    if chat_id not in target_users:
        target_users[chat_id] = set()
    target_users[chat_id].add(target_user.id)
    try:
        await message.reply("🛡️ Target သတ်မှတ်ပြီးပါပြီ။ ချက်ချင်းဖျက်မည်။")
    except:
        pass

@app.on_message(filters.command("unngo", prefixes="") & filters.reply & filters.me)
async def remove_target(client, message):
    chat_id = message.chat.id
    target_user = message.reply_to_message.from_user
    if not target_user:
        return
    if chat_id in target_users and target_user.id in target_users[chat_id]:
        target_users[chat_id].remove(target_user.id)
        try:
            await message.reply("✅ Target စာရင်းမှ ဖယ်ရှားလိုက်ပါပြီ။")
        except:
            pass

@app.on_message(filters.command("clearngo", prefixes="") & filters.me)
async def clear_all_targets(client, message):
    chat_id = message.chat.id
    if chat_id in target_users and target_users[chat_id]:
        target_users[chat_id].clear()
        try:
            await message.reply("🧹 Target အားလုံး ရှင်းလင်းပြီးပါပြီ။")
        except:
            pass

@app.on_message(~filters.me & filters.incoming, group=1)
async def delete_target_messages(client, message):
    try:
        chat_id = message.chat.id
        if chat_id in target_users and message.from_user:
            if message.from_user.id in target_users[chat_id]:
                await message.delete()
    except:
        pass

if __name__ == "__main__":
    print("Userbot is running 24/7 on Web Cloud...")
    app.run()
  
