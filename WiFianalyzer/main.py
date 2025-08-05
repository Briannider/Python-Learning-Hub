import subprocess


def get_traffic():
    try:
        result = subprocess.run(
            ["iptables", "-L", "FORWARD", "-v", "-n", "-x"],
            capture_output=True,
            text=True,
            check=True,
        )
        lines = result.stdout.split("\n")
        for line in lines:
            if "192.168." in line:  # Ajustá según tu red
                print(line)
    except FileNotFoundError:
        print(
            "Error: 'iptables' command not found. Please ensure it is installed and in your PATH."
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running iptables: {e}")


get_traffic()
