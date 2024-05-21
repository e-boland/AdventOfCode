from itertools import product


def starting_stats_and_objects():
    # PLAYER AND BOSS STATS:
    boss_stats = {"damage": 8, "defense": 2}
    player_stats = {"damage": 0, "defense": 0}

    # OBJECTS: {stat: cost}, negative numbers are defense and positive ones are damage
    weapons = {4: 8, 5: 10, 6: 25, 7: 40, 8: 74}
    armors = {0: 0, -1: 13, -2: 31, -3: 53, -4: 75, -5: 102}
    rings = {0: 0, -1: 20, 1: 25, -2: 40, 2: 50, -3: 80, 3: 100}

    # EQUIPMENTS: (1 weapon, 0 or 1 armor, 0, 1 or 2 different rings)
    all_equipments = product(weapons.keys(), armors.keys(), rings.keys(), rings.keys())
    equipments = [equipment for equipment in all_equipments if not (equipment[2] == equipment[3] and equipment[2] != 0)]

    # EQUIPMENTS BY COST: {cost: [equipments]}, sorted from lowest to highest costs
    cost_equipments = dict()
    for equipment in equipments:
        cost = weapons[equipment[0]] + armors[equipment[1]] + rings[equipment[2]] + rings[equipment[3]]
        if cost not in cost_equipments.keys():
            cost_equipments[cost] = [equipment]
        else:
            cost_equipments[cost].append(equipment)
    equipments_by_cost = dict(sorted(cost_equipments.items()))

    return boss_stats, player_stats, equipments_by_cost


def play_game(boss, player):
    player_health = 100
    boss_health = 100

    while boss_health > 0 and player_health > 0:
        player_hit = max(1, player['damage'] - boss['defense'])
        boss_health -= player_hit
        if boss_health <= 0:
            continue
        boss_hit = max(1, boss['damage'] - player['defense'])
        player_health -= boss_hit

    if boss_health <= 0:
        # print(f"Player won with {player_health} HP left")
        return True
    else:
        # print(f"Player lost, Boss has {boss_health} HP left")
        return False


def best_equipment():
    boss, player, cost_equipments = starting_stats_and_objects()

    for cost, equipments in cost_equipments.items():
        for equipment in equipments:
            player['damage'] = sum([num for num in equipment if num > 0])
            player['defense'] = abs(sum([num for num in equipment if num < 0]))

            player_victory = play_game(boss, player)
            if player_victory:
                return cost


def worst_equipment():
    boss, player, cost_equipments = starting_stats_and_objects()
    decreasing_cost_equipments = dict(sorted(cost_equipments.items(), reverse=True))  # from highest to lowest cost

    for cost, equipments in decreasing_cost_equipments.items():
        for equipment in equipments:

            player['damage'] = sum([num for num in equipment if num > 0])
            player['defense'] = abs(sum([num for num in equipment if num < 0]))

            player_victory = play_game(boss, player)
            if not player_victory:
                return cost


def main():
    print(best_equipment())
    print(worst_equipment())


if __name__ == "__main__":
    main()

