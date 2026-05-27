# 🚀 Quantum Smart Parking Simulation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Qiskit](https://img.shields.io/badge/Qiskit-Quantum%20Computing-6045ba.svg)](https://qiskit.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **Quantum-Classical Hybrid System** designed to solve urban parking congestion using advanced mathematical optimization. This project models the smart city parking allocation problem as a **Quadratic Unconstrained Binary Optimization (QUBO)** task and solves it using a Quantum Minimum Eigensolver.

It features a live, interactive dashboard that compares the efficiency of a **Quantum Engine (Global Optimization)** against a traditional **Classical Engine (Greedy Search)** in real-time.

---

## ✨ Key Features
* **Global Quantum Optimization:** Evaluates $2^n$ possible parking statevectors simultaneously to find the absolute minimum total fleet distance.
* **Classical vs. Quantum Benchmarking:** Live comparison showing how greedy algorithms fail in congested environments while quantum logic thrives.
* **Hardware-Aware Execution:** Strategically limits the quantum simulation sector to prevent classical RAM overload (safely running 20 qubits on 16GB RAM).
* **Interactive City Simulator:** An on-demand traffic simulator that shuffles distances and parking availability to mimic real-world IoT sensor data.

---

## 📸 Output & Screenshots

Here is a visual overview of the Quantum Smart Parking Simulation in action:

### 1. Interactive Control Room Dashboard
*(Displays the split-view comparison between the Quantum Sector and the Full Classical Grid)*
![Interactive Dashboard](assets/Screenshot_1.png)

### 2. Real-Time Efficiency Analytics
*(Shows the dynamic calculation of Total Fleet Distance, Average Distance Per Vehicle, and Decision Latency)*
![Analytics Report](assets/Screenshot_2.png)

### 3. Simulator & Solver Terminal Logs
*(Demonstrates the background traffic simulator and the exact Quantum Solver hardware checks)*
![Terminal Logs](assets/Screenshot_3.png)

### 4. Dynamic Fleet Configuration
*(Interactive inputs allowing users to adjust vehicle counts and simulate various traffic conditions)*
![Fleet Configuration](assets/Screenshot_4.png)

### 5. Quantum Advantage Verdict
*(Real-time verdict highlighting the efficiency savings achieved by the Global Optimizer over the Greedy approach)*
![Quantum Advantage](assets/Screenshot_5.png)

### 6. Live City Shuffling
*(Demonstrates the 'Shuffle City' feature, simulating real-world dynamic road closures and changing distances)*
![City Shuffle](assets/Screenshot_6.png)

> **Note:** To see the UI in action, clone the repository and run the simulation locally!

---

## ⚙️ Installation & Setup

Follow these steps to set up the quantum simulation environment on your local machine.

**1. Clone the repository**
```bash
git clone [https://github.com/PanabakaMahesh/Quantum-Smart-Parking-Simulation.git](https://github.com/PanabakaMahesh/Quantum-Smart-Parking-Simulation.git)
cd Quantum-Smart-Parking-Simulation

2. Create a virtual environment

Bash
python3 -m venv venv

3. Activate the virtual environment

For Linux/macOS:

Bash
source venv/bin/activate
For Windows:

DOS
venv\Scripts\activate

4. Upgrade PIP & Install Dependencies

Bash
pip install --upgrade pip
pip install -r requirements.txt

5. Run the Application

Bash
python main.py
(Once running, open your web browser and navigate to http://127.0.0.1:5000)