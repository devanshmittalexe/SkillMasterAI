import os

# Base folder
base_folder = "skill_mirror"

# Files to create
files = [
    "main.py",
    "identifier.py",
    "questioner.py",
    "examiner.py",
    "invigilator.py",
    "analyzer.py",
    "announcer.py",
    "database.py",
]

# Create base folder
os.makedirs(base_folder, exist_ok=True)

# Create files inside folder
for file in files:
    file_path = os.path.join(base_folder, file)
    with open(file_path, "w") as f:
        f.write("# " + file.replace(".py", "").capitalize() + " module\n")

print("Project structure created successfully.")