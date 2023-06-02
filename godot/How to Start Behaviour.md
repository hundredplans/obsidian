- Setting what method the child should call
```
$Child.method_name = "do" # Parent
call(method_name) # Child, calls method do if it has one
```
- Initiliazing [[Callable]]
```
$Child.func_property = other_child.some_method # Parent
func_property.call() # Child
```
- Setting a variable on child to the reference the parent
```
$Child.target = self # Parent
print(target) # Child
```
- Initializing a [[NodePath]]
```
$Child.target_path = ".." # Parent, can use .. to go back one level
get_node(target_path) # Child, gets the parent
```
- These options ensure [[Loose Coupling]] for the child as they don't know how/why they are calling the method