import subprocess

class Vim:
    @staticmethod
    def run():
        commands = [
            "sudo apt install vim -y",
            # Additional Vim setup commands can be added here
        ]

        for command in commands:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            while True:
                output = process.stdout.readline()
                if output:
                    print(output.strip())
                if output == '' and process.poll() is not None:
                    break

            if process.returncode != 0:
                print(f"Error executing {command}, exited with {process.returncode}")

