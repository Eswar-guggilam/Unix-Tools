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

The `cd` command navigates between directories.

```bash
cd /path/to/directory   # Change to a specific directory
cd ..                   # Move up one directory
cd ~ (or) cd            # Change to home directory
cd -                    # Change to previous directory
```

### pwd - Print working directory

The `pwd` command displays the current directory path.

```bash
pwd         # Display the current working directory
```

### Make/Remove directory

```bash
mkdir new_directory     # Create a new directory
mkdir -p path/to/new/directory  # Create nested directories
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

```bash
cp file.txt destination/    # Copy a file to a directory
cp -r source/ destination/  # Copy a directory and its contents
cp *                        # Copy all
cp path/to/dir1 path/to/dir2 # Copy multiple directories
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

### df - Display disk space usage

```bash
df -h                   # Display disk space usage in human-readable format
```

### du - Estimate file and directory space usage

```bash
du -sh directory/       # Display total size of a directory
du -h --max-depth=1 /   # Display size of top-level directories
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

```bash
grep pattern file.txt   # Search for a pattern in a file
grep -r pattern directory/  # Recursively search for a pattern in files of a Directory
grep 'pattern' *.cob    #Search for the pattern in all .cob files
grep 'display.*error' *.cob   #Search for string starts with display & ends with error in .cob files
```

### awk - Pattern scanning and text processing language

```bash
awk '{print $1}' file.cob   # Print the first word/field of each line
```

### General
### 

```bash
history              # Print all commands used in current session
cal                  # Prints the current month callender
date                 # Prints today date, time, day
```

**Note**
> Please suggest new ideas for improving this document. Actively seeking contributions
