stops = input()
command = input()
initial_string = stops

while command != "Travel":
    command_args = command.split(":")
    action = command_args[0]

    if action == "Add Stop":
        index = int(command_args[1])
        string = command_args[2]
        if index in range(-len(stops), len(stops)):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif action == "Remove Stop":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if (
                start_index in range(-len(stops), len(stops)) and
                end_index in range(-len(stops), len(stops))
        ):
            removed_part = stops[start_index:end_index + 1]
            stops = stops.replace(removed_part, "")
        print(stops)
    elif action == "Switch":
        old_string = command_args[1]
        new_string = command_args[2]
        if old_string in initial_string:
            old_string_count = initial_string.count(old_string)
            stops = stops.replace(old_string, new_string, old_string_count)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
