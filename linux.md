```
sudo -su - 
sudo -s
su -
cd / - root
```
---

`uptime`
`hostname`
uname --> `uname -a`
ps ... ps -fu .... ps -f ... ps -ef .... ps awx ... ps u
`top`
kill -PID
`kill -9` (No Question)
ls -l .... ls -ltr
`whoami`
wim -- > exit :wq!
`mkdir
`| pipe 
ls -ltr | more (lapzás - space)
d -directory, l -link, - -file
rwx - read, write, execute
ugo - user, group, other

---

chown "new-user" file
chgrp "new-group" file
```
chmod g+w file (group enable write permission)
chmod a+r file (all enable read permission)
chmos u+w file (user enable write permission)
```
---

`rm `- remove

text
echo "something" > filename 
echo "something" >> filename 

`touch` - create a file

whatis command
command --help
command man

---

###Maintenance Commands

`cp` - copy 
`rm` - remove
`mv` - move
`mkdir` - make directory
`rmdir` or `rm -r` ---- remove directory
`chgrp` - 
`chown` - 
`rm - Rf` - force full remove

chown root:root file

---

###Filters/Text Processors Commands
```
- out
- awk
- grep
- sort
- uniq
- wc (word count)
```
`cut -c1 filename` (give you back first letters)

`awk` separate each columns

`awk '(print $1)' filename` (first column)

`grep` ---- search

grep mit miben

sort - sorba rendezés
sort filename
sort -r fordított sorrend

`uniq`  - removes all duplicates
`sort | uniq` együtt 

`wc` - word count
`wc filename` (-l, lines)

---

###Finding System Informations

- `cat`
- `uname -a `
- `dmidecode`

---

###User Account Management

1. `useradd`
2. `groupadd`
3. `userdel`
4. `groupdel`
5. `usermod`

---

###Switch Users and sudo access

- su -username
- sudo command
- visudo

---
```
ifconfig
dmidecode
fdisk -l
```
---
###System Utility Commands
```
1. date
2. uptime
3. hostname
4. uname
5. which
6. cal
7. bc
```
`main hier` (könyvtárszerkezet)

`shutdown -t 300` (300sec)
`shutdown -21:00` (konkrét időpontban)

---

`wget link`

CTRL + C prompt back

----

### Könyvtárszerkezet

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

`cd` - change directory
`pwd` - print working directory
`ls` - listing
`find . -name filename`
`locate filename`
`updatedb`

---

`passwd userid`
Old password: ----
New password: ----

---

### Wildcards

- \* zero or more characters
- ? single characters
- [] range of characters

---

Create 9 file:
`touch filename{1..9}`
`touch Csaba{1..9}`

List filename file
`ls -l Csaba*`
Több file törlése
`rm Csaba*`

\ = slash (escape character)
^ = caret (the beginning of the line)
$ = dollar sign (the end of the line)

---

### Soft and Hardlink

- inode (pointer or number of a file on the hard disk)
- soft link (link will be remover if file is removed)
- hard link (deleting, renaming or moving the original file will not affect the hard link)

`ln -s file` -- softlink
ln new file original file

---
### Commands Syntax

Command options and arguments
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

### File Permission

3 type of permission r-w-x

Each permission can be controlled at 3 levels

- u (user)
- g (group)
- o (other)

Command : chmod
`chmod g-w filename` - (remove group write permission)
`chmod a-r filename` - (a -- every level remove read permission)

`setfacl - m u:user:rwx 'path'`
`setfacl - m g:group:rw 'path'`
`setfacl - Rm "entry" 'path'`
`setfacl - x u:user 'path'`
`setfacl - b 'path'`

---
### Help Commands

- Whatis command
- command --help
- mand command

---
TAB completion and Up arrow

Adding text to Files (Redirects)
- `vi` (vi editor)
- Redirect command output > or >> 
- echo > or >>

`cat` - what inside in the file

---
### Standard Output to a File (tee)

`echo "szöveg" | tee filename`

append
`echo "szöveg" | tee -a filename`

How many characters --- `wc -c`
word -- `wc -w`

`ls -l | tee listdir` same `cat listdir`

---
### Pipes

`ls -ltr | more`
`ls -l | tail -1` - last line

---
### File Display Commands

- `cat`
- `more`
- `less`
- `head -2 filename` - first 2 line
- `tail -2 filename` - last 2 line

---
### Filter/Text Processor Commands
- `cut`
- `awk`
- `grep` and `egrep`
- `sort`
- `uniq`
- `wc` (word count)

---
### `cut` commands

`cut -c1 filename` - first character
`cut -c1,2,3 filename` - picked characters
`cut -c1-3 filename` - range of characters
`cut -b1-3 filename` - by bite size

---
### `awk` commands

`awk '{print $1}' filename` - print 1st field from a file

`ls -l | awk '{print $1, $3}'`

`ls -l | awk '{print $NF}' filename` - last column

`awk '/jerry/ {print}' filename` - search command

Replace Word

`echo "Hello Tom" | awk '{$2="Adam"; print $0}'`

Get line that have more than 15 byte size
`awk 'length($0) > 15' filename`

---
### `grep` and `egrep`

`grep --version` or `grep --help`
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
### `sort` / `uniq` - Text processors commands

Sort command sorts in alphabetical order.
Uniq command filters out the repeated or duplicate lines.

`sort --version` or `sort --help` - Check version or help
`sort file` - Sorts file in alphabetical order
`sort -r file` - Sorts in reverse alphabetical order
`sort -k2 file` - Sort by field number
`ls -l | sort file` - List sort by alphabetical order
 
`uniq file` - Removes duplicates 
`sort file | uniq` - Always `sort` before using `uniq` their line numbers
`sort file | uniq -c` - Sort first then uniq and list count
`sort file | uniq -d` - Only show repeated line

---

### `wc` - Text processors commands

The command reads either standard input or a list of files and generates: <b>newline count, word count, and byte count.</b>

`wc file` - Check file line count, word count, and byte count
`wc -l file` - Get the number of lines in a file
`wc -w file` - Get the number of words in a file
`wc -c file` - Get the number of byte in a file

`ls -l | wc -l` - Number of files 
`ls -l | grep drw` - Get the Directories
`ls -l | grep drw | wc -l` - Get the line of Directories
`grep keyword | wc -l` - Number of keywords line

---
### Compare Files

- `diff` - Line by line
- `cmp` - Byte by byte

---

### Compress and uncompress file

- `tar`
- `gzip`
- `gzip - d` or `gunzip`

`tar cvf file.tar file` - Compress
`tar xvf file.tar` - Uncompress
`tar czvf`
`tar xzvf`

`gzip file.tar`
`gzip -d file.tar.gz`

`rm -rf`

---
### Truncate File Size
The linux `truncate` command is often used to shring or extend the size of a file to the specified size.

`truncate -s 10 filename`

---
### Combining and Splitting Files
- Multiple files can be combined into one and
- One file can be split into multiple files

>> `cat file1 file2 file3 > file 4`
>> `split file4`

>> example: `split -l 300 file.txt childfile`

Split file.txt into 300 lines per file and output childfileaa, childfileab, childfileac

 




