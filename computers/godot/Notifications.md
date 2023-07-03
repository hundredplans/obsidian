# Common Examples
## Method
- \_ready(): NOTIFICATION_READY
- \_enter_tree(): NOTIFICATION_ENTER_TREE
- \_exit_tree(): NOTIFICATION_EXIT_TREE
- \_process(delta): NOTIFICATION_PROCESS
- \_physics_process(delta): NOTIFICATION_PHYSICS_PROCESS
- \_draw(): NOTIFICATION_DRAW

## No-Method
- NOTIFICATION_PARENTED
- NOTIFICATION_UNPARENTED

## Other
- Find others here [click me](https://docs.godotengine.org/en/stable/classes/class_node.html#class-node-constant-notification-enter-tree)

# General
- Every object implements a \_notification method that you can access in script
- Find exampls of Notifications here [click me](https://docs.godotengine.org/en/stable/classes/class_node.html#class-node-constant-notification-enter-tree)
- Methods labeled "virtual" are intended to be overwritten by scripts
- \_init calls first then \_enter_tree then \_ready