
import os
import shutil
from pathlib import Path
from datetime import datetime


# Extension categories
FILE_CATEGORIES = {
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".ppt", ".pptx", ".xls", ".xlsx"
    ],

    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".svg", ".webp"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz"
    ],

    "Code": [
        ".py", ".java", ".c", ".cpp",
        ".html", ".css", ".js", ".sql"
    ]
}


# Function 1: Identify file category
def get_category(extension):

    for category, extensions in FILE_CATEGORIES.items():

        if extension.lower() in extensions:
            return category

    return "Others"


# Function 2: Find a safe destination filename
def get_unique_path(destination):

    if not destination.exists():
        return destination

    folder = destination.parent
    name = destination.stem
    extension = destination.suffix

    count = 1

    while True:

        new_name = f"{name}_{count}{extension}"

        new_path = folder / new_name

        if not new_path.exists():
            return new_path

        count += 1


# Function 3: Organize files
def organize_files(directory):

    total_files = 0
    moved_files = 0
    skipped_files = 0
    error_files = 0

    print("\nScanning directory:", directory)

    try:

        # Read directory contents
        for filename in os.scandir(directory):

            if not filename.is_file():
                continue

            total_files += 1

            source = Path(filename.path)

            # Identify extension
            extension = source.suffix.lower()

            # Identify category
            category = get_category(extension)

            # Create category folder
            category_folder = directory / category

            try:

                category_folder.mkdir(
                    parents=True,
                    exist_ok=True
                )

                # Create destination path
                destination = category_folder / source.name

                # Handle duplicate filenames
                destination = get_unique_path(destination)

                # Move file
                shutil.move(str(source), str(destination))

                moved_files += 1

                print(
                    f"MOVED: {source.name} -> "
                    f"{category}/{destination.name}"
                )

            except PermissionError:

                error_files += 1

                print("Permission denied:", source.name)

            except FileExistsError:

                error_files += 1

                print("File already exists:", source.name)

            except OSError as error:

                error_files += 1

                print("Error moving", source.name, ":", error)

    except PermissionError:

        print("Permission denied while accessing directory.")

        return

    except OSError as error:

        print("Directory error:", error)

        return

    skipped_files = total_files - moved_files - error_files

    # Execution summary
    print("\n====================================")
    print("       FILE ORGANIZATION REPORT")
    print("====================================")

    print("Directory:", directory)
    print("Total files scanned:", total_files)
    print("Files moved:", moved_files)
    print("Files skipped:", skipped_files)
    print("Errors:", error_files)

    print("Completed at:", datetime.now())

    print("====================================")


# Function 4: Main program
def main():

    print("\n====================================")
    print("   AUTOMATED FILE ORGANIZER")
    print("====================================")

    directory_input = input(
        "\nEnter directory path to organize: "
    ).strip().strip('"')

    directory = Path(directory_input).expanduser()

    # Validate directory
    if not directory.exists():

        print("Error: Directory does not exist.")
        return

    if not directory.is_dir():

        print("Error: The given path is not a directory.")
        return

    print("\nSelected directory:", directory.resolve())

    confirmation = input(
        "Do you want to organize this directory? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        organize_files(directory)

    else:

        print("\nOrganization cancelled.")


# Execute the program
if __name__ == "__main__":

    main()

====================================
   AUTOMATED FILE ORGANIZER
====================================

Enter directory path to organize:
Test_Files

Selected directory: Test_Files

Do you want to organize this directory? (yes/no): yes

MOVED: Resume.pdf -> Documents/Resume.pdf
MOVED: Photo.jpg -> Images/Photo.jpg
MOVED: Video.mp4 -> Videos/Video.mp4
MOVED: Project.zip -> Archives/Project.zip
MOVED: program.py -> Code/program.py

====================================
       FILE ORGANIZATION REPORT
====================================

Total files scanned: 5
Files moved: 5
Files skipped: 0
Errors: 0

====================================
