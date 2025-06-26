# Jet Engine Bracket Optimization with Fusion 360 API + Python ML

This project automates the generation, simulation, and performance prediction of aerospace brackets using **Fusion 360 API** and **Python Machine Learning**.

## 🛠️ Tools Used
- Autodesk Fusion 360 (CAD + Simulation)
- Python (VS Code + PyCharm)
- scikit-learn, pandas, numpy, matplotlib
- Regression models (MultiOutputRegressor, RMSE evaluation)

## 📂 Files Included
| File                          | Description                              |
|------------------------------|------------------------------------------|
| `Fusion_360_API_Bracket_Automation.py` | Python script to auto-generate 27 Fusion bracket designs |
| `exported parameters`           | Simulation results of 6 designs (Stress, SF, Mass) |
| `predict_stress_safety_mass.py` | Trained ML model to predict 3 outputs from geometry |
| `output                         | Actual vs Predicted Stress plot          |

## 📈 Sample Results
| Design                     | hole_dia | rib_thickness | fillet_r | Max Stress | SF   | Mass (g) |
|---------------------------|----------|---------------|----------|------------|------|----------|
| Bracket_h18_r16_f3        | 18       | 16            | 3        | 48.49      | 5.67 | 2220.40  |
| Bracket_h22_r20_f3        | 22       | 20            | 3        | 53.07      | 5.18 | 2431.33  |
| Bracket_h20_r18_f5        | 20       | 18            | 5        | 49.69      | 5.53 | 2357.88  |

## 🤖 AI Model Performance
- RMSE (Max Stress): 1.96 MPa
- RMSE (Safety Factor): 0.24
- RMSE (Mass): 2.42 g

## 🔍 What I Learned
- Parametric design automation with Fusion 360 API
- How geometry affects stress, safety, and mass
- Building & evaluating ML regression models
- Bridging mechanical design with AI

## 🙏 Acknowledgment
Special thanks to Prof. Nezamoddin for Statistical Modelling guidance, helping me understand RMSE and regression methods.

## 📬 Contact
Feel free to explore the repo or reach out to collaborate!

