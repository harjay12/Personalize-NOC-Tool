"""
https://ahk.readthedocs.io/en/latest/

https://stackoverflow.com/questions/71408434/how-to-make-a-python-exe-file-automatically-install-dependancies

"""

import os
import re
import time
import json
import psutil
import ahkFunc
import gspread
import datetime
import subprocess
import gspreadKey
from ahk import AHK
from dotenv import *
from glob import glob
from PySide6.QtCore import *
from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.chrome.options import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from gspread_formatting import get_data_validation_rule
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException


# Find the .env file
dotenv_path = find_dotenv(rf'c:\Users\{os.environ["username"]}\Documents\.env')
load_dotenv(dotenv_path)
seleCloser = []

# Dict for Selemiun usage collecting tags.
promptPath ={
        'pOkta' : "/html/body/div[2]/div/div/div/div[1]/button[1]",
        'pEmail' : "/html/body/div[2]/div/div/div/form/div[2]/div/div[1]/div/div/input",
        'pPaswd' : "/html/body/div[2]/div/div/div/form/div[2]/div/div[2]/div/div/input",
        'pOktaIn' : "input28",
        'psrchInputs': "/html/body/div[2]/div/div/main/div/div[1]/div/div/form/div/div/div[1]/div/div/div/input",
        'inputNSO': "/html/body/div[2]/div/div/main/div/div[1]/div/div/form/div/div/div[1]/div/div/div/input",
        'nsoSrchBtn': "/html/body/div[2]/div/div/main/div/div[1]/div/div/form/div/div/div[2]/button[2]",
        'nocField': "/html/body/div[2]/div/div/main/div/div[1]/main/div/div/a[4]",
        'configFeild': "/html/body/div[2]/div/div/main/div/div[1]/div[1]/div/div[4]/div/a",
        'stdField': "/html/body/div[2]/div/div/main/div/div[1]/main/div/div/a[1]",
        'lookUpFeild': "/html/body/div[2]/div/div/main/div/div[1]/div[1]/div/div[2]",
        'pnsoInputs':"/html/body/div[2]/div/div/main/div/div[1]/div/div/div[4]/form/div/div/div[1]/div/div/div/input",
        'stdSrchBtn': "/html/body/div[2]/div/div/main/div/div[1]/div/div/div[4]/form/div/div/div[2]/button[2]",
        'nfound':"/html/body/div[2]/div/div/main/div/div[1]/div/div/form/div/div/div[1]/div/div[1]",
    }
logPrompt = {}
pathVa = [0]*10

# Check for AutoHotkey64
def ahkExe_Path():
    if os.path.exists(r"c:\Program Files\AutoHotkey\v2\AutoHotkey64.exe"):
        return AHK(executable_path=r"c:\Program Files\AutoHotkey\v2\AutoHotkey64.exe")
    else:
        return "Not Found!"

# Check for CCA App
def cca_Path():
    return (
        r"'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Call Center Agent.lnk'"
    )


UserName = ""
PassWord = ""
LogFail = ""
gs_NOC = ""

ADP_Time = "https://online.adp.com/signin/v1/?APPID=EeT&productId=80e309c3-7096-bae1-e053-3505430b5495&returnURL=https://eetd2.adp.com&callingAppId=EeT&TARGET=-SM-https://eetd2.adp.com/122af1p/applications/navigator/htmlnavigator"


def seleniumDiverInit():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def dotEnv_File(UserEnvSetup: dict):

    with open(rf'c:\Users\{os.environ["username"]}\Documents\.env', "x") as file:
        print(f"File 'new_file.txt' created successfully.")
    with open(rf'c:\Users\{os.environ["username"]}\Documents\.env', "w") as file:
        for key, value in UserEnvSetup.items():
            file.write(f'{key}="{value}"\n')


def ClockingIn():
    pageStart = ""

    driverIn = seleniumDiverInit()
    driverIn.get(ADP_Time)

    WebDriverWait(driverIn, 30).until(
        EC.presence_of_element_located((By.ID, "login-form_username"))
    )

    try:  # Incase tag does not exist.
        pageStart = driverIn.find_element(
            By.XPATH, '//*[@id="user-remember-checkbox"]'
        ).text

    except NoSuchElementException:
        print("Not found")

    if "Remember user ID" in pageStart:
        driverIn.find_element(By.ID, "login-form_username").send_keys(f"{UserName}")

    checkbox = driverIn.find_element(By.XPATH, '//*[@id="user-remember-checkbox"]')
    if not checkbox.is_selected():
        checkbox.click()
        driverIn.find_element(By.XPATH, '//*[@id="verifUseridBtn"]').click()
        time.sleep(2)
        driverIn.find_element(By.XPATH, '//*[@id="login-form_password"]').send_keys(
            f"{PassWord}"
        )
        driverIn.find_element(By.XPATH, '//*[@id="signBtn"]').click()
        time.sleep(10)
        try:  # Incase tag does not exist.
            global LogFail
            LogFail = driverIn.find_element(
                By.XPATH, '//*[@id="common_alert"]/div'
            ).text
            driverIn.quit()
            return

        except NoSuchElementException:

            iFrame = driverIn.find_element(By.ID, "widgetFrame692")
            driverIn.switch_to.frame(iFrame)

            driverIn.find_element(By.TAG_NAME, "button").click()

            time.sleep(5)

            inRes = driverIn.find_element(
                By.XPATH,
                "/html/body/div[1]/ui-view/krn-timestamp/krn-result-message/div/div/div[2]",
            ).text
            GoogleSheetIn(inClock=inRes)
            time.sleep(1)
            CCA_LoggOns(logStatus=inRes)

            driverIn.switch_to.default_content()
            time.sleep(2)
            driverIn.find_element(
                By.XPATH,
                "/html/body/krn-app/krn-navigator-container/ui-view/krn-header-container/krn-user-info/span/a",
            ).click()

        time.sleep(3)
        driverIn.quit()

        if inRes == "The out punch was accepted.":
            closeSel()

            ahkExe_Path().run_script(
                """
                Sleep 10000
                DllCall("user32.dll\LockWorkStation")
                """
            )

    return


def custmInputBox_Func(bxInput=None, inputTitle=None):
    '''
    With this function we have created a custom user input with AutoHotkey, that would accecpt and dictionary and a string.
    The this dict to display what the user need to input the key get assigned the input val for the .env file.    
    '''
    listInputs = ""
    keyInputs = ""

    for key, value in bxInput.items():
        if os.getenv(key) is None or os.getenv(key) == "":
            listInputs += f"{value},"
            keyInputs += f"{key},"

    listInputs = listInputs[:-1]
    keyInputs = keyInputs[:-1]

    listInputs = listInputs.split(",")
    keyInputs = keyInputs.split(",")

    if not os.path.exists(rf'c:\Users\{os.environ["username"]}\Documents\.env'):
        filvar = "{"
        # os.environ["CCA_USERNAME"] = cca_val.split(',')[0]
        cca_val = ahkFunc.CCA_inputBx(listInputs, inputTitle=inputTitle)

        if len(cca_val) == 0:
            return

        for cnt, value in enumerate(bxInput):
            filvar += f'"{value}":"{cca_val.split(',')[cnt]}",'

        filvar = filvar[:-1]
        filvar += "}"

        filvar = json.loads(filvar)
        dotEnv_File(filvar)
    else:

        if listInputs[0] != "":

            cca_val = ahkFunc.CCA_inputBx(listInputs, inputTitle=inputTitle)
            if len(cca_val) == 0:
                return

            for idx in range(0, len(listInputs)):
                with open(dotenv_path, "a") as f:
                    if os.getenv(key) is None:
                        f.write(f"\n{keyInputs[idx]}='{cca_val.split(',')[idx]}'")
                    else:
                        set_key(
                            dotenv_path,
                            f"{keyInputs[idx]}",
                            f"{cca_val.split(',')[idx]}",
                        )
    load_dotenv(dotenv_path, override=True)
    

def CCA_LoggOns(logStatus=None):
    if logStatus == "The return from break punch was accepted.":
        return

    bxInput = {
        "CCA_USERNAME": "Enter your Granite Email ID",
        "CCA_PASSW": "Enter your CCA Password",
        "CCA_PHONE": "Enter your Granite Phone ID",
    }
    custmInputBox_Func(bxInput, "CCA Sign In")

    # load_dotenv(dotenv_path, override=True)s
    try:
        if os.path.exists(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Call Center Agent.lnk"
        ):
            if ahkFunc.isWin("My Contact Center Agent"):
                ahkFunc.CCA_LogSentIn()

            else:
                if ahkExe_Path().win_exists("ahk_exe CCA.exe"):
                    time.sleep(1)
                    win = ahkExe_Path().active_window
                    if win:
                        if logStatus == "The in punch was accepted.":
                            ahkFunc.CCA_LogSentIn()
                        elif logStatus == "The out for break punch was accepted.":
                            ahkFunc.CCA_LogSentBreak()

                        elif logStatus == "The out punch was accepted.":

                            if ahkExe_Path().win_exists("ahk_exe CCA.exe"):
                                ahkExe_Path().win_close("ahk_exe CCA.exe")
                                win = ahkExe_Path().find_window(title="Confirmation")
                                win.activate()
                                win.send("{Enter}")

                else:
                    ahkExe_Path().run_script(f"Run {cca_Path()}")
                    time.sleep(1)
                    win = ahkExe_Path().active_window
                    if win or logStatus == "The in punch was accepted.":
                        ahkFunc.CCA_LogSentIn()

    except BaseException as e:
        print(e)

    return


def kill_process(old_pid):
    """
    Kills all processes matching the given name.
    Colecting all processes with mathcing name
    """
    procTo_kill = [
        p.info["pid"]
        for p in psutil.process_iter(["pid", "name"])
        if p.info["name"] == "AutoHotkey64.exe"
    ]

    for proc in procTo_kill:
        try:
            if proc != old_pid:
                psutil.Process(proc).kill()
                print(f"Killed process: PID: {proc}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Could not kill process {proc}: {e}")


def GoogleSheetIn(inClock=None, shStatus=None, shCol=None):
    bxInput = {"SHT_KEY": "Enter The NOC Sheet Key", }
    custmInputBox_Func(bxInput, "Add the NOC Google sheet key.")

    global gs_NOC
    inOut_office = "Office"
    pcUser = re.findall(
        r"jsaintaime?",
        os.environ["username"],
        flags=re.IGNORECASE,
    )
    if is_remotely_used_windows():
        inOut_office = "Remote"

    file_path = rf'c:\Users\{os.environ["username"]}\Documents\apiGSpread.json'

    if not os.path.exists(
        rf'c:\Users\{os.environ["username"]}\AppData\Roaming\gspread'
    ):
        if not os.path.exists(file_path):
            gspreadKey.credsFile_Gspread(file_path=file_path)

    gc = gspread.oauth(credentials_filename=file_path)
 
    wb = gc.open_by_key(f"{os.getenv('SHT_KEY')}")

    worksheet = wb.worksheet("Rep Punch Tab")
    if shCol:
        rule = get_data_validation_rule(worksheet, shCol)
        return [
            str(e)[str(e).rfind("=") + 1 : len(str(e))]
            for e in rule.condition.values
            if rule
        ]

    cell = worksheet.find(f"{os.getenv('NOCGSH')}")
    r = cell.row
    l = cell.col + 1
    l2 = cell.col + 2

    if shStatus is not None:
        worksheet.update_cell(r, l2, f"{shStatus}")

    if inClock == "The in punch was accepted.":
        worksheet.update_cell(r, l, inOut_office)
        worksheet.update_cell(r, l2, "In")

    elif inClock == "The out for break punch was accepted.":
        worksheet.update_cell(r, l2, "Lunch")

    elif inClock == "The return from break punch was accepted.":
        worksheet.update_cell(r, l2, "In")

    elif inClock == "The out punch was accepted.":
        worksheet.update_cell(r, l, "")
        worksheet.update_cell(r, l2, "")

    if os.path.exists(file_path):
        os.remove(file_path)

    gs_NOC = worksheet.cell(r, l2).value
    if gs_NOC:
        return gs_NOC


def is_remotely_used_windows():
    """
    Google AI Genarated code to determine is current computer is remote in.
    This code is being use to work with function to update  NOC google spread sheet.
    If is_remotely_used_windows is true I am showing as remot from NOC google spread sheet
    """

    process = QProcess()
    # Start the 'query user' command on Windows
    process.start("cmd.exe", ["/C", "query user"])
    process.waitForFinished()  # Wait for the command to complete

    # Read the output
    output = process.readAllStandardOutput().data().decode("utf-8", errors="ignore")

    for line in output.splitlines():

        if "console" in line and "Active" in line:
            # If the active session is the console session, it might be local use or a remote session connected to the console.
            # A more definitive check is for sessions without 'console' but with an IP address or 'rdp-tcp' in the session name/origin.
            pass  # Keep checking other lines

        if "rdp-tcp" in line or (
            len(line.split()) > 5 and line.split()[-1].replace(".", "").isdigit()
        ):
            # This is a heuristic check: looking for RDP related text or an IP address in the last column
            return True

    return False


# --------------------------------ED Look Up with Selenium----------------------------------
def driver_init():
# 1. Setup Chrome options
    try: 
        bxInput = {"ED_LINK": "Enter your Granite ED Link",
                   "ED_PORT": "Enter your Port to listen to:", }
        custmInputBox_Func(bxInput, "Adding Granite ED Link.")

        chrome_options = Options()
        service = Service()
        chrome_options.add_argument("--headless=new") # Required for headless mode
        chrome_options.add_argument("--disable-gpu")    # Recommended for some systems
        port = portListner(f"{os.getenv('ED_PORT')}")
        print(port)
        inneDriver =''
        
        if not port:
            print("adding port")
            chrome_options.add_experimental_option("detach", True)
            chrome_options.add_argument(f"--remote-debugging-port={os.getenv('ED_PORT')}")
            inneDriver = webdriver.Chrome(service=service,options=chrome_options)
            inneDriver.get(f"{os.getenv('ED_LINK')}")
        else:
            print("running on port")
            chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{os.getenv('ED_PORT')}")
            inneDriver = webdriver.Chrome(service=service,options=chrome_options)

        seleCloser.append(inneDriver)
        return inneDriver 
    
    except WebDriverException as err:
        return err


def portListner(port):
    try:
        cmd = f'netstat -ano | findstr ":{port}"' # Windows version
        output = subprocess.check_output(cmd, shell=True).decode()
        return(f"LISTENING" in output or f"ESTABLISHED" in output)
    except subprocess.CalledProcessError:
        return False
    

def edInit_(driver):

    # Mian try process to catch errors.
    try: 
 
        # All the try process bellow are checking if we are at a certain part or tag of the page to determine how to proceed.
        try: 
            logPrompt.update(
                {"okta": driver.find_element(By.XPATH, f"{promptPath['pOkta']}")
                })
            pathVa[0] = logPrompt['okta'].text
        except NoSuchElementException:
            pathVa[0] = "Not found"

        try:
            logPrompt.update({
            "email": driver.find_element(By.XPATH, f"{promptPath['pEmail']}")})
            pathVa[1] = "Email In"
        except NoSuchElementException:
            pathVa[1] = "Not found"
        
        try:
            logPrompt.update({
            "paswd": driver.find_element(By.XPATH, f"{promptPath['pPaswd']}")})
            pathVa[2] = "Password In"

        except NoSuchElementException:
            pathVa[2] = "Not found"

        if "Sign in with OKTA" in pathVa[0]:
            print(logPrompt['okta'].text)
            logPrompt['okta'].click()
        elif "Email In" in pathVa[1]:
            logPrompt['email'].send_keys(os.getenv("CCA_USERNAME"))
            logPrompt['paswd'].send_keys(os.getenv("CON_PASSW"))
        
        time.sleep(3)
        try:
            logPrompt.update({
            "oktaSgn": driver.find_element(By.ID, f"{promptPath['pOktaIn']}")})
            pathVa[3] = 'Okta In'
        except NoSuchElementException:
            pathVa[3] = "Not found"

        if "Okta In" in pathVa[3]:
            print('empty here',logPrompt['oktaSgn'].text)
            logPrompt['oktaSgn'].send_keys(os.getenv("COND_USERNAME"))
            driver.find_element(By.XPATH,'//*[@id="form20"]/div[2]/input').click()
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID,'input61'))).send_keys(os.getenv("CON_PASSW"))
            driver.find_element(By.XPATH,'//*[@id="form53"]/div[2]/input').click()

    except WebDriverException as err:
        print(err)

    

def edConfig_Srch(nsoidInput=None):
    InputTup = ('nocField','configFeild', 'inputNSO','nsoSrchBtn',nsoidInput)
    
    driver = driver_init()
    try:
        if driver.msg:
            return  "Unable to load the page. You need to Sign in to Granite VPN to access this page."
    except BaseException:
        pass
    
    time.sleep(3)
    edInit_(driver)
    time.sleep(2)
    # Mian try process to catch errors.
    try:
        # All the try process bellow are checking if we are at a certain part of the page to determine how to proceed.
        try: 
            driver.find_element(By.XPATH, f'{promptPath['pnsoInputs']}')
            driver.find_element(By.XPATH,'/html/body/div[2]/header/div/div/a').click()
        except NoSuchElementException:
            pass
        
        try:
            driver.find_element(By.XPATH, f'{promptPath['psrchInputs']}')
        except NoSuchElementException:
            WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH,f"{promptPath['nocField']}"))).click()
            
            WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH,f"{promptPath['configFeild']}"))).click()

        WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,  f"{promptPath['inputNSO']}"))).clear()
        
        driver.find_element(By.XPATH,f"{promptPath['inputNSO']}").send_keys(nsoidInput)
        driver.find_element(By.XPATH,f"{promptPath['nsoSrchBtn']}").click()

        oktaCheck(driver,InputTup)

        return WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="output"]/div[2]/div'))).text
            
    except BaseException as err:
        return 'ERROR: Something went wrong!'
      


def NSOLook(nsoidInput=None):
    
    InputTup = ('stdField','lookUpFeild', 'pnsoInputs','stdSrchBtn',nsoidInput)
    driver = driver_init()

    try:
        if driver.msg:
            return  "Unable to load the page. You need to Sign in to Granite VPN to access this page."
    except BaseException:
        pass

    time.sleep(3)
    edInit_(driver)
    time.sleep(2)
    # Mian try process to catch errors.
    try:
        # All the try process bellow are checking if we are at a certain part of the page to determine how to proceed.
        try:
            driver.find_element(By.XPATH, f'{promptPath['psrchInputs']}')
            driver.find_element(By.XPATH,'/html/body/div[2]/header/div/div/a').click()
        except NoSuchElementException:
            pass

        try:
            driver.find_element(By.XPATH, f'{promptPath['pnsoInputs']}')
        except NoSuchElementException:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH,f"{promptPath['stdField']}"))).click()
                
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH,f"{promptPath['lookUpFeild']}"))).click()
            
        WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH,  f"{promptPath['pnsoInputs']}"))).clear()
        driver.find_element(By.XPATH, f'{promptPath['pnsoInputs']}').send_keys(nsoidInput)
        driver.find_element(By.XPATH,f"{promptPath['stdSrchBtn']}").click()

        oktaCheck(driver,InputTup)
       
        return WebDriverWait(driver, 30).until(
                            EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/main/div/div[1]/div/div/div[4]/div[2]'))).text
    
    except BaseException as err:
        return "ERROR: Something went wrong!\nPossibly this is an OffNet Circuit check the WAN IP."

    
def oktaCheck(driver,nsoidInput=None):
    try:  # Incase tag does not exist.
        a,b,c,d,e = nsoidInput
 
        time.sleep(1.5)
        driver.find_element(By.XPATH, f"{promptPath['pOkta']}").click()
        WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,f"{promptPath[str(a)]}"))).click()
        WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,f"{promptPath[str(b)]}"))).click()
        print('Okta test pass here!')
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH,  f"{promptPath[str(c)]}"))).clear()
        driver.find_element(By.XPATH, f'{promptPath[str(c)]}').send_keys(str(e))
        driver.find_element(By.XPATH,f"{promptPath[str(d)]}").click()
        
    except NoSuchElementException:
        return False
    

def closeSel():
    if len(seleCloser) != 0:
        print(("Yes"))
        seleCloser[0].close()
        seleCloser[0].quit()
    Stop_portListener()


def Stop_portListener():
    try: #if port does not exist it will create one.
        cmd = f'netstat -ano | findstr ":{9561}"' # Windows version
        output = subprocess.check_output(cmd, shell=True).decode()
        if (f"LISTENING" in output or f"ESTABLISHED" in output):
            pidTokill = re.search(r'(LISTENING\s*\d+)',str(output))
            pidTokill = "".join(re.findall(r'\d+',pidTokill.group(0))) 
            print(pidTokill) 
        
            psutil.Process(int(pidTokill)).kill()
    except subprocess.CalledProcessError:
        return False


def nsoTableFormat(dict_listVal=None):
    # Formatting the result into somewhat of a table display.
    res = ''
    for key, val in dict_listVal.items():
        res =   res +"\n" +  f"\n{key:<10}\n"
        res = res +  ("-" * 60) 
        for row in val:
            res = res +  (f"\n\t{row[0]:<20} \t{row[1]:<10}")
    return res
    
    
def stdrdNSO_srchFormatter(nsoStr=None):
    
    tempArr = []
    formatToDicy ={}

    if 'ERROR: ' in nsoStr:
        return nsoStr
    
    '''
    - Manupilate the result by first locate the word Details to form the hearder of the table. 
    - We then isolate the remainder of the results are added into a sub-array with only 2 ithems.
    '''
    nsoStr  =  nsoStr.strip().split('\n')
    for header in nsoStr:
        if 'Details' in header:
            tempArr.append(header)
        
    for cnt in range(0, len(tempArr)-1):
 
        if tempArr[cnt] in nsoStr:
            start = nsoStr.index(tempArr[cnt])
            end = nsoStr.index(tempArr[cnt+1])
            pairs = [nsoStr[start+1 : end][i:i+2] for i in range(0, len(nsoStr[start+1 : end]), 2)]

            formatToDicy.update({tempArr[cnt]: pairs})
            if end == nsoStr.index(tempArr[len(tempArr)-1]):
                pairs = [nsoStr[end+1:][i:i+2] for i in range(0, len(nsoStr[end+1]), 2)]
                formatToDicy.update({tempArr[len(tempArr)-1]: pairs})

    dictTable_Res = nsoTableFormat(formatToDicy)
    return dictTable_Res


if __name__ == "__main__":
 
    print(datetime.date.today().strftime("%A").lower())
    GoogleSheetIn()
    if is_remotely_used_windows():
        print("The Windows computer might be used remotely.")
    else:
        print("The Windows computer appears to be used locally.")
