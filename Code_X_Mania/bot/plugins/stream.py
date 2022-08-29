# (c) Jigarvarma2005 || Code-X-Mania || 
#edit at your own risk
import os
import asyncio
from asyncio import TimeoutError
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.utils.database import Database
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.vars import Var
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


MY_PASS = os.environ.get("MY_PASS",None)
pass_dict = {}
pass_db = Database(Var.DATABASE_URL, "jv_passwords")

@StreamBot.on_message((filters.private) & (filters.document | filters.photo) & ~filters.edited, group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER : \n\n NAME : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Joined file stream bot!!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="Sorry bruh, You are banned🤪\n\n  **contact @pyrogrammerschat**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""You have to join my updates channel in order to use me.""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="HTML"
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="An error occurred. Contact @pyrogrammerschat",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    try:
        
        file_size = None
        if m.document:
            file_size = f"{humanbytes(m.document.file_size)}"
        elif m.photo:
            file_size=f"{humanbytes(m.photo.file_size)}"

        file_name = None
        if m.document:
            file_name = f"{m.document.file_name}"
        """
        elif m.photo:
            file_name=f"{m.photo.file_name}"
        """
            
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        
        online_link = Var.URL + 'download/'+ str(log_msg.message_id) 
       
        
        

        msg_text ="""
<u>**LINK GENERATED**</u>

<b>Name :</b> <code>{}</code>
<b>Size:</b> **{}**
<b>Download URL:</b> <code>{}</code>"""

        await log_msg.reply_text(text=f"**Requested by :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**user id :** `{m.from_user.id}`\n**Stream ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True, parse_mode="Markdown", quote=True)
        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML", 
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                                                InlineKeyboardButton('Play 📥', web_app=online_link)
                                               ]]) #Download Link
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode="Markdown")


@StreamBot.on_message((filters.private) & (filters.video | filters.audio) & ~filters.edited, group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) joined!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="Sorry man, You are banned\n  **contact @pyrogrammers",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""Join my updates channel in order to use me.""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="HTML"
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="An error occurred contact @pyrogrammerschat",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    try:
        
        file_size = None
        if m.video:
            file_size = f"{humanbytes(m.video.file_size)}"
        elif m.document:
            file_size = f"{humanbytes(m.document.file_size)}"
        elif m.audio:
            file_size = f"{humanbytes(m.audio.file_size)}"
        elif m.photo:
            file_size=f"{humanbytes(m.photo.file_size)}"

        file_name = None
        if m.video:
            file_name = f"{m.video.file_name}"
        elif m.document:
            file_name = f"{m.document.file_name}"
        elif m.audio:
            file_name = f"{m.audio.file_name}"
        """
        elif m.photo:
            file_name=f"{m.photo.file_name}"
        """
            
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        
        online_link = Var.URL + 'download/'+ str(log_msg.message_id) 
       
        
        

        msg_text ="""
<u>**LINK GENERATED**</u>

<b>Name :</b> <code>{}</code>
<b>Size:</b> **{}**
<b>Download URL:</b> <code>{}</code>"""

        await log_msg.reply_text(text=f"**Requested By :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**User id :** `{m.from_user.id}`\n**Stream  :** {stream_link}", disable_web_page_preview=True, parse_mode="Markdown", quote=True)
        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML", 
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📺 PLAY ONLINE", web_app=stream_link), #Stream Link
                                                InlineKeyboardButton('📥 DOWNLOAD', url=online_link)]]) #Download Link
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Flood wait {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**User id :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode="Markdown")




@StreamBot.on_message(filters.channel & ~filters.group & (filters.video | filters.audio) & ~filters.edited & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    check_pass = await pass_db.get_user_pass(broadcast.chat.id)
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        online_link = Var.URL + 'download/' + str(log_msg.message_id) 
        await log_msg.reply_text(
            text=f"**Channel name:** `{broadcast.chat.title}`\n**channel id:** `{broadcast.chat.id}`\n**Request URL:** {stream_link}",
            quote=True,
            parse_mode="Markdown"
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📺 PLAY ONLINE ", web_app=stream_link),
                     InlineKeyboardButton('📥 DOWNLOAD', url=online_link)] 
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(w.x)}s from {broadcast.chat.title}\n\n**Cʜᴀɴɴᴇʟ ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`", disable_web_page_preview=True, parse_mode="Markdown")
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Chanell{e}**")

@StreamBot.on_message(filters.channel & ~filters.group & (filters.document) & ~filters.edited & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    check_pass = await pass_db.get_user_pass(broadcast.chat.id)
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        online_link = Var.URL + 'download/' + str(log_msg.message_id) 
        await log_msg.reply_text(
            text=f"**Channel name:** `{broadcast.chat.title}`\n**Channel id:** `{broadcast.chat.id}`\n**Request URL:** {stream_link}",
            quote=True,
            parse_mode="Markdown"
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                     InlineKeyboardButton('DOWNLOAD 📥', url=online_link)
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(w.x)}s from {broadcast.chat.title}\n\n**Cʜᴀɴɴᴇʟ ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`", disable_web_page_preview=True, parse_mode="Markdown")
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Chanell{e}**")
