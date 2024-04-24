from netmiko import ConnectHandler
import time
import os

# ip address print
# ip service print
# 118.179.157.241
# 118.179.222.100

# =========================
# ROUTER LIST
# =========================
ROUTERS = []

def ipTOdic(ip,user,password,dicName=ROUTERS):
    a = {
        'device_type': 'mikrotik_routeros',
         'host': str(ip),
         'port': 422,
         'username': str(user),
         'password': str(password),
         'conn_timeout': 20,
         'auth_timeout': 20,
         'banner_timeout': 20,
    }
    ROUTERS.append(a)



# =========================
# CMD LIST
# =========================

cmdList = []



# =========================
# Main function start
# =========================
outputLog = []
outputDataCSV =[]
def routerConfig(routers=ROUTERS, CMDS=cmdList):
    for singleRouter in routers:
        try:
            print("\n==========================================\n")
            print("------------------------------------------")
            print("[+] CONFIGURE", singleRouter["host"])
            print("------------------------------------------")
            # Check Ping status
            ping = os.system("ping -n 2 " + singleRouter["host"])

            if ping == 0:
                # Try to connect with router
                net_connect = ConnectHandler(**singleRouter)
                time.sleep(0.5)

                # Command execute
                for cmd in CMDS:
                    output = net_connect.send_command(cmd)
                    outputLog.append(output)

                print("------------------------------------------")
                print("[+] CONFIGURATION DONE ")
                print("------------------------------------------")
                csv_data = [singleRouter["host"], singleRouter["host"], "SUCCESS"]
                outputDataCSV.append(csv_data)

                output = []


            else:
                print("[!]Router is Down")
                csv_data = [singleRouter["host"], singleRouter["host"], "ROUTER DOWN"]
                outputDataCSV.append(csv_data)
                continue


        # IF get any error then print error
        except:
            print("------------------------------------------")
            print("[!] ERROR ")
            print("------------------------------------------")
            csv_data = [singleRouter["host"], singleRouter["host"], "GET ERROR"]
            outputDataCSV.append(csv_data)





