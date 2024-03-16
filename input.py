import pandas as pd
import re

# Read CSV file into DataFrame
df = pd.read_csv('input.csv')

# Regular expression pattern to extract domain from URL
domain_pattern = re.compile(r'<url>https?://([a-zA-Z0-9._-]+)</url>', re.IGNORECASE)

# Function to extract domain from Access Link for a given device type
def extract_domain(device_type):
    filtered_df = df[df['Device_Type'] == device_type]
    if not filtered_df.empty:
        match = domain_pattern.search(filtered_df['Stats_Access_Link'].iloc[0])
        if match:
            return match.group(1)
        else:
            return "Domain not found in the URL."
    else:
        return "Device Type not found in the database."

# Get user input for device type
device_type_input = input("Enter the device type: ")

# Extract domain for the specified device type
domain = extract_domain(device_type_input)

# Display extracted domain
print(f"Extracted domain for Device Type '{device_type_input}': {domain}")
