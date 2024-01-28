import subprocess
import threading
import os

def run_interactsh(session_number):
    path = "/Users/arupgope"  #change to your actual golang path 
    command = [f"{path}/go/bin/interactsh-client"]
    # command = "./interactsh-client"

    output_file = os.path.join("data", f"out{session_number}.txt")

    os.makedirs("data", exist_ok=True)

    with open(output_file, "a") as file:
        process = subprocess.Popen(command, stdout=file, stderr=subprocess.STDOUT)
        process.wait()

        return_code = process.returncode
        print(f"Session {session_number} exited with return code: {return_code}")

n = int(input("Enter how many sessions you want to run:"))
# n = 5
# Create threads for sessions
threads = []
if(n<=5):
    for i in range(0, n):
        thread = threading.Thread(target=run_interactsh, args=(i,))
        threads.append(thread)
else:
    j= n-5;
    for i in range(j,n):
        thread = threading.Thread(target=run_interactsh, args=(i,))
        threads.append(thread)
    
# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join() 

print("All sessions have completed.")

