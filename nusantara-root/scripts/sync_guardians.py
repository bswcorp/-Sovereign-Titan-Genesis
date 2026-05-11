import json
import csv
import os

# Path to the exported CSV from Google Forms
CSV_INPUT = "guardian_applications.csv"
# Path to our Airdrop list
JSON_OUTPUT = "../../stg-web3/scripts/guardian_list.json"

def sync_data():
    if not os.path.exists(CSV_INPUT):
        print(f"🚨 Error: {CSV_INPUT} not found. Please export from Form first.")
        return

    new_addresses = []
    with open(CSV_INPUT, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming the column name is 'Sovereign Wallet Address'
            address = row.get('Sovereign Wallet Address', '').strip()
            if address.startswith('0x') and len(address) == 42:
                new_addresses.append(address)

    # Save to JSON for the Airdrop script
    with open(JSON_OUTPUT, 'w') as f:
        json.dump(new_addresses, f, indent=4)
    
    print(f"✅ Sync Complete: {len(new_addresses)} Guardians added to the Airdrop queue.")

if __name__ == "__main__":
    sync_data()
  
