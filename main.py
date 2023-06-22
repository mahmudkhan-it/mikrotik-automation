from netmiko import ConnectHandler
import time
import os


# =========================
# ROUTER LIST
# =========================
ROUTERS = []

def ipTOdic(ip,user,password,dicName=ROUTERS):
    a = {
        'device_type': 'mikrotik_routeros',
         'host': str(ip),
         'username': str(user),
         'password': str(password),
         'conn_timeout': 20,
         'auth_timeout': 20,
         'banner_timeout': 20,
    }
    print(a)
    ROUTERS.append(a)



# =========================
# CMD LIST
# =========================

cmdList = []



# =========================
# Main function start
# =========================
outputLog = []
def routerConfig(routers=ROUTERS, CMDS=cmdList):
    print(ROUTERS)
    for singleRouter in routers:
        try:
            print("\n==========================================\n")

            # Check Ping status
            ping = os.system("ping -n 2 " + singleRouter["host"])

            if ping == 0:
                print("[+]Router is Up!")
                # Try to connect with router
                net_connect = ConnectHandler(**singleRouter)
                time.sleep(0.5)

                # Connection done
                print("[+] CONNECT DONE TO ->", singleRouter["host"])

                # Command execute
                for cmd in CMDS:
                    output = net_connect.send_command(cmd)
                    outputLog.append(output)

                print("------------------------------------------")
                print("[+] CONFIGURATION DONE ")
                print("------------------------------------------")
                output = []

            else:
                print("[!]Router is Down")
                continue


        # IF get any error then print error
        except:
            print("------------------------------------------")
            print("[!] ERROR ")
            print("------------------------------------------")



