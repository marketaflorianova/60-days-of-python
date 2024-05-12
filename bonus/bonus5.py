waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for i, j in enumerate(waiting_list):
    row = f"{i+1}.{j.capitalize()}"
    print(row)