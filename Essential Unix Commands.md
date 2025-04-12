## 🐧 UNIX
[![LinkedIn](https://img.shields.io/badge/linkedin-Eswar%20Guggilam%20linkedIn-blue)](https://www.linkedin.com/in/eswar-guggilam-tv/)


This document overviews essential Unix commands for file, directory, system, and network management. It assumes a basic understanding of Unix and shell environments. Each command is presented with common usage examples to assist in daily operations, especially in a developer or administrative context.

> This document is prepared by considering you have a basic understanding of UNIX and shell.

## 1. File and Directory Operations

### ls - List directory contents

The `ls` command is used to list the contents of directories. It can display detailed information and control results with various options.

```bash
ls          # List files and directories in the current directory
ls -l       # List in long format, showing permissions, owner, size, etc.
ls -a       # List all files, including hidden ones (starting with .)
ls -lh      # List in long format with human-readable file sizes
ls -t       # Sort by newest first
ls -r       # Sorts in revers order
ls -s       # Sort by size
ls -x       # Sort by extention
ls -lrt     # Long list with newest last
ls -lrt *.cob # Long list .cob files with newest last 
ls *sam*      # List file that contain "sam" in the name
```

### cd - Change directory

The `cd` (Change Directory) command navigates the filesystem hierarchy in Unix/Linux systems.

```bash
cd /path/to/directory   # Change to a specific directory
cd ..                   # Move up one directory
cd ../..                # Go back 2 directories
cd ../../..             # Go back 3 directories
cd ~ (or) cd            # Change to home directory
cd -                    # Change to previous directory
```


### Create/Remove directory -mkdir
The `mkdir` (Make Directory) command is used to create new directories in Unix/Linux systems.

```bash
mkdir new_directory     # Create a new directory
mkdir dir1 dir2 dir3    # Create multiple directories.
mkdir -p path/to/new/directory  # Create nested directories
mkdir -p project/{src,docs,tests}/{lib,bin,data}    # Create complete directory structure

# Create directory with specific permissions
mkdir -m 755 directory  # rwxr-xr-x
mkdir -m 700 private    # rwx------
mkdir -m 777 public     # rwxrwxrwx

# Remove Direcotries
rmdir directory        # To remove existing directory
rmdir path/to/directory # To remove directory using path 
```

### rm - Remove files or directories

```bash
rm file.txt             # Remove a file
rm -r directory         # Remove a directory and its contents
rm -f file.txt          # Force remove without prompting
rm *                    # To remove all the files in the directory
rm -f *                 # To remove all the directories
```

### cp - Copy files or directories
The `cp` (Copy) command is used to copy files and directories in Unix/Linux systems.

```bash
cp file.txt destination/    # Copy a file to a directory
cp -r source/ destination/  # Copy a directory and its contents
cp *.COB /home              # Copy all .COB files to home directory
cp file[1-3].txt destination/  # Copy file1, file2, file3
cp path/to/dir1 path/to/dir2 # Copy multiple directories

# backup/update
cp -u source.txt destination/  # Copy only if source is newer
cp -b file.txt destination/  # Create backup of existing files

```

### mv - Move or rename files or directories

```bash
mv file.txt new_name.txt    # Rename a file
mv file.txt /new/location/  # Move a file to a new location
```

## 2. File Viewing and Editing

### touch - Create files

```bash
touch    file.txt file2.txt    # Creates files
touch    file{1..2}           # To create file1,file2 
```

### cat - Concatenate and display file contents

```bash
cat file.txt            # Display contents of a file
tac file.txt            # Display contents of a file in revers
cat -n file.txt file2.txt # Display with numbered sequence
cat file1.txt file2.txt # Display contents of multiple files
cat file*               # Display contents of files matching the filter
cat >file1              # To insert or overwrite the data
cat >>file1.txt         # To append the data
```

### less - View file contents page by page

```bash
less file.txt           # View file contents with scrolling and search
```

### head - Display the beginning of a file

```bash
head file.txt           # Display first 10 lines of a file
head -n 20 file.txt     # Display first 20 lines of a file
```

### tail - Display the end of a file

```bash
tail file.txt           # Display last 10 lines of a file
tail -n 20 file.txt     # Display last 20 lines of a file
tail -f file.txt        # Follow the file in real-time (useful for logs)
```

### nano - Simple text editor

```bash
nano file.txt           # Open or create a file for editing
```

## 3. File Permissions

### chmod - Change file permissions
|Representation|Definition||Representation|Definition||Representation|Definition|
|--------------|----------|-|--------------|----------|-|--------------|------------------------------|
|u:|User||r:|Read Permission||+:| To add permissions to file|
|g:|Group||w:|Write Permission||-:| To remove permissions of file|
|o:|Others||x:|Exicutable Permission||=:| To assign permissions to file|



```bash
chmod 755 file.txt      # Change permissions using octal notation
chmod u+x file.txt      # Add execute permission for the owner
chmod go-w file.txt     # Remove write permission for group and others
```

### chown - Change file owner and group

```bash
chown user:group file.txt   # Change owner and group of a file
chown -R user:group directory/  # Recursively change ownership
```

## 4. System Information

### uname - Print system information

```bash
uname -a                # Display all system information
uname -s                # Display kernel name
uname -r                # Display kernel release
```

### Disk Usage Commands

```bash
df -h                   # Display disk space usage in human-readable format

du -sh directory/       # Display total size of a directory
du -h --max-depth=1 /   # Display size of top-level directories

du -h --max-depth=1 | sort -hr  # Find largest directories in current location

lsof | grep python  # Check which open python files are using disk space

fdisk -l # Disk Partitioning Information

```

### top - Display and update sorted information about processes

```bash
top             # Display real-time system statistics and running processes
```

## 5. Network Commands

### ping - Send ICMP ECHO_REQUEST to network hosts

```bash
ping google.com         # Ping a host to check network connectivity
```

### ifconfig - Configure network interface parameters

```bash
ifconfig                # Display network interface configuration
```

## 7. Text Processing

### grep - Search for patterns in files
#### Common Options
|Option |Description |
|--------|-------------------|
|-i|Case-insensitive search|
|-v|Invert match (show non-matching lines)|
|-r, -R|Recursive search in directories|
|-l|Show only filenames with matches|
|-n|Show line numbers|
|-c|Count matching lines|
|-w|Match whole words only|
|-A n|Show n lines after match|
|-B n|Show n lines before match|
|-C n|Show n lines before and after match|
|-E|Extended regular expressions (same as egrep)|
|--color|Highlight matching text|

```bash
grep pattern file.txt   # Search for a pattern in a file.txt
grep -i "error" logfile.txt   # Case-insensitive search
grep -r pattern directory/  # Recursively search for a pattern in files of a Directory
grep 'pattern' *.cob    #Search for the pattern in all .cob files
grep 'display.*error' *.cob   #Search for string starts with display & ends with error in .cob files

# Multiple Patterns

grep -E "error|warning" file.txt    # Match multiple patterns (OR)
grep "error" file.txt | grep "warning"    # Match all patterns (AND)

# Controll lines

grep -A 3 "error" logfile.txt    # Show 3 lines after match
grep -B 3 "error" logfile.txt    # Show 3 lines before match
grep -C 3 "error" logfile.txt    # Show 3 lines before and after match

# Line Numbers and Count

grep -n "error" logfile.txt    # Show line numbers with matches
grep -c "error" logfile.txt    # Count number of matches

# Advanced

grep "error.*" file.txt    # Match words starting with 'error'
grep -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" file.txt    # Match email addresses
grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" file.txt    # Match IP addresses
history | grep "secompilecob"    # Search command history for secompilecob
ps aux | grep "nginx"    # Search currently processing list



```
### Find
The `find` command is a powerful Unix/Linux utility for searching files and directories in a hierarchy.
```bash
find  -name "example.txt"  # Find files named exactly "example.txt" in all paths
find  -name "*.pdf"	#Using *
find  -type d		# Find directories
find  -type f		# Find regular files
find  -type l		# Find symbolic links

# Search by time

find  -mtime -1		# Files modified less than 24 hours ago
find  -atime +7		# Files accessed more than 7 days ago
find  -cmin -30		# Files changed within last 30 minutes

# Search by size

find  -size +100M	# Files larger than 100MB
find  -size -1k		# Files smaller than 1KB
find  -size 20M		# Files exactly 20MB
find  -name "*.pdf" -size +1M		# AND condition
find  -name "*.jpg" -o -name "*.png"	# OR condition
find  -not -name "*.txt"		# NOT condition
```


### awk - Pattern scanning and text processing language

```bash
awk '{print $1}' file.cob   # Print the first word/field of each line
```

### General
### 

```bash
pwd                  # Display the current working directory
history              # Print all commands used in current session
cal                  # Prints the current month callender
date                 # Prints today date, time, day
top                  # Monitor system processes in real me.
kill                 # Terminate a process by ID (PID in ps command)
killall firefox      # Kills all "firefox" processes.
ifconfig             # Shows network interfaces.
whoami               # Display the current logged-in user.

```
### Process Status PS:

The `ps` (Process Status) command provides information about active processes on a Unix/Linux system.

```bash
ps     # Current terminal processes
ps aux    # All processes
ps -ef    # Detailed process list

ps aux | grep debug    # Find specific process
ps -C command_name           # Find processes by command

ps -eo pid,user,cpu,memory,command      # Custom columns
ps aux --sort=-pcpu                   # Sort by CPU usage
ps aux --sort=-pmem                 # Sort by memory usage

ps -ejH                  # Show process hierarchy
pstree                  # Alternate tree view
ps axjf                # Compact tree view

pidstat               # cpu usage per pid
pidstat 2             # Monitors every 2 seconds

topas       # AIX system monitoring tool
nmon        # AIX performance monitor

```

### nohup (No Hang Up):

allows processes to continue running even after the user who started them logs out or the terminal session closes.

```bash
nohup command [arguments] [&]
# command: The command you want to run
# arguments: Optional arguments for the command
# &: Optional symbol to run the process in the background

nohup python3 long_script.py > custom_output.log  
# Exicutes python script & stores logs to custom_output.log, all in background(&)
# If not provide custom_output, By default, nohup redirects output to nohup.out in the current directory

ps -ef | grep $(whoami) | grep command
# To get nohup processid

kill -9 [PID]
# kill the nohup process
```

### Alias
- The `alias` command allows users to create shortcuts or abbreviations for longer commands and is commonly used to customize the command-line environment.
- Therefore, you can use alias variables instead complex commands

```bash
alias name='command'    # Create alias
alias                   # List aliases
unalias name            # Remove alias

# Creating a new alias

alias lsrt='ls -lrt'    # Alias of lsrt
alias c='clear'         # alias for Clear screen 'c'
alias ..='cd ..'        # Go up one directory '..'

```

**Note**
> Please suggest new ideas for improving this document. Actively seeking contributions
