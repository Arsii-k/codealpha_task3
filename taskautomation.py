import os
import shutil


def organize_files(source_dir, destination_dir):

    if not os.path.exists(source_dir):

        print(f"Source directory '{source_dir}' does not exist.")

        return

    if not os.path.exists(destination_dir):

        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):

        source_path = os.path.join(source_dir, filename)

        if os.path.isfile(source_path):

            _, extension = os.path.splitext(filename)

            extension = extension.lower()

            if extension in ['.jpg', '.jpeg', '.png', '.gif']:

                destination_subdir = 'images'

            elif extension in ['.doc', '.docx', '.pdf', '.txt']:

                destination_subdir = 'documents'

            elif extension in ['.mp4', '.avi', '.mkv', '.mov']:

                destination_subdir = 'videos'

            else:

                destination_subdir = 'other'

            destination_path = os.path.join(destination_dir, destination_subdir, filename)

            shutil.move(source_path, destination_path)

    print("File organization completed.")


if __name__ == "__main__":

    source_directory = "E:/path/to/your/source_directory"

    destination_directory = "E:/path/to/your/destination_directory"

    organize_files(source_directory, destination_directory)
