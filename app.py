from flask import Flask, render_template, jsonify, request
import pandas as pd
import time
from quantum.quantum_allocator import quantum_allocate_batch
from traffic_simulator import scramble_city_data

app = Flask(__name__)

# --- SYSTEM CONFIGURATION ---
CSV_PATH = "data/parking_data.csv"
QUANTUM_SLOT_LIMIT = 5 # Strict limit to keep 16GB RAM safe
# ----------------------------

def classical_greedy_allocate(df, num_vehicles):
    """Classical picks the best from all available slots."""
    temp_df = df[df['availability'] == 1].copy()
    allocs = {}
    for i in range(num_vehicles):
        if temp_df.empty: break
        idx = temp_df['distance'].idxmin()
        allocs[f"V{i+1}"] = temp_df.loc[idx, 'slot_id']
        temp_df = temp_df.drop(idx)
    return allocs

@app.route('/')
def index():
    # Scramble the city layout ONLY when the page is reloaded
    scramble_city_data(CSV_PATH)
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    # Read the number of vehicles from the frontend (Defaults to 0 on page load)
    q_vehicles = int(request.args.get('q_veh', 0))
    c_vehicles = int(request.args.get('c_veh', 0))
    
    df = pd.read_csv(CSV_PATH)
    
    # 1. QUANTUM ENGINE (Only runs if user requested > 0 vehicles)
    start_q = time.perf_counter()
    q_allocs = quantum_allocate_batch(CSV_PATH, q_vehicles, limit_slots=QUANTUM_SLOT_LIMIT) if q_vehicles > 0 else {}
    q_speed = (time.perf_counter() - start_q) * 1000 if q_vehicles > 0 else 0
    
    # 2. CLASSICAL ENGINE (Only runs if user requested > 0 vehicles)
    start_c = time.perf_counter()
    c_allocs = classical_greedy_allocate(df, c_vehicles) if c_vehicles > 0 else {}
    c_speed = (time.perf_counter() - start_c) * 1000 if c_vehicles > 0 else 0
    
    # Calculate Total Distances
    q_total = sum(df[df['slot_id'] == s]['distance'].values[0] for s in q_allocs.values()) if q_allocs else 0
    c_total = sum(df[df['slot_id'] == s]['distance'].values[0] for s in c_allocs.values()) if c_allocs else 0
    
    # Calculate Average Distance per Vehicle (For Fair Comparison)
    q_avg = q_total / len(q_allocs) if len(q_allocs) > 0 else 0
    c_avg = c_total / len(c_allocs) if len(c_allocs) > 0 else 0
    
    return jsonify({
        "slots": df.to_dict('records'), 
        "quantum": q_allocs,           
        "classical": c_allocs,         
        "q_total": int(q_total),
        "c_total": int(c_total),
        "q_avg": round(q_avg, 2),
        "c_avg": round(c_avg, 2),
        "q_speed": round(q_speed, 2),
        "c_speed": round(c_speed, 2),
        "qubits": q_vehicles * QUANTUM_SLOT_LIMIT
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)