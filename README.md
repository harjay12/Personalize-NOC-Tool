This is a tool I created to provide easy logging access to the current company's logging pages.

I am currently working as a NOC rep level I, and when first introduced to the job, I had to mark my presence in a couple of different places.

I first needed to clock in to the company time-management sheet, the Call system we used, and a manager's Google Sheet created by management.

Knowing myself, I know I would miss some of these signs, so I came up with the idea to create one tool I would just need to sign in from that tool, and I would sign myself in any other places I needed to be in, and when signed out.

I decided to use Python to develop the tool; however, with the Python script, I am using AutoHotkey64.exe to interact with the computer keyboard and screen.
Suppose you are not familiar with the AutoHotkey64.exe script. Please learn how it works before using the script from this code.

A few add-ons for the app are the ability to run pings, access a specific link to access the manager router interface, and auto-call the carrier as needed from our Call Center App  

------------------------Package------------------

To access pages that I do not have API access to, I am using Selenium for Web scraping. It is already included in the requirements.txt file.

- Apps with no API and that I am not able to scrape, I am using AutoHotkey to interact with the keyboard and the window screen.
      - The Python package ahk is included in the requirements.txt file, but the actual program still needs to be installed on your pc use the link below:
        link: https://www.autohotkey.com/
- For the user interface, I am using PySide6

  <img width="587" height="525" alt="image" src="https://github.com/user-attachments/assets/abfbe765-4862-4784-9b10-6cff58e158b6" />

  --------------------------------------Project Changes and Visualization---------------------------------------------------
  
  <img width="677" height="546" alt="ToolImg1" src="https://github.com/user-attachments/assets/ed79e654-a837-44da-9237-28dbc59383ba" />

  - Communicate with Google Sheet to make changes as needed:

  <img width="649" height="531" alt="ToolImg2" src="https://github.com/user-attachments/assets/49ae4ded-0906-4db7-86cf-25949b446612" />

  - Ping test Results:

  <img width="643" height="515" alt="ToolImg3" src="https://github.com/user-attachments/assets/2b37d08e-2c09-447f-b470-1fc25118008b" />

  - New Changes For ED Results:
  
  <img width="642" height="522" alt="ToolImg4" src="https://github.com/user-attachments/assets/f7700c09-82c7-4de7-844b-d55a3a283d53" />




