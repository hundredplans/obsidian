Replace name1 with name2
- :s/name1/name2/g replaces all instances in line
- :s/name1/name2 replaces first instance in line
- :%s/name1/name2 replaces every occurence in file
- :%s/name1/name2/gc replaces every file in the whole file with a prompt
- :#,#s/name1/name2/g replaces all occurences on line # to #