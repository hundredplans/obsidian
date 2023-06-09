# Sorting Info / Human-Readable
- sed -n ('1,5p'|'5p') -> Only print specified line or line range
- sed -I NUM -> Changes wrap-length to specified amount
- sed -u -> Immediately display info rather than buffering, useful for real-time monitoring
- sed -z -> Seperate lines by NUL 

# File Shenanigans
- sed -i\[SUFFIX] -> Edit files and create a backup with SUFFIX if provided
	e.g. sed -i.txt 
- sed --follow-symlinks -> Follows symlinks
- sed -s -> Consider files as seperate rather one long stream

# Adding Scripts
- sed -e SCRIPT -> Add specified SCRIPT 
- sed -f SCRIPT-FILE -> Add contents of script-file as script

# Altering Regex
- sed -E/-r -> Uses [[extended-regex]] rather than basic
- sed --posix -> Changes to basic regex, limits [[regex-capture-groups]] to \\1-\\9. Used for compatibility among different os'es very unlikely this is necessary for me

# Info Commands
- sed --help -> Display a help message
- sed --version -> Display the current version