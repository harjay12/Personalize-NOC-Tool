import WorkToolFunc
import os


def CCA_inputBx(inputLabels=None, inputTitle=None):

    input_result = WorkToolFunc.ahkExe_Path().run_script(
        f"""
                    #Requires AutoHotkey v2.0
                    #SingleInstance Force   

                    inLabels := {inputLabels}

                    ccaInputBx := Gui(, "{inputTitle}") ; Create the GUI window
                    loop inLabels.Length {{
                        ccaInputBx.Add("Text", "Section vMyText" A_Index "", "*" inLabels[A_Index] ":")

                        if InStr(inLabels[A_Index], 'Password'){{
                            ccaInputBx.Add("Edit", "vUser" A_Index " w283 h23 Password", "")

                        }}else{{
                            ccaInputBx.Add("Edit", "vUser" A_Index " w283 h23 ", "")

                        }}
                    }}
                    ccaInputBx.AddButton("Default yp+30", "Submit").OnEvent("Click", Submission) ; Add a submit button
                    ccaInputBx.SetFont('s11')
                    ccaInputBx.Add("Text", "Section x+10 vReq hidden  cRed",
                                   "All fields are required, can't be empty.")
                    ccaInputBx.Show()

                    Submission(*) {{
                        values := ccaInputBx.Submit(false) ; Get all named controls' values
                        my_value := ''

                        loop inLabels.Length {{
                            if (A_Index > 1) {{
                                my_value .= ','
                            }}

                        my_value .= ccaInputBx['User' . A_Index].Value

                        if (ccaInputBx['User' . A_Index].Value == '') {{
                            ccaInputBx["MyText" . A_Index].Opt("cRed")
                            ccaInputBx["Req"].Visible := true
                            SetTimer(HideText, -3500)

                            if ((A_Index == inLabels.Length)
                                && (ccaInputBx['User' . A_Index].Value == '')) {{
                                return

                            }} else if (ccaInputBx['User' . inLabels.Length].Value != '') {{

                                ccaInputBx["MyText" . inLabels.Length].Opt(
                                    "cBlack")
                                loop (inLabels.Length - 1) {{
                                    if (ccaInputBx['User' . A_Index].Value == '') {{
                                        ccaInputBx["MyText" . A_Index].Opt(
                                            "cRed")
                                }} else {{
                                        ccaInputBx["MyText" . A_Index].Opt(
                                            "cBlack")
                                    }}
                            }}

                            return
                        }}

                        }} else {{
                            ccaInputBx["MyText" . A_Index].Opt("cBlack")

                        }}

                    }}

                    FileAppend my_value . "`n", "*"
                    ccaInputBx.Destroy() ; Close the window after submission
            }}

            HideText(*) {{
                ccaInputBx["Req"].Visible:= false
            }}

    """
    )

    # You can run an AHK script string and capture output

    return input_result.replace("\n", "")


def CCA_LogSentIn():
    WorkToolFunc.ahkExe_Path().run_script(
        f"""
        #Requires AutoHotkey v2.0
        #SingleInstance Force

        try{{
                                      
            if('{winFound("My Contact Center Agent")}'=='Found!'){{
                WinActivate('My Contact Center Agent')                            
                Sleep 500
                Click(256, 125, count:=2) ;
                send "^c"
                ClipWait
                Sleep 500
                                                
                if (A_Clipboard == "") {{
                    send  "{os.getenv('CCA_USERNAME')}"
                }}
                    send "{{tab}}"
                    Sleep 500
                    send "{os.getenv('CCA_PASSW')}"
                    send "{{tab 2}}"
                    Sleep 500
                    send "^c"
                    ClipWait
                    Sleep 500
                    if (A_Clipboard == "") {{
                        send "{os.getenv('CCA_PHONE')}"
                    }}
                    send "{{tab}}"
                    send "{{Enter}}"
                    Sleep 500
                    WinActive("My Contact Center Agent - Not Ready")
                    Sleep 300
                    if  A_ScreenWidth >= 1920 && MonitorGetCount() > 1{{
                        WinMove 3420,  820, 425, 210, "A"  
                    }}
            }}


        }} catch Error as e{{
        
        ;Display detailed information about the error
        MsgBox(Format("Error Details:`nMessage: {{}}`nFile: {{}}`nLine: {{}}`nWhat: {{}}`nStack: {{}}"
        , e.Message, e.File, e.Line, e.What, e.Stack))
        
        }}

    """
    )


def CCA_LogSentBreak():
    WorkToolFunc.ahkExe_Path().run_script(
        f""" 
                                                
            #Requires AutoHotkey v2.0
            #SingleInstance Force

            winList:= {{
                128:"My Contact Center Agent - Not Ready",
                120:"My Contact Center Agent - Available",
                220:"My Contact Center Agent - Calling LEC outside CCA", 
                127:"My Contact Center Agent - Supervisor",
                118:"My Contact Center Agent - Training",
                190:"My Contact Center Agent - Busy - Wrapping Up",
                219:"My Contact Center Agent - Busy - After Call Work"
            }}
            Sleep(500)
            
            for k, v in winList.OwnProps(){{

                if activateNeededWin(v){{
                    WinMove 2234, 291, 560, 533, v
                    Click k, 70 ;
                    Sleep(500)
                    Click 121, 400 ;
                    Sleep(500)
                    Click 308, 505 ;
                    Sleep(800)
                    
                    if  A_ScreenWidth >= 1920 && MonitorGetCount() > 1{{
                        WinMove 3420,  820, 425, 210, "A"  
                    return
                    }}

                }}
            }}
                                                
            activateNeededWin(neededWin) {{
                ids := WinGetList(, , "Program Manager")
                needWin := ""
                for this_id in ids {{
                    
                    if (WinGetTitle(this_id) = neededWin) {{
                        WinActivate this_id
                        needWin := WinGetTitle(this_id)
                        break
                    }}

                }}
                return needWin
            }}

    """
    )


def isWin(neededWin):

    curentWin = WorkToolFunc.ahkExe_Path().run_script(
        f""" 
                                                      
        #Requires AutoHotkey v2.0
        #SingleInstance Force

        ids := WinGetList(, , "Program Manager")
        needWin := ""
        for this_id in ids {{
            
            if (WinGetTitle(this_id) = "{neededWin}") {{
                WinActivate this_id
                needWin := WinGetTitle(this_id)
                break
            }}

        }}
        FileAppend needWin . "`n", "*"

    """
    )
    return curentWin.replace("\n", "")


def winFound(TargetedWin):

    curentWin = WorkToolFunc.ahkExe_Path().run_script(
        f""" 
                                                      
    #Requires AutoHotkey v2.0
    #SingleInstance Force
        
    itemFind := ''                                                   
    winTere := true
    rnCnt := 500
    while (winTere) {{
        sleep rnCnt
        if (WinActive("{TargetedWin}")) {{
            itemFind := 'Found!'
            break
        }}
        if (rnCnt == 2000) {{
            MsgBox("Timed out Please try again.")
            return
        }}
        rnCnt := rnCnt + 500
    }}
    FileAppend itemFind . "`n", "*"
    """
    )
    return curentWin.replace("\n", "")


def runCund(userN=None, condPassW=None):

    WorkToolFunc.ahkExe_Path().run_script(
        f""" 
                                          
        #Requires AutoHotkey v2.0
        #SingleInstance Force
        if(A_Clipboard==''){{
            A_Clipboard := 'Place Older'                    
        }}
     
        ogVal := A_Clipboard
        winTere := true
        rnCnt := 500
        timeOut:= 2000
 
        if (WinActive("Privacy error - Google Chrome")) {{
            Click(589, 645)
            Sleep(200)
            Click(629, 795)
            timeOut:=3500
        }}
            
        while (winTere) {{
            WinActive("Sign In | EET - Google Chrome")
            Click(1289, 420, Count := 3)
            send "^c"
            ClipWait
            Sleep 500
            CleanedString := StrReplace(A_Clipboard, "`r`n", "")
            sleep rnCnt
            if (CleanedString == 'Welcome') {{
            
                Send('{{Tab}}')
                Sleep 100
                send "{userN}"
                Sleep 100
                Send "{{tab}}"
                Sleep 100
                Send "{condPassW}"
                Sleep 100
                send "{{Enter}}"
                break
            }}
            if (rnCnt == timeOut) {{
                MsgBox("Timed out Please try again.")
                return
            }}
            rnCnt := rnCnt + 500
        }}
         
        A_Clipboard := ogVal
        
    """
    )


def CCA_Calls(PHnum=None):
    WorkToolFunc.ahkExe_Path().run_script(
        f""" 
            if WinExist("ahk_exe CCA.exe"){{
                if  A_ScreenWidth >=1920 && MonitorGetCount()>1{{
                    WinMove 3380,  820, 460, 210, WinGetTitle() 
                }}
                Sleep 500
                WinActivate(WinGetTitle())
                sleep 500
                ;Click(350, 69)
                send('^d')
                sleep 500
                Send "{PHnum}"
                sleep 850
                Send "{{Tab 4}}"
                Send "{{enter}}" 
            }}
        """
    )


if __name__ == "__main__":
    # print(isWin('ahkFunc.py - Python_With_Venv - Visual Studio Code'))
    CCA_LogSentBreak()
    # CCA_LogSentIn()
    # runCund('userN',)
    # CCA_inputBx()
    # CCA_inputBx(inputLabels=['df', 'rt'], inputTitle='None')
