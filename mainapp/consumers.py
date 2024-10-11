import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Quest_round3 as qr3
from .models import Tea_m as tm

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
            # print(text_data_json['counter'])
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
                'counter':text_data_json['counter'],

            }
        )
        else:
            print(text_data_json)
            message = text_data_json['message']
            team = text_data_json['team']
            time = text_data_json['time']
            option = text_data_json['option']
            cnt = text_data_json['cnt']
            qes = qr3.objects.filter(qes_id = int(cnt)).first()
            score = 0
            print(team)
            if option != qes.ans:
                score = qes.deduct * -1
                print("Done!!!!")
            else:
                score = qes.score
                print("Done!!!!")
            
            play = False
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'message':message,
                    'team':team,
                    'score':score,
                    'time':time,
                    'play':play,
                    
                }
            )
            # print(message, team, time)

    def chat_message(self, event):
        
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
            'counter':event['counter'],

            "here25324522":"sfg",
            
        }))
        else:
            message = event['message']
            team = event['team']
            time = event['time']
            score = event['score']
            self.send(text_data=json.dumps({
                'type':'chat',
                'message':message,
                'team':team,
                'time':time,
                'score':score,
                "here22":"sfg",
                'play':False,
                
            }))

