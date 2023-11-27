import subprocess
import os

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")

def main():
    # Base setup commands
    base_commands = [
        "sudo apt update",
        "sudo apt upgrade -y",
        # Add more base setup commands here
    ]

    for command in base_commands:
        run_command(command)

    # Load and run plugins
    plugins_dir = "plugins"
    for plugin_file in os.listdir(plugins_dir):
        if plugin_file.endswith(".py"):
            module_name = plugin_file[:-3]
            module = __import__(f"plugins.{module_name}", fromlist=[module_name.capitalize()])
            plugin_class = getattr(module, module_name.capitalize())
            plugin_class.run()

if __name__ == "__main__":
    main()

