from django.urls import path
from .views import *

urlpatterns = [
    path("",index),
    path("r1_rules", r1_rules),
    path("teams", display_teams),
    path("r1", r1),
    path("r2", r2),
    path("r2_quest", r2_quest),
    path("r1_quest", r1_quest),
    path("graph", graph),
    path("ws",ws),
    path("ws_r",round_ws),
]

