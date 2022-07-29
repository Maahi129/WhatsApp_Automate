import pywhatkit

# This is useful , if you wanna send wishes to your friend at midnight.

pywhatkit.start_server()

pywhatkit.sendwhatmsg("+911234676153", "Hello", 14 , 45) # ("number you wanna send", "text", hrs, min)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("Group Name", "Image Path", "Caption (Text)")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+910123456789", "Image Path")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("Search (Ex:- Funny Videos)")