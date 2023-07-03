- Small sun and environment icon at top allows to set default environment that is overriden by any environment nodes or resources in scene
- Setting an environment resource to a camera has the highest priority followed by a WorldEnvironment node then the default environment at the top
- CameraAttributesPhysical uses arbitrary units CameraAttributesPractical uses irl (mm)
- Using a CAPhys overrides a Camera3D if set in the Camera but not if set in the WorldEnv
- Setting CameraAttributes on camera and not WorldEnv is recommended

# Tweaking Settings & What They Do
- Sky might greatly affect lighting in your scene due to [[IBL]]

## Options
- Clear Color is the default color
- Custom Color has a custom color value but stays the same color throughout
- Sky lets you define a custom sky material, objects wil lreflect this sky and absorb ambient light
- Canvas displays a 2D Canvas Layer as the background
- Keep does not draw any sky and keeps what was present on previous frames, to optimize perfomance for example when in doors, causes glitches if sky is visible

# Sky
- 3 Built-In Sky Materials to choose (and Shaders)
- Panaroma uses a 360d panaroma sky image (2:1 ratio is recod), image should be in .hdr or .exr instead of .png or .jpg
- Procedural uses a procedurrally generated sky, you can set sun, sky and horizon colors. The sun's position is derived from the first 4 directional light 3ds in scene, you can have 4 suns at a time. This is used in the preview
- Physical is physically based with adjustable scattering parameters (?). Supports only one sun, looks better than procedural but is slower
- Panaroma sky images are sometimes called [[HDRI]], can be found on [Poly Haven](https://polyhaven.com/hdris)
- If you have very bright spots enable HDR Clamp Exposure in import settings

# Ambient Light
- Light that affects each piece of geometry with the same intensity, global and independent of lights added to the scene. Does not vary based on camera position and viewing angle unlike reflected light
- Different ambient lights to choose from
	- Background (Sky, custom color, look at Options above). Will vary depending on Sky image's content
	- Disabled (indoor)
	- Color, useful for perfomance and fixing pitch black shadows
	- Sky, uses the sky even if it's not set, if it is set behaves same as background
- Sky contribution lets you blend between a set ambient color and the sky ambient light

# Specular Light
- Also called reflected light, is the other component of [[IBL]]
- Different specular lights to choose from:
	- Background (look at Options above)
	- Disabled (indoor, perfomance)
	- Sky same as Ambient Light

# Fog
- Makes distant objects fade into a uniform color
- Two kinds of Fog in Godot 4
	- Depth Fog (distance from camera)
	- Height Fog (applied to objects below or above a certain height)
- Two properties of these fog
	- Sun Amount, when looking towards a DirectionalLight color of the fog changes, simulating sunlight passing through it
	- Transmit enabled, makes light stand out more across fog

# Volumetric Fog
- See later [here](https://docs.godotengine.org/en/stable/tutorials/3d/environment_and_post_processing.html) if needed