Defined with ~ClassName(){}
Used to delete objects
Can't take parameters, and there can only be one destructor per class
You can think of destructors as memory garbage collectors

Destructors are called when
- Object goes out of scope
- If an object is allocated using (MyClass MyObject = new MyClass) you can use (delete MyObject)
- When the container is destroyed/cleaned up e.g. (std::vector where std is the container)
- When an exception is thrown
- When a program terminates

``` c++
class MyClass {
	public:
		~MyClass():
			cout << "Destructor Called!"
}
```