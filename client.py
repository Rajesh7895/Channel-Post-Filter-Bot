from info import *
from pyrogram import Client
from subprocess import Popen

User = Client(name="user", session_string=SESSION)
DlBot = Client(name="auto-delete", 
               api_id=29810598,
               api_hash=4f6367a57aeebcf48b58c179684c8250,           
               bot_token=6366997633:AAFLAavo_iu7ieEXGYS17w9iDGuzKSYjk2A)

class Bot(Client):   
    def __init__(self):
        super().__init__(   
           "bot",
            api_id=29810598,
            api_hash=4f6367a57aeebcf48b58c179684c8250,           
            bot_token=6366997633:AAFLAavo_iu7ieEXGYS17w9iDGuzKSYjk2A,
            plugins={"root": "plugins"})
    async def start(self):                        
        await super().start()        
        await User.start()
        Popen("python3 -m utils.delete", shell=True)       
        print("Bot Started 👍🙂")   
    async def stop(self, *args):
        await super().stop()
