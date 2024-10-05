Called once on an Object when the Class creates it, similar to \_ready()
Constructors can also take parameters
``` c++
class SomeClass
{
	public:
		SomeClass(string Name) // Constructor
		{
			cout << Name;
		}
};

SomeClass my_obj("En Garde!");
// Will print the constructor value when created
```
Constructors are created by using the name of the class within it as a function

You can also declare Constructors outside of the Class with ::
``` c++
class SomeClass
{
	public:
		SomeClass(int a, int b, int c);
};

SomeClass::SomeClass(int a, int b, int c)
{
// some code here
}
```
Constructors outside of the class need to have their parameters defined within the class then are named with ClassName::ClassName(parameters)