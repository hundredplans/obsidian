Profiling - How to optimise the code
Profilers - Typically CPU profilers, used to measure the time of execution

# Two Main Types
Tracing Profiler - Execute with your code and take a note (add a lot of overhead)
Sampling Profiler - Execute your program, every so often (100miliseconds) stops your program and gives you statistics (looks at the stack trace)

Line Profiler - Presents profiling results in a more readable way, e.g. [[kernprof]] for python
Memory Profilers - Profile how much memory is allocated