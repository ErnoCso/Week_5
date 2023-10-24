import sys
import shutil

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python backup_file.py <filename>")
    else:
        original_filename = sys.argv[1]

        # Check if the original file exists
        if not shutil.os.path.exists(original_filename):
            print(f"The file '{original_filename}' does not exist.")
        else:
            # Generate a backup filename by adding ".bak" to the original filename
            backup_filename = original_filename + ".bak"

            # Create a backup copy of the file
            shutil.copy(original_filename, backup_filename)
            print(f"Backup copy created as '{backup_filename}'")

# python backup_file.py yourfile.txt