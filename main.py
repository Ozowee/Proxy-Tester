import requests
from time import time
from utils import formatProxy,log_info,log_success,log_error_p

def checkProxy(websiteUrl,proxyList):
    log_info(f"Checking proxies on {websiteUrl}")
    OutputGoodProxy = []
    OutputBadProxy = []
    for proxy in proxyList:
        proxyFormatted = formatProxy(proxy)
        startTime = time()
        request = requests.get(websiteUrl,proxies=proxyFormatted)
        endTime = time()
        responseTime = endTime-startTime
        if request.status_code == 200 or request.status_code == 204:
            OutputGoodProxy.append(f'{proxy}\n')
            log_success(f'IP ADDRESS: {proxy} | Status: OK - [{request.status_code}] | Speed: {round(responseTime,2)}s')
        if request.status_code >= 500 and request.status_code < 600:
            OutputBadProxy.append(f'{proxy}\n')
            log_error_p(f'IP ADDRESS: {proxy} | Status: FAILED - [{request.status_code}]')
        if request.status_code >= 400 and request.status_code < 500:
            OutputBadProxy.append(f'{proxy}\n')
            log_error_p(f'IP ADDRESS: {proxy} | Status: FAILED - [{request.status_code}]')

    return [OutputGoodProxy,OutputBadProxy]

        