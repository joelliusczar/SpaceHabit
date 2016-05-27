

def do_damage_to_monster(monster,damage):
    result = {}
    if damage >= monster.nowHp:
        result['xp'] = get_xp_reward_for_monster(monster)
        result['treasure'] = check_for_dropped_treasure(monster)
        monster.nowHp = 0
    else:
        monster.nowHp -= damage
    monster.save_changes()
    return result


def calculate_daily_damage_to_monster(hero,daily,monster):
    raise NotImplementedError

def calculate_habit_damage_to_monster(hero,habit,monster):
    raise NotImplementedError

def calculate_todo_damage_to_monster(hero,todo,monster):
    raise NotImplementedError

def get_xp_reward_for_monster(monster):
    raise NotImplementedError

def check_for_dropped_treasure(hero,luck):
    raise NotImplementedError


def get_weighted_daily_gold_reward(daily):
    raise NotImplementedError("get_weighted_daily_gold_reward")

def get_weighted_daily_xp_reward(daily):
    raise NotImplementedError("get_weighted_daily_xp_reward")

def get_weighted_daily_hp_penalty(daily,monster):
    raise NotImplementedError("get_weighted_daily_hp_penalty")


def get_weighted_todo_gold_reward(todo):
    raise NotImplementedError()

def get_weighted_todo_xp_reward(todo):
    raise NotImplementedError()


def get_weighted_habit_gold_reward(habit):
    raise NotImplementedError()

def get_weighted_habit_xp_reward(habit):
    raise NotImplementedError()

def get_weighted_health_penalty(habit):
    raise NotImplementedError()