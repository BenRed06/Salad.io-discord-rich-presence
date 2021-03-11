from pypresence import Presence
import time

client_id = "819380421040144394"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()

#print(RPC.update(state="referal code:", details="currently Chopping"))  # Set the presence
print(RPC.update(buttons=[{"label": "Get Salad!", "url": "https://www.salad.io"}])) # Can specify up to 2 buttons

RPC.update(details="🔪 Currently Chopping", state="😀 Referal code: 5H9AJ2",  large_image='1024', small_image='discord.png', large_text='SALAD.IO', small_text='text here', start=time.time())

while 1:
    time.sleep(15) #Can only update presence every 15 seconds
    
