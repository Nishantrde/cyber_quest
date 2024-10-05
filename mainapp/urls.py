from django.urls import path
from .views import *

urlpatterns = [
    path("",index),
    path("dis", disclaimer),
    path("teams", display_teams),
    path("r1", r1),
    path("r2", r2),
    path("r3", r3),
    path("r3_ele", r3_elemator),
    path("r2_quest/<int:id>/<int:team_id>", r2_quest),
    path("r1_quest", r1_quest),
    path("graph/<str:id>", graph),
    path("ws",ws),
    path("ws_r",round_ws),
]

