import os, sys, subprocess, time, pexpect

au = sys.argv[1]
ds = sys.argv[2]

assert au in ["RPK", "DID"]

RUNS = 10

print(f"\n\n\n\n\n\nWill prepare {au}")
for i in [0, 1]:
    if input(f"\nflash {au} device {i}? [y/N] ").lower() == "y":
        os.system(f"make BOARD=pulga PROGRAMMER=openocd AUTH={au} flash")

print(f"\n\nWill run {au}")
print("  cmd:  init handshake fe80::a4dd:f143:3055:dc42")

input(f"\npress enter for {au} {ds}")
res_file = f"results/edhoc-{au}-{ds}.log"

process = pexpect.spawn(f"make BOARD=pulga PORT=/dev/ttyUSB0 AUTH={au} term")
process.logfile = open(res_file, "wb")
input(f"> logfile is {process.logfile}")

for i in range(0, RUNS):
    input(f">>> RUN={i} reboot and handshake - press enter")
    process.sendline("reboot")
    time.sleep(1)
    process.sendline("init handshake fe80::a4dd:f143:3055:dc42")

    try:
        process.expect(r".*\[init\] end")
    except pexpect.expect.TIMEOUT as e:
        input("timed out -- MAKE SURE TO manually reboot the device (press enter)")

    print("\nfinished")

        #os.system(f"make BOARD=pulga PORT=/dev/ttyUSB0 AUTH={au} term | tee -a results/edhoc-{au}-{ds}.log")
"""
        proc = subprocess.Popen(f"make BOARD=pulga PORT=/dev/ttyUSB0 AUTH={au} term | tee -a results/edhoc-{au}-{ds}.log", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        print(f">>> reboot and handshake in {sleep_time}")
        time.sleep(sleep_time)
        print(">>> reboot and handshake now")
        proc.communicate(input="reboot\n")
        proc.communicate(input="init handshake fe80::a4dd:f143:3055:dc42\n")
"""

