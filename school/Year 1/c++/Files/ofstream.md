ofstream is used to create and write to files
```c++
ofstream MyFile ("file_name.txt");
MyFile << "Hello File";
MyFile.close()
```
You have to assign a variable to the file to open it, the name is relative to script being run