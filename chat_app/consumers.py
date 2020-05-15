from channels import Channel,Group

def websocket_connect(message):
	message.channel_session['rooms'] = []

def websocket_disconnect(message):
	

def websocket_receive(message):
	Channel('receive').send(<<message>>)



def join_chat(message):
	


def leave_chat(message):
	send_chat()

def send_chat(message):
	group = Group("room-" +str(message["room_id"]))