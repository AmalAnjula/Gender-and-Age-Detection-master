import subprocess as sp
import time



# Path to the Python script you want to run
script_path = r"C:\Users\Amal\Downloads\Gender-and-Age-Detection-master\addrun.py"
# Run the script
sp.run(["python", script_path])

time.sleep(1)

sp.run(['taskkill /f /FI "WINDOWTITLE eq Slidshow*"']) 