from django.shortcuts import render, redirect
from .models import Quest_round1 as qr
from .models import Quest_round2 as qr2
from .models import Team as tm



def index(request):
    return render(request, "index.html")

def display_teams(request):
    return render(request, "teams.html")

def r1_rules(request):
    return render(request, "r1_rules.html")

def r1(request):
    return render(request, "r1.html")


def r2_quest(request):
    teams = list(tm.objects.all().order_by('id'))[:-1]
    quests = list(qr2.objects.all().order_by('qes_id'))
    
    return render(request, "r2_quest.html",{"team":teams[0], "quest":quests[0]})


def r1_quest(request):
    # Sort teams by their ID
    teams = list(tm.objects.all().order_by('id'))[:-1]
    
    quests = qr.objects.all().order_by('qes_id')
    
    ans = False
    count = quests.count()

    if request.method == "GET":
        i = 0  # quest id
        j = 0  # team id
        k = 0
        quest = quests[i]
        team = teams[j]
        bnt = "qes"
        ans = "qes"
        pas_s = False
    
    if request.method == "POST":
        i = int(request.POST.get("counter"))
        j = int(request.POST.get("team_counter"))
        k = int(request.POST.get("pass_counter"))
        pas_s = False

        bnt = request.POST.get("bnt")
        print(request.POST.get("wrong"), request.POST.get("ans"), bnt)

        if request.POST.get("wrong"):
                print("wrong")
                if k!=len(teams):
                    print("j:",j)
                    l = int(request.POST.get("pass_counter"))
                    k = 0 if k == len(teams) - 1 else l + 1
                    bnt = "qes"
                    pas_s = True
                    bnt = "qes"
                    if k == j:
                        k = len(teams)
                        pas_s = False

                else:
                    bnt = "qes"
                    i += 1
                    j = 0 if j >= len(teams) - 1 else j + 1 # Loop through the teams
                    k = j

        elif request.POST.get("ans") and bnt == "qes":
            
            bnt = "ans"

            if request.POST.get("ans") == "y":
                team = list(tm.objects.all().order_by('id'))[k]
                quest = quests[i]
                print("score", team.score, quest.score)
                if k == j:
                    team.score += quest.score
                    team.save()
                else:
                    team.score += quest.pass_score
                    team.save()
                print(request.POST.get("ans"))
                ans = True
            

            elif request.POST.get("ans") == "p":
                
                if k!=len(teams):
                    print("j:",j)
                    l = int(request.POST.get("pass_counter"))
                    k = 0 if k == len(teams) - 1 else l + 1
                    bnt = "qes"
                    pas_s = True
                    if k == j:
                        k = len(teams)
                        pas_s = False

                else:
                    bnt = "qes"
                    i += 1
                    j = 0 if j >= len(teams) - 1 else j + 1 # Loop through the teams
                    k = j

        else:
            j = 0 if j == len(teams) - 1 else j + 1  # Loop through the teams
            k = j
            i += 1
            bnt = "qes"

       
        if i < count:
            quest = quests[i]
            if pas_s:
                team = teams[k]
            elif k == len(teams):
                print(k)
                team = list(tm.objects.all().order_by('id'))[len(teams)]
            else:
                team = teams[k]
        else:
            return redirect("/graph1")

    return render(request, 'r1_quest.html', {
        "quest": quest,
        "teams": list(tm.objects.all().order_by('score'))[::-1],
        "team": team, 
        "bnt": bnt, 
        "team_counter": j,
        "pass_counter": k,
        "counter": i, 
        "d_counter": i + 1, 
        "ans": ans, 
        "pas_s": pas_s,
        "count": count,
    })

def ws(request):
    return render(request, "ws.html")

def round_ws(request):
    return render(request, "round_cs.html")

def graph1(request):
    # Fetch all team objects from the database
    teams = tm.objects.all().order_by('id')

    # Prepare the team names and scores
    categories = [team.team_name for team in teams]
    frequencies = [team.score for team in teams]

    # Render the template and pass the data
    return render(request, "graph1.html", {
        "categories": categories,
        "frequencies": frequencies,
        "teams": teams
    })


def r2(request):
    return render(request, "r2.html")


