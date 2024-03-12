Used to read from a [stream](fstream.md) and store the value in a variable
getline(FileStream, StringVar)
``` c++
string text;
ifstream MyFile ("file_name.txt");
while (getline(MyFile ,text));
	{
	cout << text
	}
MyFile.close()
```

The return value is the !(Error/EoF) bool of the MyFile stream
Sets the value of text to the found line

You can specify deliminator
getline(FileStream, StringVar, "-") -> Sets deliminator to -