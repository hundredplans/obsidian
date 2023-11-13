Method to create archives
# Default Options
- -f -> Define name of archive file (ends with .tar)
- -c -> Copy files to archive
- -x -> Unpack tar file
- -v -> List files used
- -z -> Zip using .gz
- -t -> List contents of a tar file
- -a -> Automatically detect compression program by file extension

# Tar Uses
- tar cf archive.tar file1 file2 (copies files to archive)
- tar xf file.tar.gz --directory=dir_path/dir (extract a tar file into a dir)
- tar xvf file.tar.gz --directory=dir_path/dir (show which files were extracted)
- tar cvfz file.tar.gz file1 file2 (copies file to archive and zips)
- tar tvf file.tar (list contents of a tar file verbosely)
- tar xf file.tar --wildcards "\*.html" (extract only .html files from a tar file)
- tar caf file.tar.xz file1 file2 (creates a xz zipped archive)