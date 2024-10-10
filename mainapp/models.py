from django.db import models

class Tea_m(models.Model):
    t_id = models.IntegerField(default=0)
    team_name = models.CharField(default = "",max_length=250)
    score = models.IntegerField(default=0)
    spec = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.team_name} {self.score}"

class Dugout(models.Model):
    teams = models.ForeignKey(Tea_m, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.teams}"

class Rounds(models.Model):
    round_name = models.CharField(default = "", max_length=250)
    rules = models.JSONField(default=list)
    round = models.CharField(default="", max_length=250)
    timer = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.round_name}"


class Quest_round1(models.Model):
    qes_id = models.IntegerField(default=0)
    quest = models.CharField(max_length=250)
    score = models.IntegerField(default=10)
    pass_score = models.IntegerField(default=5)
    ans = models.CharField(max_length=250, default="")

    def __str__(self):
        return f"{self.quest}"

class Quest_round2(models.Model):
    qes_id = models.IntegerField(default = 0)
    quest = models.CharField(max_length=255)
    ans = models.IntegerField(default=1)
    option1 = models.CharField(default = "",max_length=100)
    option2 = models.CharField(default = "",max_length=100)
    option3 = models.CharField(default = "",max_length=100)
    option4 = models.CharField(default= "",max_length=100)
    score = models.IntegerField(default=10)
    deduct =  models.IntegerField(default=10)   

    def __str__(self):
        return self.quest

class Quest_round3(models.Model):
    qes_id = models.IntegerField(default = 0)
    quest = models.CharField(max_length=255)
    ans = models.IntegerField(default=1)
    option1 = models.CharField(default = "",max_length=100)
    option2 = models.CharField(default = "",max_length=100)
    option3 = models.CharField(default = "",max_length=100)
    option4 = models.CharField(default= "",max_length=100)
    score = models.IntegerField(default=50)
    deduct =  models.IntegerField(default=20)   

    def __str__(self):
        return self.quest

class Quest_round4(models.Model):
    qes_id = models.IntegerField(default = 0)
    quest = models.CharField(max_length=255)
    ans = models.CharField(default = "",max_length=100)
    score = models.IntegerField(default=50)
    deduct =  models.IntegerField(default=20)   

    def __str__(self):
        return self.quest


    
