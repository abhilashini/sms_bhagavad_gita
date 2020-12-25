from twilio.rest import Client
import os
import json


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

# Send SMS with Twilio
def send_sms(message: str) -> None:
	client = Client(account_sid, auth_token)
	msg = client.messages.create(
		to="+919035377491", 
		from_="+14793492290", 
		body=message)

	print(msg.sid) #Verify SMS sent successfully
	
# Fetch current verse number to send
with open("verse_num.dat") as f:
	curr_verse_num = f.read()

# Check if all verses have been read
if int(curr_verse_num) > 640:
	send_sms("You've reached the end of Gita. Good job! 👏")
else:
	# Load all verses of Gita
	with open("bhagavad_gita.json") as f:
		curr_verse = json.load(f)

	# Format message content
	msg_content = f"Bhgavad Gita Verse of the Day\
			\n\n{curr_verse[curr_verse_num]['verse']}\
			\n\"{curr_verse[curr_verse_num]['translation']}\"\
			\n\nRead further about this verse at:\
			\n{curr_verse[curr_verse_num]['commentary_link']}"
	# print(msg_content)
	
	send_sms(msg_content)
	
	# Increment verse number
	curr_verse_num = int(curr_verse_num)+1
	with open("verse_num.dat", "w") as f:
		f.write(f"{curr_verse_num}")
