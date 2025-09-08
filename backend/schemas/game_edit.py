# backend/schemas/game_edit.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time
from backend import models

#-----------------
# for top
#-----------------

class GameEditTop(BaseModel):
    num: int


#-----------------
# for substitution
#-----------------

class GameEditSubstitution(BaseModel):
    num: int


#-----------------
# for play
#-----------------

class GameEditPlay(BaseModel):
    num: int
