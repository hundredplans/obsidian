## Orthographic Views
1. 1 - Front
2. 3 - Right
3. 7 - Top

- If your laptop doesn't have them, you can go to Edit/Preferences/Input/Emulate Numpad which changes the number keys on your keyboard into numpad, will have to remap 1,2,3 for face vertex and edge so not worth it for me

- You want to make sure your characters are facing the Green (Y) Axis to export correctly into Godot

## Mirroring
- When applying mirroring, you should apply on the X axis with Orientation setting set to Negative.

- Clipping keeps the edges on the mirror's edge connected as one vertex.

- Mirror modifier is based on the center of the character (cursor), if you change th cursor's position mirror will stop functioning

- Ctrl-A is a shortcut to apply modifiers

- You can apply the mirror modifier before making an armature

## Shading
- The texture with the focus in the shading menu is the one that will be displayed

## Coordinates
- You can change Z to 0 on the foot so it's perfectly aligned with the ground

## Selecting Faces/Edges/Vertices
- Ctrl + and Ctrl - allows you to select all connected faces
- Ctrl Alt (Vertice) - Ring Select (idk just try hard to explain)
- Ctrl RMB - Lasso Select

## Deleting Faces/Edges/Vertices
- X (Dissolve Edges) - Removes edges without affecting geometry too hard

# Moving Faces/Edges/Vertices
- Alt-S - Move vertices along their normals

# Creating Faces/Edges/Vertices
- K (Knife Tool) - Allows you to manually set edges

# Moving 3d Cursor
- Select two vertices or a line and do cursor to selected, it will place it on the mid-point between those two vertices/line

# Setting Origin
- Helps with Godot physics
- RMB Object/Set Origin/3D Cursor 

# Armature Stuff
- Inverse Kinematics allows bones not to sink when moving Root
- Alt-G and Alt-R in Pose Mode resets position & rotation
- [[Armature Process]]
- If you significantly alter vertices do Ctrl P with Character then Armature Selected and automatic weights

# Moving Camera
- 8, 2 on numpad allow to move camera perspective up and down incrementally
