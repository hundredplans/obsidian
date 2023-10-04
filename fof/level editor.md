# Level Editor 
- When you load in, chooses a size you selected in preferences e.g. (30x30, 50x50, 100x100)
- the tiles you don't want you can remove/not select anything on and they won't be saved 
- if you reload/in game free roam camera Some sort of way to cycle between the two modes 
- Middle-Mouse click to free roam or Q, E rotate on the y axis 
- Hold left click to spam whatever is selected, or click to place it 
- Right click to remove Object -> Decoration -> Wall -> Tile
- Select Level Difficulty for each level
- Variations are just different levels
# ELEVATION 
- Units on different elevations can't attack eaceh other (except ranged) 
- Elevation exists, up to 5 is possible, .5 elevations to climb to the next elevation (only affects vision) units can't go up an elevation without stepping through a 0.5 
- How elevations work (sandwich) 
	- Default Tile 
	- Elevation Tile 
	- Default Tile Build Mode 
- You don't see decorations 
- You can jump down from 1 to 0 but not from 0 to 1
# BUILD MENU
- Tab opens Buildmenu 
- Each tile has a default Buildmenu 
- Tabs to switch between (Tiles, Walls, Objects, Decorations) 
- 1,2,3,4,5 to switch between 
- Makes a straight wall if 4 tiles are connected in a specific pattern some way to disable this sometimes
# Tiles
- Ground Tile
# Walls
- Have to be placed on a tile 
	- Wall 
	- Window 
- Walls are thick, units can't walk on a 4 wall
- Walls have sub-wall (decorations) inside which look different 
- Walls have a height property that affects how tall it is (default 2)
- You can place tiles on top of walls
# Objects
- You can place decorations where object area
- They're always placed on tiles 
- Objects can be rotate 
- Interactable gameplay mechanics, can be walkeable/transparent 
- Door -> Can be placed on tiles 
- Objects have folders where all models of the object are found, when you place an Object you select the model 
- There can only be one object per tile
- Enemy Object
- Spawn Object (that allows player to place units on the tile)
# Decoration Types 
## Tile Decorations
- You can place decorations where object area
- Each decoration has two properties (walkable, transparent) 
## Wall Decorations
Wall Decorations - Which always do nothing, except look good