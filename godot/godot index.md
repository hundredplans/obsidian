# Organized Notes
- [[Singletons]]
- [[Programming Principles]]
- [[Loads & Preloads]]
- [[How to Start Behaviour]]
- [[Notifications]]
- [[Viewports]]
- [[Environments]]
- [[Post-Processing Effects]]
- [[CameraAttributes]]

# Import
- Write a .gdignore file if you want the folder to ignore imports

# Scenes vs Scripts
- Scenes are slightly faster than scripts
- Scenes identify what constitutes a scene while scripts run the behaviour
- Scripts are resources that tell the engine a sequence of initilizations
- See [[Script Classes]] for how to transform a script into a class

# Advised Scene Structure
```
Node "Main" main.gd
	Node3D "World" game_world.gd
	Control "GUI" gui.gd
```
- When changing levels one can swap the children of "World" 

# Good Behaviour
- Sub-scenes should not be picky about how they are used (run solo)
- Scenes should have [[Loose Coupling]], a singular purpose
- If a scene needs external content use [[Dependency Injection]]
- Sibling interactions should be mediated by an ancestor
- Scenes operate best when they operate alone or with [[Loose Coupling]]
- Use a [RemoteTransform](https://docs.godotengine.org/en/stable/classes/class_remotetransform3d.html#class-remotetransform3d) when you want to move nodes relative to each other that are not parented to the same object

# Node Alternatives
- See [Node Alternatives](https://docs.godotengine.org/en/stable/tutorials/best_practices/node_alternatives.html)

# How to Reference Objects/Properties
- [[Standard Way to Access Objects]]
- [[Loads & Preloads]] for Resources
- Exporting values
- Remember you can pass Resources as references
- @onready variables
- $Child is faster than get_node("child")

# Responding to Behaviour (Up the Tree)
- Signals, note how they typically have past tense names e.g. collected
```
$Child.signal_name.connect(parent_method) # Parent 
signal_name.emit() # Child
```

# Data Preferences
- If you want to remove/insert at the front of a large array, invert it do the operations then reinvert

# Removing Children
- Use remove_child() if you want to keep node in memory (re-add later)
- Use queue_free() if you want to delete node from memory (permanently remove)

# Style Guide
- Use snake_case for folder and file names
- Use PascalCase for node names