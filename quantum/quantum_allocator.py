import pandas as pd
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import NumPyMinimumEigensolver

def quantum_allocate_batch(csv_path, num_vehicles, limit_slots=5):
    # Only load the number of slots allowed by the hardware limit
    data = pd.read_csv(csv_path).head(limit_slots)
    slots = data['slot_id'].tolist()
    vehicles = [f"V{i+1}" for i in range(num_vehicles)]
    
    qp = QuadraticProgram("SmartParking")
    for v in vehicles:
        for s in slots:
            qp.binary_var(name=f"x_{v}_{s}")

    costs = {}
    for v in vehicles:
        for _, row in data.iterrows():
            # Penalty (100,000) for unavailable slots
            penalty = 0 if row['availability'] == 1 else 100000
            costs[f"x_{v}_{row['slot_id']}"] = row['distance'] + penalty
    qp.minimize(linear=costs)

    # Constraints
    for v in vehicles:
        qp.linear_constraint(linear={f"x_{v}_{s}": 1 for s in slots}, sense="==", rhs=1)
    for s in slots:
        qp.linear_constraint(linear={f"x_{v}_{s}": 1 for v in vehicles}, sense="<=", rhs=1)

    # Exact Eigensolver - 20 Qubits (Safe for 16GB)
    exact_solver = MinimumEigenOptimizer(NumPyMinimumEigensolver())
    result = exact_solver.solve(qp)
    
    allocations = {}
    for i, var in enumerate(qp.variables):
        if result.x[i] > 0.5:
            parts = var.name.split('_')
            allocations[parts[1]] = parts[2]
            
    return allocations