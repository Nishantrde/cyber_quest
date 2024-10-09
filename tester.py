import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyber_quest.settings')
import django
django.setup()
from mainapp.models import *
with open('data_backup.json', 'r') as file:
    data = json.load(file)

dat = data["Quest_round3"]

# for i in dat:
#     print(i)
#     obj = Rounds.objects.create(
#         round_name = i["round_name"],
#         rules = i["rules"],
#         round = i["round"],
#         timer = i["timer"]
#         )
# for i in dat:
#     print(i)
#     obj = Quest_round3.objects.create(
#         qes_id = i["qes_id"],
#         quest = i["quest"],
#         ans = i["ans"],
#         option1 = i["option1"],
#         option2 = i["option2"],
#         option3 = i["option3"],
#         option4 = i["option4"],
#         )

# Now you can access the data
# print(data["Rounds"])
