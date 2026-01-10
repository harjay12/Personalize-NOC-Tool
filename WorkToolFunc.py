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
import platform
import datetime
import subprocess
import gspreadKey
from ahk import AHK
from dotenv import *
from glob import glob
from PySide6.QtCore import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import geocoder

# Find the .env file
dotenv_path = find_dotenv(rf'c:\Users\{os.environ["username"]}\Documents\.env')
load_dotenv(dotenv_path)

# bundle_dir = getattr(
#     sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
# data_path = os.path.abspath(os.path.join(bundle_dir, 'AutoHotkeyV2.exe'))
# print(data_path)


def ahkExe_Path():
    if os.path.exists(r"c:\Program Files\AutoHotkey\v2\AutoHotkey64.exe"):
        return AHK(executable_path=r"c:\Program Files\AutoHotkey\v2\AutoHotkey64.exe")
    else:
        return "Not Found!"


def cca_Path():
    return (
        r"'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Call Center Agent.lnk'"
    )


conductors = {
    "Select a conductor": "",
    "Conductor 1": "https://157.96.244.20/",
    "Conductor 2": "https://157.96.244.70/",
    "Conductor 3": "https://157.96.244.30/",
    "Conductor 4": "https://157.96.244.40/",
    "Conductor 5": "https://157.96.244.41/",
    "Conductor 6": "https://157.96.244.42/",
    "Conductor 7": "https://157.96.244.43/",
    "Conductor 8": "https://157.96.244.44/",
    "Conductor 9": "https://157.96.244.45/",
    "Conductor 10": "https://157.96.244.46/",
    "Applegreen": "https://157.96.244.58/",
}

CarrierPH = {
    "spectrum": "844-350-5679",
    "suddenLink1": "888-822-5151",
    "suddenLink2": "800-490-9604",
    "at&t (opt 2)": "8007323960",
    "cablevision/optimum": "866-575-8000",
    "comcast": "877-881-6544",
    "comcast national": "866-511-6489",
    "cox (opt 4)": "877-225-0005",
    "hargray sparklight1": "8437061850",
    "hargray sparklight2": "877-427-4729",
    "mediacom": "800-379-7412",
    "shentel": "800-743-6835",
    "cableone/sparklight": "877-570-0500",
    "wave": "800-246-2455",
    "bright speed": "8333632907",
    "bright speed t1/pri": "8333632888",
    "bright speed": "833-692-7773",
    "verizon dsac (opt2)": "866-844-3592",
    "gvtc noc": "8554882662",
    "vyve": "8553678983",
    "centurylink": "800-201-4099",
    "midcontinental (midco)": "800-888-1300",
    "windstream": "800-347-1991",
    "ziply": "866-947-5995",
}

UserName = ""
PassWord = ""
LogFail = ""

ADP_Time = "https://online.adp.com/signin/v1/?APPID=EeT&productId=80e309c3-7096-bae1-e053-3505430b5495&returnURL=https://eetd2.adp.com&callingAppId=EeT&TARGET=-SM-https://eetd2.adp.com/122af1p/applications/navigator/htmlnavigator"


def seleniumDiverInit():
    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
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

            CCA_LoggOns(inRes)
            time.sleep(1)

            GoogleSheetIn(inClock=inRes)

            driverIn.switch_to.default_content()
            time.sleep(2)
            driverIn.find_element(
                By.XPATH,
                "/html/body/krn-app/krn-navigator-container/ui-view/krn-header-container/krn-user-info/span/a",
            ).click()

        time.sleep(3)
        driverIn.quit()

        if inRes == "The out punch was accepted.":
            ahkExe_Path().run_script(
                """
                Sleep 15000
                DllCall("user32.dll\LockWorkStation")
                """
            )

    return


def custmInputBox_Func(bxInput=None, inputTitle=None):
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


def CCA_LoggOns(logStatus=None):

    bxInput = {
        "CCA_USERNAME": "Enter your Granite Email ID",
        "CCA_PASSW": "Enter your CCA Password",
        "CCA_PHONE": "Enter your Granite Phone ID",
    }
    custmInputBox_Func(bxInput, "CCA Sign In")

    load_dotenv(dotenv_path, override=True)
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
                    ahkExe_Path().run_script(f"Run '{cca_Path()}'")
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


def ping_host(ip_list=None, nunICMP=None):
    # ip_list = ['8.8.8.8', '1.1.1.1', '192.168.1.1']  # Example IP list

    for ip in ip_list:
        if platform.system() == "Windows":
            # For Windows, use 'start cmd /k' to open a new command prompt
            # and keep it open after the command finishes.
            if nunICMP == "t":
                command = f"start cmd /k ping -t {ip}"
            elif nunICMP is not None:
                command = f"start cmd /k ping -n {nunICMP} {ip}"
            else:
                command = f"start cmd /k ping {ip}"
            # Run "cmd.exe /k ping "
            # ahkExe_Path().run_script(f'Runwait "cmd.exe /k ping {ip}"')
        else:
            command = f'xterm -e "ping {ip}" &'

            # command = f'start cmd /k ping -n {nunICMP} {ip}'
            # For Linux/macOS, use a terminal emulator command like 'xterm -e' or 'gnome-terminal -e'
            # The specific command might vary based on the system's default terminal.
            # This example uses 'xterm'.
            # '&' runs the command in the background

        try:
            subprocess.Popen(command, shell=True)
            print(f"Opened new window to ping: {ip}")
        except Exception as e:
            print(f"Error opening window for {ip}: {e}")


def GoogleSheetIn(inClock=None, shStatus=None, workingStat=None):

    # gc = gspread.service_account(filename=r'c:\Users\harja\OneDrive\Desktop\Python_With_Venv\ClockUp_App\gspread.json')
    # try:
    # myloc = geocoder.ip("me")
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
    # gc = gspread.oauth()
    wb = gc.open_by_key("1fWXYlfnNS71ZPsNqXZ5ZVjSCjASnvgcHKC5idWD3cOA")
    sh = wb.get_worksheet_by_id(101455945)
    cell = sh.find(f"{os.getenv('NOCGSH')}")
    # print('from here',os.getenv('NOCGSH'))
    r = cell.row
    l = cell.col + 1
    l2 = cell.col + 2
    thurs_day = datetime.date.today().strftime("%A")

    if shStatus is not None:
        sh.update_cell(r, l2, f"{shStatus}")

    if inClock == "The in punch was accepted.":
        sh.update_cell(r, l, inOut_office)
        sh.update_cell(r, l2, "In")
        if thurs_day.lower() == "wednesday" and pcUser:
            sh.update_cell(r, l2, "CCA Call Block")

    elif inClock == "The out for break punch was accepted.":
        sh.update_cell(r, l2, "Lunch")

    elif inClock == "The return from break punch was accepted.":
        sh.update_cell(r, l2, "In")
        if thurs_day.lower() == "wednesday" and pcUser:
            sh.update_cell(r, l2, "CCA Call Block")

    elif inClock == "The out punch was accepted.":
        sh.update_cell(r, l, "")
        sh.update_cell(r, l2, "")

    if os.path.exists(file_path):
        os.remove(file_path)
    # except BaseException as err:
    #     if os.path.exists(file_path):
    #         os.remove(file_path)
    #     print(err)


# import subprocess


def is_remotely_used_windows():
    # Run the 'query user' command
    result = subprocess.run(["query", "user"], capture_output=True, text=True)
    output = result.stdout

    # Parse the output
    # The output format is generally: USERNAME SESSIONNAME ID STATE IDLETIME LOGONTIME
    # A local session has SESSIONNAME as 'console'

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


if __name__ == "__main__":
    # CCA_LoggOns()

    print(datetime.date.today().strftime("%A").lower())
    # kill_process()
    # ClockingIn()
    # Example Usage
    GoogleSheetIn(inClock="The in punch was accepted.")
    if is_remotely_used_windows():
        print("The Windows computer might be used remotely.")
    else:
        print("The Windows computer appears to be used locally.")


# You can also use pre-written AHK files more easily
# result_from_file = ahk.run_script_stdout(script_path="my_script.ahk")

# ahk = AHK()
# script_path = os.path.abspath(rf'c:\Users\{os.environ["username"]}\Documents\inputGui.ahk')

# # Run the AHK script and capture the integer return value (exit code)
# # The return_value parameter is for this purpose
# # return_code = ahk.run_script(script_path, blocking=True, return_value=True)
# return_code=ahkExe_Path().run_script(f'{script_path}',blocking=True,)

# print(f"The value from AHK is: {return_code}")

# print(rf'c:\Users\{os.environ["username"]}\Documents')
# GoogleSheetIn(inClock='',shStatus='')
# print(dotenv_path)

# dotEnv_File("XYZ")
# ping_host()
# ip_list = ['8.8.8.8', '1.1.1.1', '192.168.1.1']
# ping_host(ip_list, 3)
# Example usage

# Example usage:

# getMonitorDimensions()
# CCA_LoggOns()
# print(os.getlogin())
# CCA_LoggOns()
# NocStatud()
