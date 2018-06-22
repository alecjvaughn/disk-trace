# target-recruiting
This is the code for the case study #2, written in Python

This program will:
  - Take a mount point as an argument and 
  - Return a list of all the files on the mountpoint and their disk usage in bytes in json format
  - Return the total number of bytes in use

To run this program:
  - Clone the repository with the link: https://github.com/alecjvaughn/target-recruiting.git
  - If Python is not installed on the local machine then download the files here: https://www.python.org/downloads/ and run the installer
  - Open Command-Line for Windows or Terminal for Unix (Macintosh) and navigate to the cloned repository
  - Type "[python_v] getdiskusage.py [path] [debug]" where
    - [python_v] is either "python" or "python3"
    - [path] is the location of the disk mount on the local machine and
    - [debug] is either "1" for ON or "0" for OFF 
    - the result will be console output in JSON format
    - the program will terminate if not a valid disk mount
    - debug mode will clarify whether or not the defined path is a disk mount and also print the disk usage
  
Obstacles:
  - This program took slightly more time than an average project of this size because it is written in an unfamiliar language, though I am much more confident writing code in Python because of this experience
    - I dealt with this obstacle by dividing the program into manageable chucks and doing research on the libraries that would give me the required functionality and how to use them.
    - Research was conducted on the python.org documentation site, Stack Overflow, and other google search results.
  - The json library for Python was very difficult to use at first when trying to conform to the sample document
    - List and dictionary structures where used initially to print the output with json.dump but it was not flexible enough
    - The solution I found was to use a string as a buffer and read data into it while adding the necessary formatting
    - It was necessary to deviate from the sample output because of the stringent requirement of the json library
  - Recursively scanning the directory was challenging at first in conjunction with the json output, until using a string buffer
    - The os.walk() method provided the recursive functionality necessary to scan the directory tree and a simple interface which reduced code significantly

Known bugs:
  - The disk usage is inaccurate when tested over small data sets (i.e. < 1GB)

Future:
  - If choosing to continue development, I would:
    - Seperate directories from files hierarchically
    - Change absolute paths to relative paths
