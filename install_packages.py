import subprocess

# Define a function to install packages from a requirements.txt file
def install_requirements(requirements_file):
    try:
        # Run the 'pip install -r' command to install packages from the requirements file
        subprocess.check_call(['pip', 'install', '-r', requirements_file])
        print("Successfully installed packages from", requirements_file)
    except subprocess.CalledProcessError:
        print("An error occurred while installing packages from", requirements_file)

# The following code block is executed only if the script is run directly, not when imported
if __name__ == "__main__":
    # path to the requirements.txt file
    requirements_file = "requirements.txt"

    # Call the install_requirements function to install packages from the requirements file
    install_requirements(requirements_file)
