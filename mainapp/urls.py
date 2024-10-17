from django.urls import path
from .views import *

urlpatterns = [
    path("t0",t_t),
    path("",index),
    path("dis", disclaimer),
    path("teams", display_teams),
    path("r1", r1),
    path("r2", r2),
    path("r3", r3),
    path("r4", r4),
    path("r3_ele", r3_elemator),
    path("r4_ele", r4_elemator),
    path("r4_quest/<int:id>/<int:team>", r4_quest),
    path("r3_quest/<int:team>", r3_quest),
    path("r3_quest_lrbd/<int:id>", r3_quest_lrbd),
    path("r2_quest/<int:id>/<int:team_id>", r2_quest),
    path("r1_quest", r1_quest),
    path("graph/<str:id>", graph),
    path("ws",ws),
    path("ws_r",round_ws),
]

