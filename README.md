# **VeRoLog Logistic Problem Solution** 🚛🔧  

This repository contains implementations of three optimization algorithms:  
- **Ant Colony Optimization (ACO)** 🐜  
- **Genetic Algorithm (GA)** 🧬  
- **Particle Swarm Optimization (PSO)** 🏆  

These algorithms solve a **logistics scheduling problem** by optimizing **truck and technician allocation** to service locations **while minimizing costs**.

---

## **📖 Table of Contents**
1. [Overview](#overview)
2. [Dataset Structure](#dataset-structure)
3. [Algorithms Implemented](#algorithms-implemented)
4. [Problem Description](#problem-description)
5. [Dependencies & Installation](#dependencies--installation)
6. [Usage](#usage)
7. [Output Format](#output-format)

---

## **📌 Overview**
The problem scenario is adapted from the **[VeRoLog Solver Challenge](http://www.verolog.eu/)**.  
This work provides several **optimization models** capable of:
- **Optimizing the routing of deliveries and technicians** 🚚🔧
- **Meeting customer availability** 📅
- **Reducing operational costs** 💰

Customers purchase **household appliances/machines**, which need to be:
1. **Delivered within a specific timeframe** ⏳
2. **Installed by a technician** 🔧

This repository explores **three different approaches** (**ACO, GA, PSO**) to **solve this problem efficiently**.

---

## **📂 Dataset Structure**
The dataset (`training_2.txt`) defines logistics constraints, such as **truck/technician capacities, customer requests, and machine delivery/installation constraints**.

### **1️⃣ General Problem Parameters**
| **Parameter**               | **Description**                          | **Example** |
|-----------------------------|------------------------------------------|------------|
| `DAYS`                      | Number of days in planning period       | `DAYS = 10` |
| `TRUCK_CAPACITY`            | Max machines a truck can carry          | `15`       |
| `TRUCK_MAX_DISTANCE`        | Max distance per truck per day          | `2000`     |
| `TRUCK_DISTANCE_COST`       | Cost per unit truck distance traveled   | `10`       |
| `TECHNICIAN_DISTANCE_COST`  | Cost per unit technician distance       | `100`      |

### **2️⃣ Machines Section**
Defines machine types available for delivery.

| **Machine ID** | **Size** | **Idle Cost** |
|---------------|---------|--------------|
| 1             | 6       | 343          |
| 2             | 5       | 887          |

### **3️⃣ Locations Section**
Provides coordinate locations for **the depot, customers, and technicians**.

| **Location ID** | **X Coordinate** | **Y Coordinate** |
|---------------|--------------|--------------|
| 1 (Depot)    | 699          | 335          |
| 2 (Customer) | 473          | 376          |
| 3 (Customer) | 546          | 621          |

### **4️⃣ Requests Section**
Lists customer requests, including **machine type, delivery window, and quantity**.

| **Request ID** | **Customer ID** | **First Day** | **Last Day** | **Machine Type** | **Quantity** |
|---------------|-------------|-------------|------------|---------------|----------|
| 1            | 8           | 1           | 6          | 1             | 1        |
| 2            | 46          | 1           | 2          | 1             | 1        |

### **5️⃣ Technicians Section**
Provides **technician details**, including location, working limits, and skill sets.

| **Technician ID** | **Home Location ID** | **Max Distance** | **Max Requests** | **Skills** |
|-----------------|-----------------|-------------|-------------|---------|
| 1              | 40              | 529         | 9           | 0 1     |
| 2              | 1               | 995         | 9           | 0 1     |

---

## **🚀 Algorithms Implemented**
This repository implements **three different metaheuristic approaches**:

### **1️⃣ Ant Colony Optimization (ACO) 🐜**
- **Inspiration**: Ants finding the shortest path to food.
- **Approach**:
  - Pheromone-based decision-making.
  - Heuristic-based route construction.
  - Cost evaluation & minimization.

📂 **File**: `ACO_solution.py`

---

### **2️⃣ Genetic Algorithm (GA) 🧬**
- **Inspiration**: Natural selection & evolution.
- **Approach**:
  - Tournament selection 🎯
  - Two-point crossover 🔀
  - Bit-flip mutation 🎲

📂 **File**: `GA_solution.py`

---

### **3️⃣ Particle Swarm Optimization (PSO) 🏆**
- **Inspiration**: Swarm intelligence & collaborative movement.
- **Approach**:
  - Velocity and position updates.
  - Inertia weight & acceleration coefficients.
  - Tracking personal & global best.

📂 **File**: `PSO_solution.py`

---

## **📌 Problem Description**
The problem involves **scheduling logistics for multiple locations**, considering:
- 🚚 **Truck capacity & distance limits**  
- 👷 **Technician allocation & working constraints**  
- 💰 **Minimization of total cost (truck & technician costs)**  

The algorithms use a **cost function** that accounts for:
- 📏 **Distance-based costs**
- ⏳ **Idle machine costs**
- 🚛 **Number of trucks & technicians used**

---

## **📥 Dependencies & Installation**
Install required dependencies:
```bash```
pip install numpy deap

---

## **Usage**

Run the algorithms using:
```bash```
python ACO_solution.py
python GA_solution.py
python PSO_solution.py

---

## **Output format**

Each script generates an optimized logistics schedule:
```bash```
SOLUTION SUMMARY:
TRUCK_DISTANCE = <value>
NUMBER_OF_TRUCK_DAYS = <value>
NUMBER_OF_TRUCKS_USED = <value>
TECHNICIAN_DISTANCE = <value>
NUMBER_OF_TECHNICIAN_DAYS = <value>
NUMBER_OF_TECHNICIANS_USED = <value>
IDLE_MACHINE_COSTS = <value>
TOTAL_COST = <value>
SCHEDULE DETAILS
DAY = <value>
NUMBER_OF_TRUCKS = <value>
NUMBER_OF_TECHNICIANS = <value>
