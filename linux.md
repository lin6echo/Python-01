
`sudo -su -`\
`sudo -s`\
`su -`\
`cd /` - root

---

`uptime`\
`hostname`\
`uname` --> `uname -a`\
`ps ... ps -fu .... ps -f ... ps -ef .... ps awx ... ps u`\
`top`\
`kill -PID`\
`kill -9` (No Question)\
`ls -l .... ls -ltr`\
`whoami`\
`wim` -- > exit :wq!\
`mkdir`\
`| pipe `\
`ls -ltr | more` (lapozás - space)\
d -directory, l -link, - -file\
rwx - read, write, execute\
ugo - user, group, other

---

chown "new-user" file\
chgrp "new-group" file\
`chmod g+w file` (group enable write permission)\
`chmod a+r file` (all enable read permission)\
`chmod u+w file` (user enable write permission)

---

`rm `- remove

text
`echo "something" > filename `\
`echo "something" >> filename ` - append\
`touch` - create a file

`whatis command`\
`command --help`\
`command man`

---
<h3>Maintenance Commands</h3>

`cp` - copy\
`rm` - remove\
`mv` - move\
`mkdir` - make directory\
`rmdir` or `rm -r` ---- remove directory\
`chgrp` - \
`chown` - \
`rm - Rf` - force full remove\
`chown root:root file`

---

<h3>Filters/Text Processors Commands</h3>

- `out`
- `awk`
- `grep`
- `sort`
- `uniq`
- `wc` (word count)

`cut -c1 filename` (give you back first letters)\
`awk` separate each columns\
`awk '(print $1)' filename` (first column)\
`grep` ---- search grep mit miben\
`sort` - sorba rendezés\
`sort filename`\
`sort -r` fordított sorrend\
`uniq`  - removes all \
`sort | uniq` együtt \
`wc` - word count\
`wc filename` (-l, lines)

---

<h3>Finding System Informations</h3>

- `cat`
- `uname -a `
- `dmidecode`

---

<h3>User Account Management</h3>

1. `useradd`
2. `groupadd`
3. `userdel`
4. `groupdel`
5. `usermod`

---

<h3>Switch Users and sudo access</h3>

- `su -username`
- `sudo command`
- `visudo`

---

`ifconfig`\
`dmidecode`\
`fdisk -l`

---
<h3>System Utility Commands</h3>

1. date
2. uptime
3. hostname
4. uname
5. which
6. cal
7. bc

`main hier` (könyvtárszerkezet)\
`shutdown -t 300` (300sec)\
`shutdown -21:00` (konkrét időpontban)

---

`wget link`

CTRL + C prompt back

----

<h3>Könyvtárszerkezet</h3>

- /BOOT Contains file that is used by the boot loader (grub.cfg)
- /ROOT Root user home directory - it is not same as /
- /DEV System devices (disk, cdrom, speakers etc.)
- /ETC Configuration files
- /BIN --/USR/BIN Everyday user commands
- /SBIN -- /USR/SBIN System, filesystem commands
- /OPT Optional add-on application (NOT part of OS apps)
- /PROC Running processes (Only exist in memory)
- /LIB -- /USR/LIB C programming library files needed by commands and apps.
- /TMP Directory for temporary files
- /HOME Directory for users
- /VAR System logs
- /RUN System deamons that start very early to store temporary rundtime files like PID files 
- /MNT To mount external filesystem
- /MEDIA For CD-rom mounts

---

`cd` - change directory\
`pwd` - print working directory\
`ls` - listing\
`find . -name filename`\
`locate filename`\
`updatedb`

---

`passwd userid`\
Old password: ----\
New password: ----

---

<h3>Wildcards</h3>

- \* zero or more characters
- ? single characters
- [] range of characters

---

Create 9 file:\
`touch filename{1..9}`\
`touch Csaba{1..9}`

List filename file\
`ls -l Csaba*`\
Több file törlése\
`rm Csaba*`

\ = slash (escape character)\
^ = caret (the beginning of the line)\
$ = dollar sign (the end of the line)

---

<h3>Soft and Hardlink</h3>

- inode (pointer or number of a file on the hard disk)
- soft link (link will be remover if file is removed)
- hard link (deleting, renaming or moving the original file will not affect the hard link)

`ln -s file` -- softlink\
`ln new file original file`

---
<h3>Commands Syntax</h3>

Command options and arguments\
Options: 
- Modify the way that a commands works
- hyphen (kötőjel)
- dash (gondolatjel - followed by a single letter.)

Some commands accept multiple options.

Arguments:
- Most commands are used together wieht one or more arguments.
- Some commands assume a default argument if none is supplied.
- Arguments are optional for some commands and required by others.

`ls -l bart` (ls - command, l - options, bart - argument)

---

<h3>File Permission</h3>

3 type of permission r-w-x

Each permission can be controlled at 3 levels

- u (user)
- g (group)
- o (other)

Command : chmod\
`chmod g-w filename` - (remove group write permission)\
`chmod a-r filename` - (a -- every level remove read permission)

`setfacl - m u:user:rwx 'path'`\
`setfacl - m g:group:rw 'path'`\
`setfacl - Rm "entry" 'path'`\
`setfacl - x u:user 'path'`\
`setfacl - b 'path'`

---
<h3>Help Commands</h3>

- Whatis command
- command --help
- mand command

---
TAB completion and Up arrow

---

<h3>Adding text to Files (Redirects)</h3>

- `vi` (vi editor)
- Redirect command output > or >> 
- echo > or >>

`cat` - what inside in the file

---
<h3>Standard Output to a File (tee)</h3>

`echo "szöveg" | tee filename`

append\
`echo "szöveg" | tee -a filename`

How many characters --- `wc -c`\
word -- `wc -w`

`ls -l | tee listdir` same `cat listdir`

---
<h3>Pipes</h3>

`ls -ltr | more`\
`ls -l | tail -1` - last line

---
<h3>File Display Commands</h3>

- `cat`
- `more`
- `less`
- `head -2 filename` - first 2 line
- `tail -2 filename` - last 2 line

---
<h3>Filter/Text Processor Commands</h3>

- `cut`
- `awk`
- `grep` and `egrep`
- `sort`
- `uniq`
- `wc` (word count)

---
<h3>cut commands</h3>

`cut -c1 filename` - first character\
`cut -c1,2,3 filename` - picked characters\
`cut -c1-3 filename` - range of characters\
`cut -b1-3 filename` - by bite size

---
<h3>awk commands</h3>

`awk '{print $1}' filename` - print 1st field from a file

`ls -l | awk '{print $1, $3}'`\
`ls -l | awk '{print $NF}' filename` - last column\
`awk '/jerry/ {print}' filename` - search command

Replace Word

`echo "Hello Tom" | awk '{$2="Adam"; print $0}'`

Get line that have more than 15 byte size

`awk 'length($0) > 15' filename`

---

<h3>grep and egrep</h3>

`grep --version` or `grep --help`\
`grep keyword file` - search for a keyword from a file
>>`grep Seinfeld seinfeld-characters` - example

`grep -c keyword file` - search for a keyword and count
>> `grep -c Seinfeld seinfeld-characters` - example

`grep -i KEYword file` - search for a keyword ignore case-sensitive
>> `grep -i seinfeld seinfeld-characters` - example

`grep -n keyword file` - Display the matched lines and their line numbers

`grep -v keyword file` - Display everything but keyword
>> `grep -vi seinfeld seinfeld-characters` - example

`grep keyword file | awk '{print $1}'` - Search for a keyword and then only give the 1st field

`ls -l | grep Desktop` - Search for a keyword and then only give the 1st field

`egrep -i "keyword|keyword2" file` - Search for 2 keyword
>> `egrep -i "Seinfeld|Costanza" seinfeld-characters` - example

---

<h3>sort/ uniq - Text processors commands</h3>

Sort command sorts in alphabetical order.\
Uniq command filters out the repeated or duplicate lines.

`sort --version` or `sort --help` - Check version or help\
`sort file` - Sorts file in alphabetical order\
`sort -r file` - Sorts in reverse alphabetical order\
`sort -k2 file` - Sort by field number\
`ls -l | sort file` - List sort by alphabetical order
 
`uniq file` - Removes duplicates \
`sort file | uniq` - Always `sort` before using `uniq` their line numbers\
`sort file | uniq -c` - Sort first then uniq and list count\
`sort file | uniq -d` - Only show repeated line

---

<h3>`wc` - Text processors commands</h3>

The command reads either standard input or a list of files and generates:\
<b>newline count, word count, and byte count.</b>

`wc file` - Check file line count, word count, and byte count\
`wc -l file` - Get the number of lines in a file\
`wc -w file` - Get the number of words in a file\
`wc -c file` - Get the number of byte in a file

`ls -l | wc -l` - Number of files\
`ls -l | grep drw` - Get the Directories\
`ls -l | grep drw | wc -l` - Get the line of Directories\
`grep keyword | wc -l` - Number of keywords line

---

<h3>Compare Files</h3>

- `diff` - Line by line
- `cmp` - Byte by byte

---

<h3>Compress and uncompress file</h3>

- `tar`
- `gzip`
- `gzip - d` or `gunzip`

`tar cvf file.tar file` - Compress\
`tar xvf file.tar` - Uncompress\
`tar czvf`\
`tar xzvf`

`gzip file.tar`\
`gzip -d file.tar.gz`

`rm -rf`

---

<h3>Truncate File Size</h3>

The linux `truncate` command is often used to shring or extend the size of a file to the specified size.

`truncate -s 10 filename`

---

<h3>Combining and Splitting Files</h3>

- Multiple files can be combined into one and
- One file can be split into multiple files

>> `cat file1 file2 file3 > file 4`
>> `split file4`

>> example: `split -l 300 file.txt childfile`

Split file.txt into 300 lines per file and output childfileaa, childfileab, childfileac

`cat filename | wc -l` - how many lines have

---

<h3>Linux file editor</h3>

- A text editor is a program which enables you to create and manipulate data (text) in a Linux file.
- There are several standard text editors available on most Linux sytems:
------- vi - Visual editor
------- ed - Standard line editor
------- ex - Extended line editor
------- emacs - A full screen editor
------- pico - Beginner's editor
------- vim - Advance version of vi

<h3>Introduction to vi editor</h3>

- <h4>vi supplies commands for:</h4>
  
  - inserting and deleting text
  - replacing text
  - moving around the file
  - finding and substitutings strings
  - cutting and pasting text

- <h4>Most common keys:</h4>
  
  - i - insert
  - Esc - Escape out of any mode
  - r - replace
  - d - delete
  - :q! - quit without saving
  - :wq! - quit and save

---
### `sed` command
- Replace a string in a file with a newstring
- Find and delete a line
- Remove empty lines
- Remove the first or n lines in a file
- To replace tabs with spaces
- Show defined lines from a file
- Substitute within vi editor
- And much more ....

example:
- `sed 's/Kenny/Lenny/g' filename` - only change display not a file
- `sed -i 's/Kenny/Lenny/g' filename` - change file
- `sed 's/Costanza// filename` - only remove on the screen
- `sed -i 's/Costanza// filename` - remove in the file
- `sed '/Seinfeld/d filename` - delete line where is e.g. Seinfeld
- `sed '/^$/d' filename` - delete empty lines only a screen
- `sed -i '/^$/d' filename` - delete empty lines in the file
- `sed '1d' filename` - delete the first line only a screen
- `sed -i '1d' filename` - delete the first line in the file
- `sed '1,2d' filename` - delete the first 2 line on the screeen
- `sed -i '1,2d' filename` - delete the first 2 line in the file
- `sed 's/\t/ /g' filename` - replace tab to space on the screen
- `sed -i 's/\t/ /g' filename` - replace tab to space in the file
- `sed 's/ /\t/g' filename` - replace space to tab on the screen
- `sed -i 's/ /\t/g' filename` - replace space to tab in the file
- `sed -n 12,18p filename` - show defined lines from a file
- `sed 12,18d filename` - shows outside the specified lines
- `sed G filename` - put under each line an empty line on the screen
- `sed -i G filename` - put under each line an empty line in the file

---

<h3>User Account Management</h3>

commands:
- `useradd`
- `groupadd`
- `userdel`
- `groupdel`
- `usermod`

files:
- /etc/passwd
- /etc/group
- /etc/shadow

Example: `useradd -m superheroes -s /bin/bash -c "user description" -m -d /home/spiderman spiderman`

`useradd -m newusername`\
`useradd - g newusername`  - add new user a group\
`userpasswd newusername`\
`userdel newusername`

userupdate: `sudo usermod -a -G sudo newusername`

---

<h3>Switch Users and Sudo Access</h3>

Commands
- `su - username`
- `sudo command`
- `visudo`

File
- /etc/sudoers

----

<h3>Monitor Users</h3>

- `who`
- `last`
- `w`
- `finger`
- `id.`

`last | awk '{print $1}' | sort | uniq` - only first column without duplicate

---

<h3>Talking to Users</h3>

- `users`
- `wall`
- `write`

---

<h3>Linux Account Authentication</h3>

- Types of Accounts
  - Local accounts
  - Domain/Directory accounts

---

<h3>System Utility Commands</h3>

- `date`
- `uptime`
- `hostname`
- `uname`
- `which`
- `cal`
- `bc`

---

<h3>Processes and Jobs</h3>

- Application = Service
- Script
- Process
- Daemon
- Threads
- Job

---

<h3>Process/Services Commands</h3>

- `systemctl` or `service`
- `ps`
- `top`
- `kill`
- `crontab`
- `at`

---

<h3>Process Management</h3>

- Background = CTRL-z, jobs and `bg`
- Foreground = `fg`
- Run process even after exit = `nohup process &`
  - OR = `nohup porcess > /dev/null 2>&1 &`
- Kill a process by name = `pkill`
- Process priority = `nice` (e.g. `nice -n 5 process`)
- Process monitoring = `top`
- List process = `ps`

---

<h3>System Monitoring</h3>

- `top`
- `df`
- `dmesg`
- `iostat 1`
- `netstat`
- `free`
- `cat /proc/cpuinfo`
- `cat /proc/meminfo`

---

<h3>Log Monitoring</h3>

Log Directory = /var/log
- boot
- chronyd = NTP
- cron
- maillog
- secure
- messages
- httpd
  
---

<h3>System Maintenance Commands</h3>

- shutdown
- init 0-6
- reboot
- halt

---


<h3>Changing System Hostname</h3>

- `hostnamectl - set-hostname newhostname`
  
---

<h3>Finding System Information</h3>

- `cat` /etc/redhat-release
- `uname -a`
- `dmidecode`
  
---

<h3>Terminal Control Keys</h3>

- CTRL-u - erase everything you've typed on the command line
- CTRL-c - stop/kill a command
- CTRL-z - suspend a command
- CTRL-d - exit from an interactive program (signals end of data)
  
---

<h3>Terminal Commands</h3>

- `clear` - clear your screen
- `exit` - exit out of the shell, terminal or a user session
- `script` - The script command stores terminal activities in a log file that can be named by a user, when a name is not provided by a user, the default filename, typescript is used 
  
---

<h3>SOS report</h3>

- What is SOS report?
  - Collect and package diagnostic and support data
- Package name
  - `sos-version`
- Command
  - `sos report`
  
---

<h3>Environment variables</h3>

What are environment variables?
- An environment variable is a dynamic-named value that can effect the way running processes will behave on a computer. They are part of the environment in which a process runs.
- In simple words: set of defined rules and values to build an environment


 To view all environment variables
- `printevn` OR `env`

 To view ONE environment variable
 - echo $SHELL

 To set the environment variables
 - `export TEST=1`
 - `echo $TEST`

 To set environment variable permanently
 - `vi .bashrc`
 - `TEST='123'`
 - `export TEST`

 To set global environment permanently
 - `vi /etc/profile` OR `vi /etc/bashrc`
 - `TEST='123'`
 - `export TEST`
  
---

<h3>Linux kernel</h3>

What is a Kernel?
- Interface between hardware and software

---

<h3>Introduction to Shell</h3>

What is Shell?
- Its like a container
- Interface between Users and Kernel/OS
- CLI is a Shell

Find your Shell
- `echo $0`
- Available Shells `cat /etc/shells`
- Your Shells? /etc/passwd
  
---

<h3>Types of Linux Shells</h3>

- Gnome
- KDE
- sh
- bash
- csh and tcsh
- ksh

cat/etc/shells

---

<h3>Shell Scripting</h3>

What is a Shell script?
  A shell script is an executable file containing multiple shell commands that are executed sequentially. The file can contain:
    - Shell (#! /bin/bash)
    - Comments (# comments)
    - Commands (echo,cp,grep etc.)
    - Statements (if,while,for etc.)

  Shell script should have executable permission (e.g -rwx r-x r-x)

  Shell script has to be called from absolute path (e.g /home/userdir/script.bash)

  If called from current location then ./script.bash

---

<h3>Basic scripts/Shell scripts</h3>

- Output to screen using "echo"

- Creating tasks

  - Telling your id, current location, your files/directories, system info
  - Creating files or directories
  - Output to a file ">"

- Filters/Text processors through scripts (cut,awk,grep,sort,uniq,wc)

---

<h3>Input and Output</h3>

Create script to take input from the user
    - `read`
    - `echo`

---

<h3>if-then scripts</h3>

- If then statement

    - <b>If this happens = do this</b>
    - <b>Otherwise =  do that</b>

---

<h3>For Loop Scripts</h3>

- For loops

    - <b>Keep running until specified number of variable</b>
    - <b>e.g: variable=10 then run the script 10 times</b>
    OR
    - <b> variable=green,blue,red (then run the script 3 times for each colors)</b>
--- 

\#!/bin/bash

\# For loop to create 5 files named 1-5

for i in {1..5}
do
	touch $i
done

---

\#!/bin/bash

\# Example of defining variables

a=Csaba
b=Bajzáth
c="Linux class"

echo "My first name is \$a"\
echo "My surname is \$b"\
echo "My class name is $c" 

---

\#!/bin/bash

\# Simple for loop output

for i in 1 2 3 4 5
do
echo "Welcome $i times"
done

---

<pre>#!/bin/bash

# Check the variable

count=100
if [ $count -eq 100 ]
then
  echo Count is 100
else
  echo Count is not 100
fi
</pre>

---

\#!/bin/bash
\# Author
\# Date
\# Desc

echo Hello, my name Csaba Bajzáth
echo
echo What is your name?
read namecontainer
echo
echo Hello $namecontainer
echo

---

<pre>#!/bin/bash

# List all users one by one from /etc/passwd file

i=1
for username in `awk -F: &apos;{print $1}&apos; /etc/passwd`
do
	echo &quot;Username $((i++)) : $username&quot;
done
</pre>

---

<pre>#!/bin/bash

# Specify days in for loop

i=1
for day in Mon Tue Wed Thu Fri
do
	echo &quot;weekday $((i++)) : $day&quot;
done
</pre>
---

<pre>#!/bin/bash

# Check if a variable value is met

a=`date | awk &apos;{print $1}&apos;`

if [ &quot;$a&quot; == Mon ]

	then
	echo Today is $a
	else
	echo Today is not Monday
fi
</pre>

---

<pre>#!/bin/bash

# Check if a file file exist

clear
if [ -e /home/lin6echo/error.txt ]

		then
		echo &quot;File exist&quot;
		else
		echo &quot;File does not exist&quot;
fi
</pre>

---

<h3>do-while scripts</h3>

do while

  - The while statement continually executes a block of statements while a particular condition is true or met
  - e.g: Run script until 2pm
  <br>

      while  [ condition ]
      do

               command1
               command2
               commandN
      done
----

<pre>#!/bin/bash

# Script to run for a number of seconds

count=0
num=10
while [ $count -lt 10 ]
do
	echo
	echo $num seconds left to stop this process $1
	echo
	sleep 1
num=`expr $num - 1`
count=`expr $count + 1`
done
echo
echo $1 process is stopped!!!
echo
</pre>

---

<pre>#!/bin/bash

# Script to run for a number of times

c=1
while [ $c -le 5 ]
do
	echo &quot;Welcome $c times&quot;
	(( c++ ))
done
</pre>

---

<pre>#!/bin/bash

echo
echo Please chose one of the options below
echo
echo &apos;a = Display Date and Time&apos;
echo &apos;b = List file and directories&apos;
echo &apos;c = List users logged in&apos;
echo &apos;d = Check System uptime&apos;
echo

	read choices

	case $choices in

a) date;;
b) ls;;
c) who;;
d) uptime;;
*) echo Invalid choice - Bye.
	
	esac
</pre>

---

<h3>Case statement script</h3>

Case
  - If option a is selected = do this e.g: run "top" command
  - If option b is selected = do this e.g: run "pwd" command
  - If option c is selected = do this e.g: run "df -h" command

---

<h3>Check Other Servers Connectivity</h3>

- A script to check the status of remote hosts

<pre>#!/bin/bash
# Author: Csaba Bajzáth
# Date: 04/11/2022
# Description: This script will ping a remote host and notify

ping -c1 192.168.1.1
	if [ $? -eq 0 ]
	then
	echo OK
	else
	echo NOT OK
	fi
</pre>
---
<h3>Aliases</h3>

Aliases is a very popular command that is used to cut down lengthy and repetitive commands

- `alias ls = "ls -al"`
- `alias pl = "pwd; ls"`
- `alias tell = "whoami; hostname; pwd"`
- `alias dir = "ls -l | grep ^d"`
- `alias lmar = "ls -l | grep Mar"`
- `alias wpa = "chmod a+w"`
- `alias d = "df -h | awk '{print \$6}' | cut -cl-4"`

---

<h3>Creating User or Global Alieses</h3>

User = Applies only to a specific user profile
Global = Applies to everyone who has account on the system

User = /home/user/.bashrc
Global = /etc/bashrc

  `alias hh="hostname"

---
<h3>Shell History</h3>

All commands are recorded

Command: "history"

----

<h3>Download Files or App</h3>

linux = `wget`

---

<h3>curl and ping commands</h3>

linux = `curl`
linux = `ping`

---

<h3>System upgrade - Patch Managment</h3>

Two types of upgrades
- Major version = 5,6,7
- Minor version = 7.3 to 7.4

Minor version = `apt update`

example: `apt update -y`

upgrade - delete packages
update - preserve old packages

---
<h3>Advanced Package Manager</h3>

`rpm -hiv link.rpm` - install package
`rpm -qa | grep installed package` - check
`rpm -qi installed package` - information
`rpm -e installed package` - delete package
`rpm -qc installed package` - shows configuration files

---
<h3>Rollback Updates and Patches</h3>

Rollback a package or patch
- `apt install \<package name>`
- `apt history undo \<ID>`

Rollback an update

`apt update` - Update will preserve them
`apt upgrade` - Upgrade will delete obsolete packages
`apt history undo \<ID>`

---
116



