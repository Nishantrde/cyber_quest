import os
import json
import django

# Set the settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyber_quest.settings')

# Setup Django
django.setup()

from mainapp.models import Tea_m, Dugout, Rounds, Quest_round1, Quest_round2, Quest_round3, Quest_round4

# Define the input JSON file
input_file = 'quiz_data.json'

# Load the data from the JSON file
with open(input_file, 'r') as file:
    data = json.load(file)

# Function to load data into the database
def load_data_to_db():
    # Load Tea_m data
    for tea_m_data in data['Tea_m']:
        team, created = Tea_m.objects.update_or_create(
            t_id=tea_m_data['t_id'],
            defaults={
                'team_name': tea_m_data['team_name'],
                'score': tea_m_data['score'],
                'spec': tea_m_data['spec'],
                'dug_out': tea_m_data['dug_out']
            }
        )
        print(f"Team {team.team_name} {'created' if created else 'updated'}")

    
    # Load Rounds data
    for round_data in data['Rounds']:
        round_, created = Rounds.objects.update_or_create(
            round_name=round_data['round_name'],
            defaults={
                'rules': round_data['rules'],
                'round': round_data['round'],
                'timer': round_data['timer']
            }
        )
        print(f"Round {round_.round_name} {'created' if created else 'updated'}")

    # Load Quest_round1 data
    for quest_data in data['Quest_round1']:
        quest, created = Quest_round1.objects.update_or_create(
            qes_id=quest_data['qes_id'],
            defaults={
                'quest': quest_data['quest'],
                'score': quest_data['score'],
                'pass_score': quest_data['pass_score'],
                'ans': quest_data['ans']
            }
        )
        print(f"Quest_round1 {quest.quest} {'created' if created else 'updated'}")

    # Load Quest_round2 data
    for quest_data in data['Quest_round2']:
        quest, created = Quest_round2.objects.update_or_create(
            qes_id=quest_data['qes_id'],
            defaults={
                'quest': quest_data['quest'],
                'ans': quest_data['ans'],
                'option1': quest_data['option1'],
                'option2': quest_data['option2'],
                'option3': quest_data['option3'],
                'option4': quest_data['option4'],
                'score': quest_data['score'],
                'deduct': quest_data['deduct']
            }
        )
        print(f"Quest_round2 {quest.quest} {'created' if created else 'updated'}")

    # Load Quest_round3 data
    for quest_data in data['Quest_round3']:
        quest, created = Quest_round3.objects.update_or_create(
            qes_id=quest_data['qes_id'],
            defaults={
                'quest': quest_data['quest'],
                'ans': quest_data['ans'],
                'option1': quest_data['option1'],
                'option2': quest_data['option2'],
                'option3': quest_data['option3'],
                'option4': quest_data['option4'],
                'score': quest_data['score'],
                'deduct': quest_data['deduct']
            }
        )
        print(f"Quest_round3 {quest.quest} {'created' if created else 'updated'}")

    # Load Quest_round4 data
    for quest_data in data['Quest_round4']:
        quest, created = Quest_round4.objects.update_or_create(
            qes_id=quest_data['qes_id'],
            defaults={
                'quest': quest_data['quest'],
                'ans': quest_data['ans'],
                'media_url': quest_data['media_url'],
                'score': quest_data['score'],
                'deduct': quest_data['deduct']
            }
        )
        print(f"Quest_round4 {quest.quest} {'created' if created else 'updated'}")


# Call the function to load data
load_data_to_db()

print(f'Successfully loaded data into the database from {input_file}')
