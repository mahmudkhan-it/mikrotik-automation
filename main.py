from netmiko import ConnectHandler
import time
import os
dev_name = "Dev by Mahmud Khan & idea by MR. Pavel"
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


banner =(" ______  _ _                     _ _                                                _             \n"
         "|  ___ \(_) |               _   (_) |         /\         _                     _   (_)            \n"
         "| | _ | |_| |  _  ____ ___ | |_  _| |  _     /  \  _   _| |_  ___  ____   ____| |_  _  ___  ____  \n"
         "| || || | | | / )/ ___) _ \|  _)| | | / )   / /\ \| | | |  _)/ _ \|    \ / _  |  _)| |/ _ \|  _ \ \n"
         "| || || | | |< (| |  | |_| | |__| | |< (   | |__| | |_| | |_| |_| | | | ( ( | | |__| | |_| | | | |\n"
         "|_||_||_|_|_| \_)_|   \___/ \___)_|_| \_)  |______|\____|\___)___/|_|_|_|\_||m|\ahm)u|\d_k/|h|a|n|\n"
         "                                                                                                  \n"
         )
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
            print("[+] CONFIGURING => ", singleRouter["host"])
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





