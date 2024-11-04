
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer 
from asgiref.sync import async_to_sync 
import json 

from .models import Group, Message

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Connecting to websocket", event)
        print('Channel Layer', self.channel_layer)
        print('Channel Name', self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupName']
        print('Group Name', self.group_name)
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.send({
            'type': 'websocket.accept',
        })
    
    def websocket_receive(self, event):
        print("Received event", event['text'])

        group = Group.objects.get(name=self.group_name)
        chat_data = json.loads(event['text'])
        chat = Message(
            group=group,
            content= chat_data
        )
        chat.save()

        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type': 'chat_message',
            'text': event['text'],
        })

    def chat_message(self,event):
        self.send({
            'type': 'websocket.send',
            'text': event['text'],
        })

    
    def websocket_disconnect(self, event):
        print("Disconnected from websocket with code", event)
        print('Channel Layer', self.channel_layer)
        print('Channel Name', self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        raise StopConsumer()
    