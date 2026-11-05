# Optimization of Space Shuttle External Tank Design Return on Investment (ROI)

[![Conference](https://img.shields.io/badge/Conference-ICAANA_2025-blue.svg)](https://amrita.edu)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://www.python.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.10%2B-orange.svg)](https://scipy.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Presented at the **International Conference on Advances and Applications of Numerical Analysis (ICAANA 2025)**, Coimbatore, India.

---

## 👥 Authors
- **Dhimant Kulkarni**
- **Hima Sagar B**
- **Araveeti Vibhas Reddy** ([@VIBHAS777](https://github.com/VIBHAS777))
- **Mamatha T M**

---

## 🚀 Overview
The Space Shuttle External Tank (ET) comprises over 90% of the shuttle vehicle's gross liftoff weight. Every single kilogram shaved from the tank's dry structural weight translates directly into a one-kilogram gain in orbital payload capacity to Low Earth Orbit (LEO).

This project implements a non-linear constrained optimization system using **Sequential Least Squares Programming (SLSQP)** coupled with finite stress equations. By optimizing skin thickness, LOX/LH2 tank geometries, and material selection (transitioning from standard Al-2219 to Al-Li 2195 alloys), the model achieves massive lifecycle launch cost reductions and quantifiable multi-mission ROI.

---

## 📁 Repository Structure
```
space-shuttle-tank-roi-optimization/
├── paper/
│   └── Optimization_of_Space_Shuttle_External_Tank_Design_ROI.pdf # Full research paper
├── src/
│   ├── materials.py       # Cryogenic aerospace alloy mechanical & cost database
│   └── optimizer.py       # SLSQP constrained optimization engine
├── main.py                # Demonstration & ROI calculation pipeline
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🛠️ Installation & Execution
```bash
git clone https://github.com/VIBHAS777/space-shuttle-tank-roi-optimization.git
cd space-shuttle-tank-roi-optimization
pip install -r requirements.txt
python main.py
```

---

## 📜 Citation
```bibtex
@inproceedings{kulkarni2025spacetank,
  title={Optimization of Space Shuttle External Tank Design Return on Investment (ROI)},
  author={Kulkarni, Dhimant and Sagar B, Hima and Reddy, Araveeti Vibhas and Mamatha, T. M.},
  booktitle={International Conference on Advances and Applications of Numerical Analysis (ICAANA)},
  year={2025}
}
```
