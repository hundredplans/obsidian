``` c++
class Name
{
	public:
	int Num;
	string name_string;
};
```
Num and name_string are attributes of the Class
public is an [[Access Specifier]]
You can create [[Objects]] from this Class

You can define functions within classes
``` c++
class SomeClass
{
	public:
	void my_method(){
		cout << "En Garde!"
	}
};

SomeClass my_obj;
my_obj.my_method() // Calls the method
```

You can define functions outside of classes (why?)
``` c++
class SomeClass
{
	public
	void my_method();
};

void SomeClass::my_method()
{
	cout << "En Garde!"
}
```

The function can be accessed in the same way as the code above