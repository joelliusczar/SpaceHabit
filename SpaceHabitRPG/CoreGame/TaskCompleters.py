

def complete_daily(dailyid,heroid):
    daily = ModelLayer.get_daily_by_id(dailyid)
    hero = ModelLayer.get_hero_by_id(heroid)
    result = do_damage_to_monster(hero,daily)

def complete_todo(todoid,heroid):
    todo = ModelLayer.get_todo_by_id(todoid)
    hero = ModelLayer.get_hero_by_id(heroid)
    hero['gold'] += get_weighted_todo_gold_reward(todo)
    hero['xp'] += get_weighted_todo_xp_reward(todo)
    raise NotImplementedError()

def plus_1_habit(habitid,heroid):
    habit = ModelLayer.get_habit_by_id(habitid)
    hero = ModelLayer.get_hero_by_id("hero",heroid)
    hero['gold'] += get_weighted_habit_gold_reward(habit)
    hero['xp'] += get_weighted_habit_xp_reward(habit)
    raise NotImplementedError()
    
def minus_1_habit(habitid,heroid):
    habit = ModelLayer.get_habit_by_id(habitid)
    hero = ModelLayer.get_hero_by_id(heroid)
    hero['hp'] -= get_weighted_health_penalty(habit)
    raise NotImplementedError()
