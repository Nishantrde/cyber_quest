from django.urls import path
from .views import *

urlpatterns = [
    path("",index),
    path("r1_rules", r1_rules),
    path("teams", display_teams),
    path("r1", r1),
    path("r1_quest_rxw", r1_quest),
    path("graph1", graph1),
    path("ws",ws),
    path("ws_r",round_ws),
]

