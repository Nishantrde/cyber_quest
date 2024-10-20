import os
import json
import django

# Set the settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyber_quest.settings')

# Setup Django
django.setup()

from mainapp.models import Tea_m, Dugout, Rounds, Quest_round1, Quest_round2, Quest_round3, Quest_round4

# Dictionary to store all models data
all_data = {}

# Fetch data from each model
all_data['Tea_m'] = list(Tea_m.objects.all().values())
all_data['Dugout'] = list(Dugout.objects.all().values())
all_data['Rounds'] = list(Rounds.objects.all().values())
all_data['Quest_round1'] = list(Quest_round1.objects.all().values())
all_data['Quest_round2'] = list(Quest_round2.objects.all().values())
all_data['Quest_round3'] = list(Quest_round3.objects.all().values())
all_data['Quest_round4'] = list(Quest_round4.objects.all().values())

# Define the output JSON file
output_file = 'quiz_data.json'

# Write the data to a JSON file with readable formatting
with open(output_file, 'w') as file:
    json.dump(all_data, file, indent=4)  # indent=4 ensures readability

print(f'Successfully exported all model data to {output_file}')
