# Panama Canal Lock Water Usage & Efficiency Modeling

This project models and visualizes freshwater loss, savings, and efficiency during ship transits through the Panama Canal. It uses Python code and Jupyter notebooks to estimate water displaced, water lost, and potential annual savings based on ship size, lock type, and operational strategies.

Developed as part of a Department of Defense–sponsored project on freshwater conservation in the Panama Canal. The tool helps visualize researched data and simulate different water usage scenarios, including the impact of ship size, batching, and scheduling on water efficiency.

## Features
- Estimate water use per transit for Panamax and Neopanamax locks
- Calculate displacement, water loss, and per-cycle cost
- Batch smaller ships into shared lock cycles
- Basic scheduling logic (greedy fill)
- Visual outputs for water savings and efficiency

## Files
- `canal_data.py` — Core calculations
- `canal_data.ipynb` — Interactive notebook for analysis, simulation, and visualization
- `test.py` — Minimal example of using the core functions

## Requirements
- Python 3.8+
- NumPy
- Matplotlib
- Jupyter Notebook for interactive analysis

Install dependencies:
```bash
pip install numpy matplotlib jupyter
```

## Usage
**Run a quick test:**
```bash
python test.py
```
```python
from canal_data import analyze_transit
result = analyze_transit(30000, "panamax")
print(result)
```

**Interactive analysis:**
Open `canal_data.ipynb` in Jupyter Notebook to explore water loss, savings, and scheduling strategies with charts and tables.

## Example Output
```
{'lock_type': 'Panamax',
 'ship_size': 30000,
 'water_displaced': 7200000,
 'water_needed': 42800000,
 'water_lost': 42800000.0,
 'cost_per_lock': 8560.0,
 'percent_savings': 14.4,
 'annual_water_displaced': 604800000000}
```


