import zipfile  # importing the program we are going to use for our zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:  # making a zipfile
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":                   # code that says if this file is executed here
    make_archive(filepaths=["bonus1.py"], dest_dir="dest")
