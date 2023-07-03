- Viewports take all it's children and render them as a single texture
- This texture can then be used as any other texture, e.g. sprite
- Can be used to make a shader apply to multiple textures at a time
- The root viewport is the window to the game_world
- Each viewport can have 1 active camera
- Make sure viewport size **matches** parent control node rect size
- Viewports have their own origin, width and height. You can use get_viewport().size.x/y to retrieve the first Viewport node it reaches from the script (up)
- You can use viewport size to define bounds for movable object (timeline)
- ViewportContainers are used to display anything the viewport has inside, ViewportContainer cann't be smaller than the size of the Viewport

# Basic General Setup
```
Control
	ViewportContainer
		Viewport
```

# Capturing Texture

![[img.png]]
