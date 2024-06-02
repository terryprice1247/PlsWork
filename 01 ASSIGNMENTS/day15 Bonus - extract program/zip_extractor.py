import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:      # archive represents the file entity
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("compressed.zip", dest_dir="files")
