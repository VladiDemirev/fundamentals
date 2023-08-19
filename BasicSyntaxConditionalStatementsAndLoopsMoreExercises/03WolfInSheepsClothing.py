def warn_the_sheep(animals_list):
    if animals_list[0] == "wolf":
        return "Please go away and stop eating my sheep"
    else:
        for animal in animals_list[1:]:
            if animal == "wolf":
                next_sheep_index = animals_list.index("wolf")
                return f"Oi! Sheep number {next_sheep_index}! You are about to be eaten by a wolf!"


animals = list(reversed(input().split(", ")))

print(warn_the_sheep(animals))
