import pandas as pd
import re
import os

# Folder containing the text files
folder_path = "logs_new/"

# Initialize a list to hold the extracted data
data = []

# Process each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        # Extract A and B values from filename
        a, b = filename.rsplit('-', 1)
        b = b.replace('.txt', '')
        
        # Read the file
        with open(os.path.join(folder_path, filename), 'r') as file:
            text = file.read()
            
            # Extract STLB TOTAL MPKI
            stlb_total_mpki = re.search(r"STLB TOTAL.*MPKI:\s+(\S+)", text)
            stlb_total_mpki = float(stlb_total_mpki.group(1)) if stlb_total_mpki else None
            
            # Extract STLB LOAD MPKI
            stlb_load_mpki = re.search(r"STLB LOAD.*MPKI:\s+(\S+)", text)
            stlb_load_mpki = float(stlb_load_mpki.group(1)) if stlb_load_mpki else None
            
            # Extract CPU cumulative IPC
            ipc = re.search(r"CPU 0 cumulative IPC:\s+(\S+)", text)
            ipc = float(ipc.group(1)) if ipc else None
            
            # Append the extracted values to the data list
            data.append([a, b, stlb_load_mpki, stlb_total_mpki, ipc])

# Create a DataFrame and save it as a CSV
df = pd.DataFrame(data, columns=["A", "B", "STLB LOAD MPKI", "STLB TOTAL MPKI", "IPC"])
df.to_csv("extracted_data.csv", index=False)

print("Data extraction complete. Saved to extracted_data.csv.")
