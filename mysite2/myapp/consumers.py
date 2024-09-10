import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
from typing import Dict

class ChatConsumer(AsyncWebsocketConsumer):
    # Class-level dictionary to store connections by user ID
    connections: Dict[str, 'ChatConsumer'] = {}

    async def connect(self) -> None:
        """Handles a new WebSocket connection."""
        # Extract user_id from the query string
        query_params = parse_qs(self.scope['query_string'].decode())
        user_id = query_params.get('user_id', [None])[0]

        if user_id:
            # Add this connection to the connections dictionary
            ChatConsumer.connections[user_id] = self
            await self.accept()
        else:
            # Reject the connection if user_id is not provided
            await self.close()
        print(ChatConsumer.connections)

    async def disconnect(self, close_code: int) -> None:
        """Handles WebSocket disconnection."""
        query_params = parse_qs(self.scope['query_string'].decode())
        user_id = query_params.get('user_id', [None])[0]

        if user_id in ChatConsumer.connections:
            del ChatConsumer.connections[user_id]
        print(ChatConsumer.connections)

    async def receive(self, text_data: str) -> None:
        """Receives a message and sends it to a specific user."""
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        target_user_id = text_data_json.get('target_user_id')  # The user to send the message to

        # Check if the target user is connected
        if target_user_id in ChatConsumer.connections:
            target_consumer = ChatConsumer.connections[target_user_id]
            # Send the message to the target user
            await target_consumer.send(text_data=json.dumps({
                'message': message
            }))
        else:
            # Optionally handle the case where the user is not connected
            await self.send(text_data=json.dumps({
                'error': 'Target user not connected'
            }))
        
        print(ChatConsumer.connections)
