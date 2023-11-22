# /bin
- Contains executable files that allow your system to boot
- Stored in binary format

# /boot
- Linux kernel
- Initial RAM disk images?
- Bootloader (GRUB)

# /dev
- All devices represented as files
- e.g. /dev/sda1 is the name of a disk
- USB devices, CPU, GPU etc

# /etc
- System-wide configuration files
- Shell scripts executed at boot
- Text files

# /home
- Contains a folder for each user on your device
- Stores private data

# /lib
- Contains the libraries required by the programs inside /bin
- Sets of functions shared between programs

# /lost+found
- Recovery folder used for [[ext4]]
- Produced for every seperate partition of a disk

# /media
- Used for automatic mounting for exmple USB and CD-ROM

# /mnt
- Used for manual mounting
- You can still mount to /media if you desire

# /opt
- Used to in stall commercial software to your system
- Not essential to your system

# /proc
- Virtual file-system used by the linux kernel
- Used by the kernel to run processes

# /root
- Used for the root account
- Kind of like the /home/username but for root user

# /run
- Temporary file system used to store files early in boot
- Recently introduced

# /sbin
- Used for binaries essential to system tasks
- Meant to be run by the super user
- Essential

# /srv
- Service files installed on your system
- For example a web-server [[http]] ?

# /tmp
- Where programs store temporary files on your system
- Cleaned up on reboot

# /usr
- All programs used by a regular user
- Contains binaries
## /usr/bin
- Programs installed by your distro 
## /usr/lib
- Libraries for the executables in /usr/bin
## /usr/local
- Compiled programs that are installed system-wide
## /usr/share
- Shared data used by /usr/bin
- Config files
- Themes
- Icons
- Wallpapers
- Sound files
## /usr/share/doc
- Documentation files for programs installed on your system

# /var
- Contains files that are variable and change frequently
- For example log files
