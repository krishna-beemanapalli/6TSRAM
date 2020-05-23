# Data word size
word_size = 8
# Number of words in the memory
num_words = 1024

# Technology to use in $OPENRAM_TECH
tech_name = "freepdk45"
# Process corners to characterize
process_corners = ["TT"]
# Voltage corners to characterize
supply_voltages = [ 1.1 ]
# Temperature corners to characterize
temperatures = [ 25 ]

# Output directory for the results
output_path = "mem"
# Output file base name
output_name = "sram_{0}_{1}_{2}".format(word_size,num_words,tech_name)

