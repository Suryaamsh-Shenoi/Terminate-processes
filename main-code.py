import subprocess
import time
import psutil

def list_all_processes():
    """List all running processes."""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_info = proc.as_dict(attrs=['pid', 'name'])
            print(process_info)
        except psutil.NoSuchProcess:
            pass

def get_process_by_name(process_name):
    """Return a list of process IDs for a given process name."""
    process_ids = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() == process_name.lower():
                process_ids.append(proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_ids

def kill_process_by_pid(pid):
    """Kill a process by its PID."""
    try:
        p = psutil.Process(pid)
        p.terminate()  # or p.kill()
        print(f"Process {pid} terminated.")
    except psutil.NoSuchProcess:
        print(f"No such process with PID {pid}.")

def main():
    process_name = input(" Enter the process which needs to be eliminated ")  # Change to the target process name
    wait_time = int(input(" Time in seconds to wait before eliminating process "))  # Time in seconds to wait before closing the application

    print(f"Listing all running processes to verify the name:")
    list_all_processes()

    print(f"Waiting for {wait_time} seconds before closing {process_name}...")
    time.sleep(wait_time)

    process_ids = get_process_by_name(process_name)
    if not process_ids:
        print(f"No running process found with name {process_name}.")
        return

    for pid in process_ids:
        kill_process_by_pid(pid)

if __name__ == "__main__":
    main()