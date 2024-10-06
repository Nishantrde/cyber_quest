import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyber_quest.settings')
import django
django.setup()
from mainapp.models import Tea_m as tm


team_names = [
    "Hex Hackers",
    "Interface Innovators",
    "Ping Prophets",
    "Kernel Kings",
    "Exception Executors",
    "Script Shifters"
]

for i in range(len(team_names)):
    print(i)
    ob = tm.objects.create(
        t_id = i,
        team_name = team_names[i]
        )
    ob.save()
ob = tm.objects.create(
        t_id = 6,
        team_name = "spec",
        spec = True
        )
ob.save()
# Now you can access the data
# print(data["Rounds"])
