import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        print("connected")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['message'] == "kernel":
            play = text_data_json['play']
            
            async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'play':play,
                'quest':text_data_json['quest'],
                'option1':text_data_json['option1'],
                'option2':text_data_json['option2'],
                'option3':text_data_json['option3'],
                'option4':text_data_json['option4'],

                
            }
        )
        else:
            message = text_data_json['message']
            team = text_data_json['team']
            time = text_data_json['time']
            
            play = False
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'message':message,
                    'team':team,
                    'time':time,
                    'play':play,
                    
                }
            )
            print(message, team, time)

    def chat_message(self, event):
        print(event['play'])
        if event['play']:
            play = event['play']
            self.send(text_data=json.dumps({
            'type':'chat',
            'play':play,
            'quest':event['quest'],
            'option1':event['option1'],
            'option2':event['option2'],
            'option3':event['option3'],
            'option4':event['option4'],

            "here25324522":"sfg",
            
        }))
        else:
            message = event['message']
            team = event['team']
            time = event['time']
            
            self.send(text_data=json.dumps({
                'type':'chat',
                'message':message,
                'team':team,
                'time':time,
                "here22":"sfg",
                'play':False,
                
            }))

