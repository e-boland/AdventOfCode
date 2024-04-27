def part1():
    with open("input.txt") as f:
        data = f.readlines()
        best_distance = 0

    for reindeer in data:
        name, _, _, speed, _, _, speed_time, _, _, _, _, _, _, rest_time, _ = (((reindeer.replace(',', '')).strip()).strip()).split(' ')
        
        resting = False
        total_time = 0
        distance = 0
        
        while total_time < 2503:
            current_time = 0

            if not resting:
                distance += int(speed) * int(speed_time)
                total_time += int(speed_time)
                resting = True

            else:
                total_time += int(rest_time)
                resting = False

            if total_time > 2503 and resting:
                time_dif = total_time - 2503
                distance -= time_dif * int(speed_time)

        if distance > best_distance:
            best_distance = distance    
                
    return best_distance


def part2():
    with open("input.txt") as f:
        data = f.readlines()
        reindeers = dict()

    for reindeer in data:
        name, _, _, speed, _, _, speed_time, _, _, _, _, _, _, rest_time, _ = (((reindeer.replace(',', '')).strip()).strip()).split(' ')

        reindeers[name] = {"speed": speed, "speed_time": speed_time, "rest_time": rest_time,
                           "distance": 0, "resting": False, "score": 0, "current_time": 0}

    total_time = 0
    best_distance = 0
    best_score = 0

    while total_time < 2503:

        for reindeer, infos in reindeers.items():

            if not infos["resting"]:  # if not resting
                infos["distance"] += int(infos["speed"])
                infos["current_time"] += 1
                if infos["current_time"] == int(infos["speed_time"]):
                    infos["current_time"] = 0
                    infos["resting"] = True

            else:
                infos["current_time"] += 1
                if infos["current_time"] == int(infos["rest_time"]):
                    infos["current_time"] = 0
                    infos["resting"] = False

            if infos["distance"] > best_distance:
                best_distance = infos["distance"]

        for reindeer, infos in reindeers.items():
            if infos["distance"] == best_distance:
                infos["score"] += 1

        total_time += 1

    for reindeer, infos in reindeers.items():
        score = infos["score"]
        if score > best_score:
            best_score = score

    return best_score


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
