sed '1,6s/hello/HELLO/' -> Replace hello with HELLO in the first 6 lines

# Selecting Lines (Adresses) (Start of COMMAND)
- NUM -> Match only NUM line in input
- ADR1, ADR2 -> Match only lines between two specified addresses
	- NUM1,NUM2 -> In range NUM1 to NUM2
	- NUM1,$ -> NUM1 to end
	- NUM1,/REGEXP/ -> Match line NUM1 no matter what and all lines following with regexp
 
- $ -> Match last line of input or file if -i or -s
- /REGEXP/ -> Match lines which match specified regexp, / inside has to be escaped
- \\%REGEXP% -> Changes delimiter from / to % (can be changed to any character) 
- ADR1! -> Match every line that is not ADR1

## GNU Extensions
- START~STEPs/ -> Start on line START and match a line every STEP, 1~2 is odd lines
- /REGEXP/I -> Matches in a case-insensitive manner
- /REGEXP/M -> Enables ^ and $ to match start and end of lines, "\\\`" and "\\\'" does this natively
- 0,/REGEXP/ -> Also match first line with regexp (GNU Extension)
- ADR1,+NUM -> Match address and up to +NUM lines
- ADR1, ~NUM -> Match starting line and every following START LINE + NUM line e.g. 2,~5 would match 2,7,12,17