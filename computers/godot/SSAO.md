- Screen-Space Ambient Occlusion
- While [[Ambient Light]], [[Reflection Probes]], Sky and constant ambient color can light up areas where light does not reach they act on a wider scale
- [[SSAO]] can simulate lighting up small spaces, darker concave areas
- Only acts on [[Ambient Light]] not direct light

# Settings
- Radius: Distance at which objects occlude each other (?), higher value costs perfomance and quality but occludes at greater distance
- Intensity: Higher = darker occlusion, recod to remain conserative, strong [[SSAO]] is distracting 
- Power: Darker occlusion high value, similar to Intensity but sharper falloff
- Detail: Makes detail pass more prominent but may add aliasing
- Horizon: Threshold to consider whether a surface is occluded or not from 0 to 1, 1 means no occlusion
- Sharpness: High = aliasing at edges, low = blur at edges
- Light Affect: Values > 0 make [[SSAO]] visible in direct light, not physically accurate but some like