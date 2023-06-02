- When light exceeds maximum luminance (brightness) supported by camera it bleeds outwards
- Even if effect is enabled it will be weak or invisible, for it to show one of two:
	- 1. Light pixel surpasses HDR Threshold, setting that can be set
	- HDR Scale allows to make the light surpassing the threshold lighter or darker
	- 2. Bloom is greater than 0.0

# Other Settings
- Intensity: How strong the effect is (0.0 is no effect)
- Strength: Unnecessary, use levels instead
- Blend Mode Effects:
	- Additive: No blending, very strong produces dream-like effect with low-intensity bloom
	- Screen: Ensures glow is never brighter than itself, good basic option
	- Softlight: Default and weak, subtle color disturbance, good with dark scenes
	- Replace: Used to blur whole screen or debug effect, only shows glow
	- Mix: Artsy one, blends glow effect with main image
- Levels: Small levels are strong glows around objects while large levels are hazy glows around the screen
- You can combine levels to create interesting glow patterns
- You can control [[Glow]] using a [[Glow Map]]