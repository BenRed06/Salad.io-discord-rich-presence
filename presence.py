from pypresence import Presence
import time

client_id = 'your client ID'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print(RPC.update(state="use code: 5H9AJ2 for 2X rewards! ", details="the gamers crypto miner!"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
