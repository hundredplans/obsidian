- f -> Specify file which to run BODY pattern from
- -v foo=bar -> Allows to assign variables before program execution
- -F fs -> Specify which delimiter (field seperator) to use

- --dump-variables FILE -> Print all global variables and their values to FILE, default file if not provided is awkvars.out
- --help -> Gets help
- --version/-V -> Diplays version
- --lint=TYPE -> Provide warnings for non-portable AWK implementations, TYPE is optional
	- fatal -> Fail on warning
	- invalid -> Only invalid warnings are issued
	- noext -> Disable gawk warnings
 - --posix -> Gawk-extensions and some other features are disabled
 - --profile=FILE -> Prints a pretty version of program in file, FILE is optional and by default is awkvars.out
 - --traditional -> Disabled gawk extensions as well