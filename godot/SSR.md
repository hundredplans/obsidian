- Screen Space Reflections
- Alternative to [[Reflection Probes]]
- Use when objects are in contact often (object and floor etc)
- Work in real time rather than precomputed, offer higher quality reflections, can be used to make real time objects reflect

# Settings
- Max Steps: Length of reflection, bigger = more compute
- Fade In: Makes contact area softer
- Fade Out: Step limit fades out softly
- Depth Tolerance: Allows to pass behind objects, will make [[SSR]] exhibit less "breakups(?)" but will sometimes create physicall incorrect reflections

- Note transparent materials wont reflect or [[hint_screen_texture]] or [[hint_depth_texture]] [[Uniform Variables]]