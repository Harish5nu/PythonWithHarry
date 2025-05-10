# write a program to print the content of a directory using os module search online for the function which does that.
import os

# Specify the directory path
directory_path = '/'  # any directory

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
