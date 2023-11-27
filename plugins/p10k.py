import subprocess

class P10k:
    @staticmethod
    def run():
        # Commands to install Zsh and Powerlevel10k
        zsh_p10k_commands = [
            "sudo apt install zsh -y",
            "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k",
            "echo 'source ~/.oh-my-zsh/custom/themes/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc",
            # Set Zsh as the default shell, if desired
            "chsh -s $(which zsh)"
        ]

        # Commands to install recommended fonts for Powerlevel10k
        font_install_commands = [
            "sudo apt install fonts-powerline -y",
            # Additional font installation commands can be added here
        ]

        # Execute Zsh and Powerlevel10k installation commands
        for command in zsh_p10k_commands:
            P10k.execute_command(command)

        # Execute font installation commands
        for command in font_install_commands:
            P10k.execute_command(command)

    @staticmethod
    def execute_command(command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if output:
                print(output.strip())
            if output == '' and process.poll() is not None:
                break
        if process.returncode != 0:
            print(f"Error executing {command}, exited with {process.returncode}")

