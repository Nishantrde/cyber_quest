from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=250)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team_name}"

class Quest_round1(models.Model):
    qes_id = models.IntegerField(default=0)
    quest = models.CharField(max_length=250)
    score = models.IntegerField(default=10)
    pass_score = models.IntegerField(default=5)
    ans = models.CharField(max_length=250, default="")

    
    def __str__(self):
        return f"{self.quest}"
