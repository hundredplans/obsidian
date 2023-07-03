- Screen-Space Indirect Lighting
- Used on small objects that other lighting methods miss, also emissive materials
- Intended to be used a complement to other methods, hard to spot, provides subtle ambient occlusion similar to [[SSAO]]

# Settings
- Radius: Distance that bounced light can travel, high = further, can result in long spikes surrounding light sources
- Intensity: Brighter effect
- Sharpness: Similar to [[SSAO]] Sharpness
- Normal Rejection: Used to avoid light leaking when only one side of an object is illuminated, can be disabled if light leaking is desired