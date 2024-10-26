#!/bin/bash

# # Define the list of values for X
# X_values=("no" "h2p" "masp" "stp" "optimized")

X_values=("no" "h2p" "masp" "stp")
# Loop over each file in the traces directory
for trace_file in ../traces/*.champsimtrace.xz; do
  # Extract the base name (Y part)
  trace_name=$(basename "$trace_file" .champsimtrace.xz)
  
  # Loop over each value of X
  for X in "${X_values[@]}"; do
    # Define the output log file path
    log_file="../logs_new/$trace_name-$X.txt"
    
    # Check if the log file already exists
    if [ -f "$log_file" ]; then
      echo "Log file $log_file already exists. Skipping..."
      continue
    fi

    # Run the command if log file does not exist
    ./no-$X-1core -warmup_instructions 25000000 -simulation_instructions 25000000 -traces "$trace_file" > "$log_file"
    
    # Check if the command ran successfully
    if [ $? -eq 0 ]; then
      echo "Successfully completed: $trace_name with X=$X"
    else
      echo "Error occurred with: $trace_name with X=$X"
    fi
  done
done
