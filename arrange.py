# Import necessary Django modules/settings
import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

# Import the models
from mainapp.models import Team, Rounds, Quest_round1, Quest_round2

def save_data_to_file():
    # Define the file path to save the data
    file_path = 'data_export.txt'

    with open(file_path, 'w') as file:
        # Save Team data
        teams = Team.objects.all()
        file.write("=== Teams Data ===\n")
        for team in teams:
            file.write(f"Team Name: {team.team_name}, Score: {team.score}, Special: {team.spec}\n")
        
        file.write("\n")  # Add a newline for separation
        
        # Save Rounds data
        rounds = Rounds.objects.all()
        file.write("=== Rounds Data ===\n")
        for round in rounds:
            file.write(f"Round Name: {round.round_name}, Rules: {round.rules}, Round: {round.round}\n")
        
        file.write("\n")  # Add a newline for separation

        # Save Quest_round1 data
        quest_round1 = Quest_round1.objects.all()
        file.write("=== Quest Round 1 Data ===\n")
        for quest in quest_round1:
            file.write(f"Question ID: {quest.qes_id}, Question: {quest.quest}, Score: {quest.score}, Pass Score: {quest.pass_score}, Answer: {quest.ans}\n")
        
        file.write("\n")  # Add a newline for separation

        # Save Quest_round2 data
        quest_round2 = Quest_round2.objects.all()
        file.write("=== Quest Round 2 Data ===\n")
        for quest in quest_round2:
            file.write(f"Question ID: {quest.qes_id}, Question: {quest.quest}, Answer: {quest.ans}, "
                       f"Options: [{quest.option1}, {quest.option2}, {quest.option3}, {quest.option4}], "
                       f"Score: {quest.score}, Deduct: {quest.deduct}\n")

    print(f"All data saved to {file_path}")

# Call the function to execute
if __name__ == "__main__":
    save_data_to_file()
