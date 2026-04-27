[README_shot_map.md](https://github.com/user-attachments/files/27128104/README_shot_map.md)# 🎯 Goal vs Shot Map Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-green) ![Domain](https://img.shields.io/badge/Domain-Football%20Analytics-black)

## 📌 Overview
This project visualises all shot attempts in a football match plotted on a pitch map, differentiating between goals scored and shots that did not result in a goal. It helps assess a player's or team's shooting efficiency and preferred scoring zones.

## 🎯 Objectives
- Map every shot attempt on a football pitch
- Distinguish between goals and non-goal shots visually
- Identify the most dangerous shooting zones on the pitch

## 🛠️ Tools & Libraries
| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| VS Code | Development environment |
| Matplotlib | Pitch drawing and shot plotting |
| Pandas | Data handling and processing |

## 📊 What the Visualisation Shows
- 🟢 **Green markers** = Goals scored
- 🔴 **Red markers** = Shots that did not result in goals
- Shot locations plotted on a scaled football pitch
- Density of shots in different zones of the penalty area

## 🖼️ Output
> Shot map showing all attempts plotted on a football pitch with colour-coded outcomes.

## 📁 Project Structure
```
goal-vs-shot-map/
│
├── data/
│   └── shot_data.csv          # Shot coordinates and outcomes
├── shot_map.py                # Main analysis script
├── output/
│   └── shot_map_plot.png      # Output visualisation
└── README.md
```

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/shabab-analyst/goal-vs-shot-map

# Install dependencies
pip install matplotlib pandas

# Run the script
python shot_map.py
```

## 💡 Key Insights
- Most goals came from inside the six-yard box and penalty spot area
- Long range shots had a very low conversion rate
- Left side of the penalty area produced more goal attempts

## 👤 Author
**Shabab** — Aspiring Sports Analyst | Kerala, India
- LinkedIn: linkedin.com/in/shabab-sports-analyst
- Email: shabab326@gmail.com

