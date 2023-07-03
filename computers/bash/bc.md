- Stands for Basic Calculator
- Only works on one line of input, use [[paste]] to transform large datasets into one line

# Example Commands
- bc -l -> Use math library
- echo '1 + 2' | bc -l -> Will output 3
- cat num_files.txt | psate -sd+ | bc -l -> will add all numbers in file as delimiter is changed to + onto one line