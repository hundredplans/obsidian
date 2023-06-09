- Similar to [[sed]] but more based on fields rather than lines, more useful for file formats such as CV or log files with defined [[field]]s
- Parses data by default by [[field]]s, lets you operate on each [[field]] seperately
- $ is used to refer to [[field]] positions, e.g. $2 is the second [[field]]
- $0 refers to the whole line/
# Example Commands
- awk '{print $2}' -> Print the second column, {} starts and ends an awk script

# Resources
- https://backreference.org/2010/02/10/idiomatic-awk/
- [computer-hope](https://www.computerhope.com/unix/uawk.htm)
