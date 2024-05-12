contents = ["slice the carrots",
            "carrots were sliced",
            "the recipe was yumsies"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)