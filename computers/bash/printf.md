printf is equivalent to prin`t
printf "message contents"
to display colors use
printf "\\e\[38;2;255;0;0mThis is red\\e\[0m"

# Breakdown
\\e represents the start of an escape sequence
\\e \[0m at the end resets the color to default values
38 represents text foreground color
2 indicates RGB mode