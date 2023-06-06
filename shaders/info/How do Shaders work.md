# General
- They process each pixel on screen and return a color
- They all run parallel so there's no communication between each thread

# Why are GPUs good at shaders?
- GPUs are a lot of tiny microprocessors so they are good at shaders
- GPU threads don't know what they were doing last as they receive new information that overrides previous information
- GPU threads are *blind* and *memoryless*