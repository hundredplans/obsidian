- Signed Distance Field Global Illumination
- Can provide global illumination for off-screen elements unlike [[SSIL]]
- See [here](https://docs.godotengine.org/en/stable/tutorials/3d/global_illumination/using_sdfgi.html#doc-using-sdfgi) for more info
- Better real-time than [[Baked Lightmaps]] but worse than [[VoxelGL]]
- Very demanding setting
- Ensure Meshinstance nodes have Global Illumination > Mode set to static, can be set for Import or as a setting 

# Settings
- Use Occlusion: Reduce light leaks, perfomance costs only use if needed
- Read Sky Light: Enabled in outdoor, disabled indoor
- Bounce Feedback: Small perfomance cost for light to bounce, realistic indirect light. Sensible is to set between 0.3 and 1.0. If your lighting is too splotchy decrease Energy
- Cascades: Very expensive, decrease to 4 or lower if camera moves fast
- Min Cell Size: Accurate indirecxt light and reflection at perfomance cost, affect two settings below
- Cascade 0 Distance: Reduce level of detail in nearest cascade but cascade transition less noticeable
- Max Distance: How far away the SDFGI is processed, always set below Camera Far value
- Y Scale: Set to 75 or 50% if your isn't highly vertical
- Energy: Brightness multiplier
- Normal Bias: Increase if striping artifacts
- Probe Bias: Increase if striping artifacts

# Mesh Global Illumination Modes
- Disabled: Will receive indirect light but will not contribute indirect light
- Static: Both receive and contribute indirect light
- Dynamic (not support with [[SDFGI]]) Acts the same as disabled

# Light Bake Modes
- Disabled: Won't be used for [[SDFGI]] baking, won't contribute indirect light
- Static: Contribute indirect light, if light is changed will mess up SDFGI until camera refocuses
- Dynamic: Slower than Static, only use if lights change significantly in gameplay
