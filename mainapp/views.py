from django.shortcuts import render, redirect
from .models import Quest_round1 as qr
from .models import Quest_round2 as qr2
from .models import Quest_round3 as qr3
from .models import Rounds as rd
from .models import Tea_m as tm
from .models import Dugout as dg

def index(request):
    return render(request, "index.html")

def display_teams(request):
    return render(request, "teams.html")

def disclaimer(request):
    rounds = rd.objects.filter(round="disclaimer").first()
    print(type(rounds.rules))
    return render(request, "disclaimer.html", {"rounds": rounds.rules})

def r1(request):
    rounds = rd.objects.filter(round="round1").first()
    print(type(rounds.rules))
    return render(request, "r1.html", {"rounds": rounds.rules})

def r2(request):
    rounds = rd.objects.filter(round="round2").first()
    print(type(rounds.rules))
    return render(request, "r2.html", {"rounds": rounds.rules})

def r3_elemator(request):
    elemeted_team = list(tm.objects.filter(spec=False).order_by('score'))[::-1][-1]
    if not dg.objects.filter(teams = elemeted_team).exists():
        obj = dg.objects.create(teams = elemeted_team)
        obj.save()
    print(elemeted_team)
    return render(request, "r3_ele.html", {"team":elemeted_team})

def r3(request):
    rounds = rd.objects.filter(round="round3").first()
    print(type(rounds.rules))
    return render(request, "r3.html", {"rounds": rounds.rules})

def r3_quest_lrbd(request, id):
    quest = qr3.objects.filter(qes_id = id).first()
    teams = list(tm.objects.filter(spec=False).order_by('score'))[::-1]
    return render(request, "r3_quest_lrbd.html", {"teams":teams,"quest":quest, "count":id+1, "counter":id})

def r3_quest(request, team):
    tea_m = tm.objects.filter(t_id = team).first()
    teams = list(tm.objects.filter(spec=False).order_by('score'))[::-1]
    return render(request, "r3_quest.html", {"teams":teams, "team":tea_m})

def r2_quest(request, id, team_id):
    
    quests = list(qr2.objects.all().order_by('qes_id'))
    check = ""
    crr = ""
    ans = ""  # Initialize ans
    
    if request.method == "GET":
        crr = "qes"

    if request.method == "POST":
        crr = request.POST.get("crr")
        inp = int(request.POST.get("answer")) if request.POST.get("answer") else 0
        
        # Toggle crr and update the question id
        crr = "ans" if crr == "qes" else "qes" 
        # Check if the selected answer is correct
        check = 1 if quests[id].ans == inp else 0

        # Determine the correct option (match quests[id].ans with the options)
        correct_answer = quests[id].ans
        if crr == "qes":
            team_id = team_id+1 if team_id<5 else 0
            id = id + 1 if crr == "qes" else id
        else:
            print(crr)
            
        if correct_answer == 1 and crr == "ans":
            ans = quests[id].option1
            if check == 1:
                
                team = tm.objects.get(t_id=team_id+1)  # Fetch the team
                team.score += quests[id].score
                team.save()
                print("score", team.score, team)
            else:
                team = tm.objects.get(t_id=team_id+1)  # Fetch the team
                team.score -= quests[id].deduct
                team.save()
                print("score", team.score, team)
                

        elif correct_answer == 2 and crr == "ans":
            ans = quests[id].option2
            if check == 1:
                
                team = tm.objects.get(t_id=team_id+1)  # Fetch the team
                team.score += quests[id].score
                team.save()
                print("score", team.score, team)
            else:
                team = tm.objects.get(t_id=team_id+1)  # Fetch the team
                team.score -= quests[id].deduct
                team.save()
                print("score", team.score, team)
                

        elif correct_answer == 3 and crr == "ans":
            ans = quests[id].option3
            if check == 1:
                
                team = tm.objects.get(t_id=team_id+1)  # Fetch the team
                team.score += quests[id].score
                team.save()
                print("score", team.score, team)
            else:
                team = tm.objects.get(t_id=team_id+1)  # Fetch the team
                team.score -= quests[id].deduct
                team.save()
                print("score", team.score, team)
                

        elif correct_answer == 4 and crr == "ans":
            ans = quests[id].option4
            if check == 1:
                
                team = tm.objects.get(t_id=team_id+1)  # Fetch the team
                team.score += quests[id].score
                team.save()
                print("score", team.score, team)
            else:
                team = tm.objects.get(t_id=team_id+1)  # Fetch the team
                team.score -= quests[id].deduct
                team.save()
                print("score", team.score, team)
                
        
        print(inp)
        if id>11:
            return redirect("/graph/r3_ele")
        print(quests[id].ans)
    print(team_id)
    return render(request, 'r2_quest.html', {
        "count": id,
        "quest": quests[id],
        "teams": list(tm.objects.filter(spec=False).order_by('score'))[::-1],
        "crr": crr,
        "team":tm.objects.get(t_id=team_id+1),
        "team_id":team_id,
        "check": check,
        "ans": ans,  # Pass the correct answer option to the template
        "counter": id + 1
    })


def r1_quest(request):
    # Sort teams by their ID
    teams = list(tm.objects.all().order_by('t_id'))[:-1]
    
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
                team = list(tm.objects.all().order_by('t_id'))[k]
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
                team = list(tm.objects.all().order_by('t_id'))[len(teams)]
                
            else:
                team = teams[k]

        else:
            return redirect("/graph/r2")

    return render(request, 'r1_quest.html', {
        "quest": quest,
        "teams": list(tm.objects.filter(spec=False).order_by('score'))[::-1],
        "team": team,
        "bnt": bnt, 
        "team_counter": j,
        "pass_counter": k,
        "counter": i, 
        "d_counter": i + 1, 
        "ans": ans, 
        "pas_s": pas_s,
        "count": count,
        "spec": False if team != "spectators" else True
    })

def ws(request):
    return render(request, "ws.html")

def round_ws(request):
    return render(request, "round_cs.html")

def graph(request, id):
    # Fetch all team objects from the database
    teams = tm.objects.all().order_by('t_id')

    # Prepare the team names and scores
    categories = [team.team_name for team in teams]
    frequencies = [team.score for team in teams]

    # Render the template and pass the data
    return render(request, "graph.html", {
        "categories": categories,
        "frequencies": frequencies,
        "teams": teams,
        "next": id,
    })





