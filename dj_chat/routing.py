# mysite/routing.py
from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # (your routes here)
})



# from channels import include
# application = [
#     # To set up the websocket routing
#    include("chat_app.routing.routing_websocket", path=r"^/socket/"),
#     # For chat join, leave, and send
#     include("chat_app.routing.routing_chat"),
# ]