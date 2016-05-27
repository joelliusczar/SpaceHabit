import ModelLayer
from datetime import datetime, timedelta
import random

def check_all_tasks(heroid):
    hero = ModelLayer.get_hero_by_id(heroid)
    result = {}
    if not 'area' in hero:
        a = random.choice(hero['areaChoices'])
    lastTime = hero["lastTime"]
    nowTime = datetime.utcnow().timestamp()
    if (nowTime - lastTime)/(60*60*24) >= 1:
        dailyResults = check_dailies(hero['dailyIds'])
        habitResults = check_habits(hero['habitIds'])
        todoResults = check_todos(hero['todoIds'])


def check_dailies(dailyIds):
    for id in dailyIds:
        daily = ModelLayer.get_daily_by_id(id)

def check_habits(habitIds):
   for id in habitIds:
       habit = ModelLayer.get_habit_by_id(id)

def check_todos(todoIds):
    for id in todoIds:
        todo = ModelLayer.get_todo_by_id(id)


