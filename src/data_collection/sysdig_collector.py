import subprocess

def collect_sysdig_logs(output_file):
    """Collect system call logs using Sysdig and save to a file."""
    command = f"sysdig -w {output_file}"
    subprocess.run(command, shell=True, check=True)
    print(f"Logs saved to {output_file}")

if __name__ == "__main__":
    collect_sysdig_logs("sysdig_logs.scap")

