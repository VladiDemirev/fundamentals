def heroes_collection(number_heroes):
    heroes_dict = {}
    for _ in range(number_heroes):
        hero, *params = input().split()
        hit_points = int(params[0])
        mana_points = int(params[1])
        heroes_dict[hero] = [hit_points, mana_points]
    return heroes_dict


def cast_spell(heroes_dict, hero, mana_needed, spell_name):
    if heroes_dict[hero][1] >= mana_needed:
        heroes_dict[hero][1] -= mana_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero][1]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")


def take_damage(heroes_dict, hero, damage, attacker):
    heroes_dict[hero][0] -= damage
    if heroes_dict[hero][0] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero][0]} HP left!")
    else:
        heroes_dict.pop(hero)
        print(f"{hero} has been killed by {attacker}!")


def recharge(heroes_dict, hero, amount):
    heroes_dict[hero][1] += amount
    if heroes_dict[hero][1] > 200:
        amount = 200 - (heroes_dict[hero][1] - amount)
        heroes_dict[hero][1] = 200
    print(f"{hero} recharged for {amount} MP!")


def heal(heroes_dict, hero, amount):
    heroes_dict[hero][0] += amount
    if heroes_dict[hero][0] > 100:
        amount = 100 - (heroes_dict[hero][0] - amount)
        heroes_dict[hero][0] = 100
    print(f"{hero} healed for {amount} HP!")


def commands_given(heroes_dict):
    while True:
        action, *params = input().split(" - ")
        if action == "End":
            return heroes_dict
        elif action == "CastSpell":
            hero, mana_needed, spell_name = params[0], int(params[1]), params[2]
            cast_spell(heroes_dict, hero, mana_needed, spell_name)
        elif action == "TakeDamage":
            hero, damage, attacker = params[0], int(params[1]), params[2]
            take_damage(heroes_dict, hero, damage, attacker)
        elif action == "Recharge":
            hero, amount = params[0], int(params[1])
            recharge(heroes_dict, hero, amount)
        elif action == "Heal":
            hero, amount = params[0], int(params[1])
            heal(heroes_dict, hero, amount)


def game_control(number_heroes):
    heroes_dict = heroes_collection(number_heroes)
    final_heroes_dict = commands_given(heroes_dict)

    for hero, specs in heroes_dict.items():
        print(f"{hero}")
        print(f" HP: {specs[0]}")
        print(f" MP: {specs[1]}")


heroes_count = int(input())
game_control(heroes_count)
