import pandas as pd
import random
import os

def scramble_city_data(csv_path):
    """
    ON-DEMAND MODE: Scrambles the city data once per page load.
    The parking lot stays stable while the user inputs their vehicle counts.
    """
    if not os.path.exists(csv_path):
        return
        
    try:
        df = pd.read_csv(csv_path)
        
        # 1. Randomly toggle 1 or 2 slots to Red (Occupied)
        for _ in range(2):
            idx = random.randint(0, len(df)-1)
            df.at[idx, 'availability'] = 0 if df.at[idx, 'availability'] == 1 else 1
            
        # 2. Shuffle the distances randomly between 10m and 120m
        df['distance'] = random.sample(range(10, 125, 5), len(df))
        
        # 3. Save it back to the CSV
        df.to_csv(csv_path, index=False)
        print("[SYSTEM] City environment shuffled for new session.")
        
    except Exception as e:
        print(f"[ERROR] Could not scramble data: {e}")