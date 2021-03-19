import subprocess
print("========= CREATED alhassanAlharb7 =========")
ip = input("enter the IP \n")
ping = subprocess.call(['ping','-c' '1', ip])
if ping == 0:
    print("\033[1;32mThe IP is run")
else:
    print("\033[1;31mThe IP is down")