fire_in_cell = input().split("#")
water_amount = int(input())

put_out_cells = []
total_fire = 0
effort = 0

for i in fire_in_cell:
    single_cell = []
    single_cell.append(i.split()[0])
    single_cell.append(i.split()[2])

    fire_type = single_cell[0]
    fire_range = int(single_cell[1])

    if fire_range > water_amount:
        continue

    if (
            (fire_type == "High" and (81 <= fire_range <= 125)) or (
            fire_type == "Medium" and (51 <= fire_range <= 80)) or (fire_type == "Low" and (1 <= fire_range <= 50))
    ):
        water_amount -= fire_range
        # if water_amount <= 0:
        #   break

        put_out_cells.append(fire_range)
        effort += (fire_range * 0.25)
        total_fire += fire_range

print("Cells:", *put_out_cells, sep="\n - ")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


# OPTION 2

# fire_in_cell = input().split("#")
# water_amount = int(input())
#
# put_out_cells = []
# total_fire = 0
# # effort = 0
#
# for i in fire_in_cell:
#     # single_cell = []
#     # single_cell.append(i.split()[0])
#     # single_cell.append(i.split()[2])
#
#     single_cell = i.split(" = ")
#
#     fire_type = single_cell[0]
#     fire_range = int(single_cell[1])
#
#     if fire_type == "High" and (fire_range < 81 or fire_range > 125):
#         continue
#     if fire_type == "Medium" and (fire_range < 51 or fire_range > 80):
#         continue
#     if fire_type == "Low" and (fire_range < 1 or fire_range > 50):
#         continue
#     if fire_range > water_amount:
#         continue
#
#     water_amount -= fire_range
#
#     # if water_amount <= 0:
#     #   break
#
#     put_out_cells.append(fire_range)
#     # effort += (fire_range * 0.25)
#     total_fire += fire_range
#
# # print("Cells:", *put_out_cells, sep="\n - ")
# print("Cells:")
# for cell in put_out_cells:
#     print(f" - {cell}")
#
# effort = total_fire * 0.25
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")
#


