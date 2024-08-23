import pathlib
import zipfile


def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(pathlib.Path(dest_dir, "compressed.zip"), 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":  # script is executed directly as a main script, now while importing
    make_archive(filepaths=["bonus2.py", "bonus3.py"], dest_dir="dest_dir")
