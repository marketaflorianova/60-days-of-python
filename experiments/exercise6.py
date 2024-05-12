filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"../files2/{filename}", "w")
    add_hello = file.write("Hello")
    file.close()