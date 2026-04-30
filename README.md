# 🎯 AlgoViz — Algorithm Visualizer

<div align="center">

![AlgoViz Banner](https://img.shields.io/badge/AlgoViz-Desktop%20Edition-cyan?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![BUBT](https://img.shields.io/badge/BUBT-Software%20Development-red?style=for-the-badge)

**A real-time, interactive algorithm visualization desktop application built with Python & Pygame.**  
*Designed to help students visually understand how sorting and pathfinding algorithms actually work — step by step.*

</div>

---

## 🎓 How This Helps Students

Learning algorithms from textbooks can be confusing. AlgoViz bridges the gap between theory and understanding by letting students **see** what the algorithm is doing at every step.

| Problem Students Face | How AlgoViz Solves It |
|---|---|
| Can't visualize how sorting works | Watch bars move and swap in real-time |
| Hard to understand comparisons | Color-coded highlights show exactly which elements are being compared |
| C++ code feels abstract | Live C++ code panel highlights the exact line executing right now |
| Can't experiment with own data | Custom array input — type your own values and watch them sort |
| Algorithms run too fast to follow | Adjustable speed slider from very slow to fast |
| Hard to remember what each color means | Live legend at the bottom of every visualization |

### 🧠 What Students Learn

- **Bubble Sort** — How adjacent comparisons and swaps gradually push large elements to the end
- **Selection Sort** — How scanning for the minimum and placing it step by step builds a sorted array
- **Insertion Sort** — How elements shift right to make room, just like sorting playing cards in hand
- **Merge Sort** — How divide-and-conquer splits and merges subarrays
- **Quick Sort** — How pivot selection and partitioning separates smaller and larger elements
- **Binary Search** — How halving the search range finds an element in O(log n)
- **Linear Search** — How sequential checking works and why it is O(n)
- **BFS** — How level-by-level traversal finds the shortest path on a grid
- **DFS** — How depth-first traversal goes deep and backtracks on dead ends
- **Dijkstra** — How shortest distances are updated dynamically using a priority queue

---

## ✨ Features

- 🔴🟢🔵 **Color-coded number boxes** at the footer — Red when comparing/swapping, Green when sorted, Blue when idle
- 📊 **Real-time bar visualization** with live value updates
- 💻 **C++ code panel** — highlights the exact line of code executing at every step
- ✏️ **Custom array input** — students can type their own values and observe the sort
- 🎯 **Search target input** — set any target value for Binary and Linear Search
- ⏱️ **Adjustable speed** — from very slow (learning mode) to fast (overview mode)
- 📝 **Explanation panel** — plain-English description of each step as it happens
- 🗺️ **Interactive pathfinding grid** — draw walls, place start/end, and watch BFS/DFS/Dijkstra solve it
- 📈 **Live stats** — comparison count, swap count, nodes visited, path length

---

## 🖥️ Screenshots

> *Run the app to see it in action!*

```
Sorting View          │  C++ Code Panel       │  Explanation Panel
──────────────────────┼───────────────────────┼─────────────────────
 ▌  ▌▌  ▌ ▌  ▌▌▌    │  void bubbleSort() {  │  Comparing a[2]=8
 ▌▌ ▌▌▌ ▌▌▌  ▌▌▌    │    for(i=0;i<n-1;i++) │  and a[3]=3 ...
 ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌    │  → if(a[j]>a[j+1])   │  Swapping!
─────────────────────  │    swap(a[j],a[j+1]) │
[3][8][1][5][2][7]    │  }                    │
 🔴 🔵 🔵 🔵 🔵 🔵   │                       │
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/algoviz.git
cd algoviz

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python main.py
```

### Requirements

```
pygame>=2.0.0
```

---

## 🗂️ Project Structure

```
algoviz/
│
├── main.py                        # App entry point & main game loop
│
├── algorithms/                    # All algorithm generators
│   ├── __init__.py                # Algorithm registry (SORTING_REGISTRY, PATH_REGISTRY)
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── binary_search.py
│   ├── linear_search.py
│   ├── bfs.py
│   ├── dfs.py
│   └── dijkstra.py
│
├── core/                          # App state and constants
│   ├── constants.py               # Colors, dimensions, speed settings
│   └── state.py                   # Global app state (array, speed, mode, etc.)
│
├── ui/                            # All UI components
│   ├── control_panel.py           # Top bar: mode tabs, algorithm dropdown, controls
│   ├── code_panel.py              # Right panel: live C++ code with line highlighting
│   ├── explanation_panel.py       # Right panel: plain-English step explanations
│   ├── status_bar.py              # Bottom bar: stats and status messages
│   ├── home_screen.py             # Welcome/landing screen
│   └── widgets.py                 # Reusable widgets: Button, Slider, Dropdown, TextInput
│
└── visualizer/                    # Visualization renderers
    ├── sorting_view.py            # Bar chart + colored number box footer
    └── pathfinding_view.py        # Interactive grid for BFS/DFS/Dijkstra
```

---

## 🎮 How to Use

### Sorting Algorithms

1. Select **Sorting** tab
2. Choose an algorithm from the dropdown
3. *(Optional)* Type your own array in the **Custom Array** field — e.g. `5, 3, 8, 1, 9` — and click **Apply**
4. Adjust the **Speed** slider to your preferred pace
5. Press **Start** and watch the visualization

### Search Algorithms (Binary Search / Linear Search)

1. Select **Sorting** tab → choose **Binary Search** or **Linear Search**
2. Type a **target value** in the search input and click **Set**
3. Press **Start** — the visualizer will show how the algorithm finds (or doesn't find) your value

### Pathfinding Algorithms

1. Select **Pathfinding** tab
2. Click **Set Start** then click a grid cell
3. Click **Set End** then click another grid cell
4. Click anywhere on the grid to draw walls
5. Choose **BFS**, **DFS**, or **Dijkstra** and press **Start**

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **Pygame 2** | Window, rendering, and event handling |
| **Generator functions** | Step-by-step algorithm execution |
| **MVC-inspired architecture** | Separation of state, logic, and rendering |

---

## 👥 Team

This project was developed as a **Software Development course project** at **Bangladesh University of Business and Technology (BUBT)**.

<table>
  <tr>
    <td align="center">
      <b>👑 Team Leader</b><br/>
      <b>Md Shajada Masum</b><br/>
      <i>Project Lead & Architecture</i>
    </td>
  </tr>
</table>

### Team Members

| Name | Role |
|---|---|
| **Jubayer Hossain Sojib** | Developer |
| **Jamil Joy** | Developer |
| **Shahriar Saikot** | Developer |
| **Sabur Aronno** | Developer |

---

## 📚 Algorithms Implemented

### Sorting & Searching

| Algorithm | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Linear Search | O(1) | O(n) | O(n) | O(1) |

### Pathfinding

| Algorithm | Shortest Path? | Time Complexity | Space |
|---|---|---|---|
| BFS | ✅ Yes (unweighted) | O(V + E) | O(V) |
| DFS | ❌ No | O(V + E) | O(V) |
| Dijkstra | ✅ Yes (weighted) | O((V + E) log V) | O(V) |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by **Team AlgoViz** — BUBT Software Development

*"The best way to understand an algorithm is to watch it work."*

</div>
