Used to read from files
``` c++
string text;
ifstream MyFile ("file_name.txt");
while (getline(MyFile,text));
	{
	cout << text
	}
MyFile.close()
```
see [[getline]]