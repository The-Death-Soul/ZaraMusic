from ZZ.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)







@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)
        
        
#start



@Client.on_callback_query(filters.regex("cb_start"))
async def cb_start(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""ʜᴇʟʟᴏ [✨](https://te.legra.ph/file/d3185c725b9ba69b3f339.jpg) **ᴡᴇʟᴄᴏᴍᴇ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
 **ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄᴀʟʟ !!**
 **ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ 💫**
 **ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴊᴏɪɴ @Death_Soul_Federation 💐**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💠Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ Gʀᴏᴜᴘ💠",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(
                    "• Cᴏᴍᴍᴀɴᴅs", callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton("• Oᴡɴᴇʀ", url=f"https://t.me/zara_THE_addiction"),
                    InlineKeyboardButton("• Dᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/zara_THE_addiction"),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/+TFNht-Xwon1lM2Y1"
                    ),
                    InlineKeyboardButton(
                        "• Uᴘᴅᴀᴛᴇs", url=f"https://t.me/ZaraSupport"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "• CHAT GROUP •", url="https://t.me/+TFNht-Xwon1lM2Y1"
                    )
                ],
            ]
        ),
    )

    
    
    
    #Help command
    
    
@Client.on_callback_query(filters.regex("cb_cmd"))
async def cb_cmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello !**
» **ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴄʟɪᴄᴋ ʙᴜᴛᴛᴏɴs 🔭 !**
⚡ Developed by [ℤ𝔸ℝ𝔸](https://t.me/zara_THE_addiction)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("sᴏᴍᴇ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅ", callback_data="cb_basic"),
                    InlineKeyboardButton("sᴏᴍᴇ ᴀᴅᴠᴀɴᴄᴇ ᴄᴏᴍᴍᴀɴᴅs", callback_data="cb_advance"),
                ],
                [InlineKeyboardButton("sᴏᴍᴇ sᴘᴇᴄɪᴀʟ ᴄᴏᴍᴍᴀɴᴅ", callback_data="cb_fun")],
               
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cb_start")],
            ]
        ),
    )
    
@Client.on_callback_query(filters.regex("cb_basic"))
async def cb_basic(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""𝙎𝙞𝙢𝙥𝙡𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 
        
        
•  `/play (song name)` 
•  `/vplay (song name)` 
•  `/vstream (song name)` 
•  `/skip` - skip the current song
•  `/end` - stop music play
•  `/pause` - pause song play
•  `/resume` - resume song play
•  `/mute` - mute assistant in vc
•  `/lyrics (song name)`

⚡ Developed By [ℤ𝔸ℝ𝔸](https://t.me/zara_THE_addiction) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_advance"))
async def cb_advance(_, query: CallbackQuery):
    await query.edit_message_text(    
      f"""𝙀𝙭𝙩𝙧𝙖 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨
• `/ping` pong !!
• `/start` - Alive msg ~group 
• `/id` - Find out your grp and your id // stickers id also
• `/uptime` - 💻
• `/rmd` clean all downloads
• `/clean` - clear storage 

⚡ Developed By [ℤ𝔸ℝ𝔸(https://t.me/zara_THE_addiction) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_fun"))
async def cb_fun(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""𝙎𝙥𝙚𝙘𝙞𝙖𝙡 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨
• `/truth` 🌝
• `/dare`  🌝
• `/wish`    🌝
• `/zain`   🌝
• `/zara` 🌝   

⚡ Developed By [ℤ𝔸ℝ𝔸](https://t.me/zara_THE_addiction) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cb_cmd")]]
        ),
    )
        

    
    
    
        


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ɴɪᴋᴀʟ ʙᴇ ᴛᴜ ᴀᴅᴍɪɴ ɴᴀʜɪ ʜᴀɪ ɢʀᴏᴜᴘ ᴋᴀ !", show_alert=True)
    await query.message.delete()
