import os
import shutil

# Define the root directory where your DAY* directories are located
root_dir = "./"  # Change this if needed
solutions_dir = os.path.join(root_dir, "solutions")
inputs_dir = os.path.join(root_dir, "inputs")

# Create solutions and inputs directories if they don't exist
os.makedirs(solutions_dir, exist_ok=True)
os.makedirs(inputs_dir, exist_ok=True)

# Iterate through each directory in the root
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)

    # Skip if it's not a directory or not a DAY* folder
    if not os.path.isdir(folder_path) or not folder.startswith("DAY"):
        continue

    # Iterate through files in the DAY* folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if file.endswith(".py"):
            # Move Python files to solutions directory
            shutil.move(file_path, os.path.join(solutions_dir, file))
        elif file.endswith(".txt"):
            # Move text files to inputs directory
            shutil.move(file_path, os.path.join(inputs_dir, file))

print("Files have been organized into 'solutions' and 'inputs'.")
