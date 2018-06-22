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
  - Type "python3 getdiskusage.py [path]"
    - where [path] is the location of the disk mount on the local machine
    - the result will be console output in JSON format, the disk usage will also be printed below that.
  
Known bugs:
  - The disk usage is proven to be inaccurate when calculated over small data sets (i.e. < 1GB)

