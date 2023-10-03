import os
import json
import time
from main import checkProxy
from utils import log,log_error_p,log_info,log_success,logo

pathProxies  = os.getcwd()+"/Input/proxy.txt"
pathGoodProxies = os.getcwd()+"/Output/goodProxy.txt"
pathBadProxies = os.getcwd()+"/Output/badProxy.txt"

while True:
    logo("""
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ████████╗███████╗███████╗████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝        ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝         ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║          ██║   ███████╗███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝          ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ BY RAFAL6750
                                                                                                
""")

    log_info("1 | Proxy Tester")
    log_info("2 | Settings")

    option = input("Option: ")
    if option == "1":
        proxyListToCheck = []
        with open(pathProxies,"r") as f:
            for line in f:
                proxyListToCheck.append(str(line).replace("\n",""))

        with open("settings.json",'r') as f:
            jsonLoad = json.load(f)
            websiteUrl = jsonLoad['websiteUrl']

        if len(proxyListToCheck) > 0:
            checkedProxies = checkProxy(websiteUrl,proxyListToCheck)
            goodProxies = checkedProxies[0]
            badProxies = checkedProxies[1]

            if len(goodProxies) > 0:
                with open(pathGoodProxies,"w",encoding="UTF-8") as file:
                    for line in goodProxies:
                        file.write(line)
                log_info(f"Saved {len(goodProxies)}/{len(proxyListToCheck)} working proxies")

            if len(badProxies) > 0:
                with open(pathBadProxies,"w",encoding="UTF-8") as file:
                    for line in badProxies:
                        file.write(line)
                log_info(f"Saved {len(badProxies)} not working proxies")
            
            optionGoBack = input("Press any key to go back: ")
            os.system('cls')
        else:
            log_error_p(f"Fill /Input/proxy.txt")
            optionGoBack = input("Press any key to go back: ")
            os.system('cls')
    if option == "2":
        log_info(f"1 | Paste new websiteURL to test your proxies")
        log_info(f"2 | Go Back")
        optionNew = input("Option: ")
        if optionNew == "1":
            newWebsiteUrl = input("New websiteURL: ")
            with open("settings.json",'r') as f:
                data = json.load(f)
            data['websiteUrl'] = newWebsiteUrl
            with open("settings.json",'w') as f:
                json.dump(data,f,indent=4)
            log_success(f"New websiteURL saved")
            time.sleep(2)
            os.system('cls')
        if optionNew == "2":
            os.system('cls')



