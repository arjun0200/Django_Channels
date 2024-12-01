# Topic - Consumer
from channels.consumer import SyncConsumer, AsyncConsumer

"""
Synchronous: SyncConsumer is synchronous, meaning it processes one request at a time, 
blocking other requests until the current one is completed.
"""


class MySyncConsumer(SyncConsumer):
    # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
    def websocket_connect(self, event):
        print('Websocket Connected...')

    # This handler is called when data received from Client
    def websocket_receive(self, event):
        print('Messaged Received...')

    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.  
    def websocket_disconnect(self, event):
        print('Websocket Disconnected...')

"""
Asynchronous: AsyncConsumer is asynchronous, meaning it can handle multiple connections concurrently without blocking. 
It is capable of performing non-blocking I/O operations, which makes it ideal for scenarios that involve high concurrency or 
long-running tasks like database queries, HTTP requests, etc.
"""

class MyAsyncConsumer(AsyncConsumer): ##handles multiple request
    # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
    async def websocket_connect(self, event):
        print('Websocket Connected...')

    # This handler is called when data received from Client
    async def websocket_receive(self, event):
        print('Messaged Received...')

    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.  
    async def websocket_disconnect(self, event):
        print('Websocket Disconnected...')