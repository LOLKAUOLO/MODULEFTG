from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
import asyncio

def register(cb):
    cb(SpamMod())
class SpamMod(loader.Module):
    """Модуль гачимучи ахазпзазхах"""
    strings = {'name': 'ГачиМучи'}
    
    async def gachicmd(self, message): 
        """Используй: .gachi если ты  факин слэээйв""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>♂️Используй команду</b>" "<code> .cum </code>""<b> чтобы выбрать нужный звук</b>")  
        try: 
            await message.edit("<b>ща всё будет</b>") 
            music = await message.client.inline_query('GachimuchiKBot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>Нету <code>{args}</code> </b>")
  
    async def cumcmd(self, message):
        """."""
        await message.edit("<b> Испозуйте .gachi + любой аргумент:\n AAAAAAAAAAAAA \n Fuck you \n Fucking slave \n Welcome to the club, buddy \n 300$ \n Dungeon Master \n Yes \n Fisting \n Boy nextdoor \n AAAAAAAAAHAH \n My aaass \n Gay party \n BILLYEAH \n Alright man</b>")