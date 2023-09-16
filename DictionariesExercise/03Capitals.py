# countries = input().split(", ")
# capitals  = input().split(", ")

# country_capital = {}
# index = 0

# for country in countries:
#   country_capital[country] = capitals[index]
#   index += 1

# for country, capital in country_capital.items():
#   print(f"{country} -> {capital}")


# # OPTION 2

# countries = input().split(", ")
# capitals  = input().split(", ")

# result = list(zip(countries, capitals))

# country_capital = {country: capital for (country, capital) in result}

# result = [f"{country} -> {capital}" for country, capital in country_capital.items()]

# print('\n'.join(result))


# OPTION 3

countries = input().split(", ")
capitals = input().split(", ")

country_capital = {countries[idx]: capitals[idx] for idx in range(len(countries))}

result = [f"{country} -> {capital}" for country, capital in country_capital.items()]

print('\n'.join(result))
