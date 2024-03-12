Inheriting attributes and methods from one class to another is possible

Base Class: Class being inherited from
Inherited Class: Class inherting from the Base Class

Can inherit from a Class using :
There are three types of inheritance, one for each [[Access Specifier]] (public is most common)
``` c++
class ParentClass
{
	public:
		int a;
};

class InheritedClass:public ParentClass
{
	public:
		int b;
};
```
You can also have multi-level inheritance where an Inherited Class can also be the Base Class, in this case the original Base Class attributes are also accesible by the second Inherited Class

Multiple Inheritance is possible using comma-seperated lists
``` c++
class ParentClassOne
{
	public:
}

class ParentClassTwo
{
	public:
}

class InheritedClass:public ParentClassOne, public ParentClassTwo
```