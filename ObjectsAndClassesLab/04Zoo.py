class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, names):
        if species == "mammal":
            self.mammals.append(names)
        elif species == "fish":
            self.fishes.append(names)
        elif species == "bird":
            self.birds.append(names)

        # self._Zoo__animals += 1
        Zoo._Zoo__animals += 1

    def get_info(self, species):
        info = ""
        if species == "mammal":
            info = f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == "fish":
            info = f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == "bird":
            info = f"Birds in {self.zoo_name}: {', '.join(self.birds)}"

        return f"{info}\nTotal animals: {Zoo._Zoo__animals}"


zoo_name = input()
inputs_count = int(input())

zoo = Zoo(zoo_name)

for _ in range(inputs_count):
    species, name = input().split()
    zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))
# print(f"Total animals: {zoo._Zoo__animals}")
# print(f"Total animals: {Zoo._Zoo__animals}")
