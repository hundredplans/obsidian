- User = u
- Group = g
- Other = o
- All = a

- chmod u+x -> Add execute perms to user
- chmod og=xw -> Set other and group perms to execute and write
- chmod a-x -> Remove execute perms from all
- chmod u=rwx \*.txt -> Add all perms for users for all files with .txt

# Numbers
- 0 - No perms
- 1 - x
- 2 - w
- 4 - r
- ugo = 777 (All perms for everyone)
- ugo = 770 (All perms but not for other)