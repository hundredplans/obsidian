# Far & Near Blur
- Depth of Field / Far Blur: Blurs objects behind a given range, simulates focal distance on cameras
- Amount: Controls how much blur, tweak Quality for large blurs
- Depth of Field / Near Blur: Blurs objects close to the camera, same as Far Blur
- Common to use Far Blur and Near Blur to focus on a given object or create a [[Tilt Shift]] effects

# Exposure
- Multiplies scene brightness from camera, higher = brighter
- Auto Exposure is basic Godot exposure setting, has moderate perfomance cost, recod to leave off if doesn't have a great impact on game
- Best way to use auto exposure is to set strong lights to energy beyond 1.0, values of 3.0 and 6.0 are usually good
## Auto Exposure Settings
- Scale: Higher = brigher 
- Min Sens: Average of light in all pixels on screen that autoexpo will aim to adjust for
- Max Sens: Same as above
- Speed: How fast autoexpo corrects itself, high for fast-paced games could be distracting though