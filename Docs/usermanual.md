## User Manual

### Introduction
The following document has the purpose of guiding the end-user through download, installation, and use of the SSN validation software. It will include clear instructions of how to perform the procceses previously mentioned in an understandably way.

### Before starting

In order to use the application, you should have Python 3.7.8 installed on your machine. To do so,do the following:
#### If you are on windows...
 Go to https://www.python.org/, click on "**Downloads**". Then, on the "**Looking for a specific release?**" section, scroll till you find the 3.7.8 release version (you can also use your browsers page search function and look for 3.7.8), then click on "Download". Scroll down to the "**Files**" section, and click "Windows x86-64 executable installer". When the download finishes, open the installer and follow the instructions carefully. After you finish, open a command line window (hit windows key, then write cmd then enter) and write "python", then hit enter. You should see "Python 3.7.8..." on your screen if it was correctly installed.
#### If you are on linux...
You should first open the terminal and write "python3", to check if python is included with your distro. You should see "Python X.X.X..." on your screen if it is installed. If not, write the following command on the terminal: 
    sudo apt-get install python3
This was tested using Ubuntu 22.04 LTS. Please refer to the following documentation: https://docs.python-guide.org/starting/install3/linux/ if you need more information.


### Download source files
Go to https://github.com/DefinitelyJuan/SSNValidation and click the green button which says "**Code**". Then, on the drop down menu, click over the "**Download ZIP**" option. The app's zip will automatically start to download, and when it finishes, you must go to where the file was saved, right click on it, and select "**Extract to SSNValidation-master\\**". The application files will be extracted to a folder with that name on the same folder that the rar was in. If you go into the SSNValidation-master folder, you should see elements as a file named "**README.md**" and a folder called "**Docs**".

### Using the application

Inside the SSNValidation-master folder, open the terminal and write the following command: 

    python3 SSN.py

 You will be prompted to enter an SSN number. After you do so, press enter. The program will validate if what you entered is valid, and then it will tell you through command-line the result of the validation process.
