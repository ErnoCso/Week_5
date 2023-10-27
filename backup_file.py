# Write a program that takes the name of a file as a command-line argument, and
# creates a backup copy of that file. The backup should contain an exact copy of the
# contents of the original and should, obviously, have a different name.
# Hint: By now, you should be getting the idea that there is a built-in way to do the
# heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.


import sys
import shutil

if len(sys.argv) != 2:
    print("Usage: python backup_file.py <filename>")
else:
    orig_filename = sys.argv[1]

    # Check if the original file exists
    if not shutil.os.path.exists(orig_filename):
        print(f"The file '{orig_filename}' does not exist.")
    else:
        # Generate a backup filename by adding ".bak" to the original filename
        backup_filename = orig_filename + ".bak"

        # Create a backup copy of the file
        shutil.copy(orig_filename, backup_filename)
        print(f"Backup copy created as '{backup_filename}'")

# python backup_file.py yourfile.txt(C:\Users\x<username>x\Desktop\yourfile.txt)
