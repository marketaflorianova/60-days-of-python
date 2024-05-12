filenames = ["1.raw data.txt", "2.reports.txt"]
filenames_new = []

for item in filenames:
    item_new = item.replace('.', '_', 1)
    print(item_new)
    filenames_new.append(item_new)
    print(filenames_new)

