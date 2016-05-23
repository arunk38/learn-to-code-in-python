import os.path

# define a filename.
filename = "read_file.py"

# open the file as f
# The function readlines() reads the file.
if not os.path.isfile(filename): # check for file existence
    print("File does not exist: " + filename)
else:
    with open(filename) as f:
        content = f.read().splitlines()

    # show the file contents line by line
    for line in content:
        print(line)