Defines the accessibility of classes, methods and other members
``` c++
// Access Specifier in a class
class SomeClass 
{
	public:
		int a; // Public int
	private:
		int b; // Private int
};
```
If you try to access b outside the class it will throw an error

Three Types of Access Specifiers
- Public -> Members can be viewed and accessed from outside the class
- Private -> Members can't be accessed or viewed from outside the class
- Protected -> Members can't be accessed from outside the class except inherited classes
