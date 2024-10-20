from django.shortcuts import render, redirect, HttpResponse
import json
from .models import Quest_round1 as qr
from .models import Quest_round2 as qr2
from .models import Quest_round3 as qr3
from .models import Quest_round4 as qr4
from .models import Rounds as rd
from .models import Tea_m as tm
from .models import Dugout as dg

def t_t(request):
    for i in range(1,8):
        obj = tm.objects.filter(t_id = i).first()
        obj.score = 0
        obj.save()
    return HttpResponse("Done")

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

def r3(request):
    rounds = rd.objects.filter(round="round3").first()
    print(type(rounds.rules))
    return render(request, "r3.html", {"rounds": rounds.rules})

def r4(request):
    rounds = rd.objects.filter(round="round4").first()
    print(type(rounds.rules))
    return render(request, "r4.html", {"rounds": rounds.rules})

def r5(request):
    rounds = rd.objects.filter(round="round5").first() 
    print(type(rounds.rules))
    return render(request, "r5.html", {"rounds": rounds.rules})

def r5_quest(request, team):
    return render(request, "r5_quest.html", {
        "teams":list(tm.objects.filter(spec=False, dug_out=False).order_by('score'))[::-1],
        "team":tm.objects.filter(dug_out = False, spec = False).order_by("t_id")[team-1],
        "team_id":team,
    }
        )

def r4_quest(request, id, team):
    if id >= 8:
        return redirect("/graph/r5_ele")
    ph = True if id<=4 else False
    yt = True if not ph else False
    
    if request.method == "POST":
        res = int(request.POST.get("inp"))
        if res == 1:
            obj = tm.objects.filter(dug_out = False, spec = False).order_by("t_id")[team-1]
            print(obj)
            obj.score += qr4.objects.filter(qes_id = id).first().score
            obj.save()
        else:
            obj = tm.objects.filter(dug_out = False, spec = False).order_by("t_id")[team-1]
            obj.score -= qr4.objects.filter(qes_id = id).first().deduct
            obj.save()

        id += 1
        team += 1
    quest = qr4.objects.filter(qes_id = id).first()
    team =  1 if team > 4 else team
    tea_m = tm.objects.filter(dug_out = False, spec = False).order_by("t_id")[team-1]
    return render(request, "r4_quest.html", {
        "q":id,
        "t":team,
        "team":tea_m,
        "quest":quest,
        "teams": list(tm.objects.filter(spec=False, dug_out=False).order_by('score'))[::-1],
        "yt":yt,
        "ph":ph,
        })

def r5_elemator(request):
    elemeted_team = list(tm.objects.filter(spec=False, dug_out=False).order_by('score'))[::-1][-1]
    ob = tm.objects.filter(team_name = elemeted_team).first()
    ob.dug_out = True
    ob.save()
        
    print(elemeted_team)
    return render(request, "r5_ele.html", {"team":elemeted_team})


def r4_elemator(request):
    elemeted_team = list(tm.objects.filter(spec=False, dug_out=False).order_by('score'))[::-1][-1]
    ob = tm.objects.filter(team_name = elemeted_team).first()
    ob.dug_out = True
    ob.save()
        
    print(elemeted_team)
    return render(request, "r4_ele.html", {"team":elemeted_team})

def r3_elemator(request):
    elemeted_team = list(tm.objects.filter(spec=False).order_by('score'))[::-1][-1]
    ob = tm.objects.filter(team_name = elemeted_team).first()
    ob.dug_out = True
    ob.save()
        
    print(elemeted_team)
    return render(request, "r3_ele.html", {"team":elemeted_team})

def r3_quest_lrbd(request, id):
    ans = ""
    if id >= 9:
        return redirect("/graph/r4_ele")
    if request.method == "POST":
        pro_lst = request.POST.get("pro_lst")
        pro_lst = list(json.loads(pro_lst))
        dep_lst = request.POST.get("dep_lst")
        dep_lst = list(json.loads(dep_lst))
        i = 0
        print(pro_lst)
        if len(pro_lst)!=0:
            print("here", pro_lst)
            for lst in pro_lst:
                print(lst)
                team = tm.objects.filter(team_name=lst["team"]).first()
                team.score += 50 - i
                team.save()
                i += 10
        if len(dep_lst)!=0:
            for lst in dep_lst: 
                print(lst)
                team = tm.objects.filter(team_name=lst["team"]).first()
                team.score -= 20
                team.save()
        
    quest = qr3.objects.filter(qes_id = id).first()
    teams = list(tm.objects.filter(spec=False, dug_out=False).order_by('score'))[::-1]
    if quest.ans == 1: ans = quest.option1
    if quest.ans == 2: ans = quest.option2
    if quest.ans == 3: ans = quest.option3
    if quest.ans == 4: ans = quest.option4
    return render(request, "r3_quest_lrbd.html", {"teams":teams,"quest":quest, "ans":ans, "count":id+1, "counter":id})

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


def r1_test_quest(request, id, team, con):
    t = team
    inp = request.POST.get("inp")
    pas = request.POST.get("pas")

    if inp == 'p':
        if pas == pas:
            team = ""
        team += 1
        t = team

    if con == 'g':
        quest = qr.objects.filter(qes_id = id).first()
        team = tm.objects.filter(t_id = team).first()
    return render(request, "r1_test_quest.html",{
        "quest":quest,
        "team":team,
        "q":id,
        "t":t,
        "teams": list(tm.objects.filter(spec=False).order_by('score'))[::-1],
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





