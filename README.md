# AlgoViz Desktop — Algorithm Visualizer

**Python + Pygame** দিয়ে বানানো desktop application।
Web version এর মতো 3-panel layout:
```
[ CODE PANEL ] | [ VISUALIZATION ] | [ EXPLANATION ]
```

## 👥 Team
**Shajada Masum · Sabur · Sojib · Joy · Saikot**
*Department of Computer Science & Engineering*

---

## VS Code এ কিভাবে Run করবে (Step by Step)

### Step 1 — Project folder খোলো
```
File → Open Folder → algoviz folder select করো
```

### Step 2 — Terminal খোলো
```
View → Terminal   অথবা   Ctrl + `  (backtick)
```

### Step 3 — Pygame install করো (একবারই করতে হবে)
```bash
pip install pygame
```

### Step 4 — Run করো
```bash
python main.py
```

> ⚠️ যদি `python` কাজ না করে তাহলে `python3 main.py` লেখো

---

## Project Structure (কোন file কী কাজ করে)

```
algoviz/
│
├── main.py                  ← এখান থেকে শুরু হয় (Entry Point)
├── requirements.txt         ← pip install -r requirements.txt
│
├── core/                    ← মূল configuration
│   ├── constants.py         ← Window size, colors, সব constant
│   └── state.py             ← App এর সব data এক জায়গায়
│
├── algorithms/              ← Algorithm logic
│   ├── bubble_sort.py       ← Bubble Sort (generator)
│   ├── selection_sort.py    ← Selection Sort (generator)
│   ├── merge_sort.py        ← Merge Sort (generator)
│   ├── bfs.py               ← BFS Pathfinding (generator)
│   └── dijkstra.py          ← Dijkstra Pathfinding (generator)
│
├── ui/                      ← সব UI component
│   ├── home_screen.py       ← Home/Splash screen
│   ├── control_panel.py     ← উপরের control bar
│   ├── code_panel.py        ← বাম panel (Python code)
│   ├── explanation_panel.py ← ডান panel (step description)
│   ├── status_bar.py        ← নিচের status bar
│   └── widgets.py           ← Button, Dropdown, Slider
│
└── visualizer/              ← Animation renderer
    ├── sorting_view.py      ← Bar chart animation
    └── pathfinding_view.py  ← Grid animation
```

---

## Keyboard Shortcuts

| Key | কাজ |
|-----|-----|
| `ENTER` বা `SPACE` | Start / Pause / Resume |
| `H` | Home screen এ ফিরে যাও |
| `R` | Reset |
| `N` | নতুন random array |
| `-` | Speed কমাও |
| `=` | Speed বাড়াও |
| `ESC` | বন্ধ করো |

---

## Algorithm গুলো

### Sorting
| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

### Pathfinding
| Algorithm | Time | Space | বৈশিষ্ট্য |
|-----------|------|-------|--------|
| BFS | O(V+E) | O(V) | সবচেয়ে কম step এর path |
| Dijkstra | O(E log V) | O(V) | সবচেয়ে কম cost এর path |

---

## Color System

| রঙ | মানে |
|----|------|
| 🔵 Cyan | তুলনা হচ্ছে (1st element) |
| 🟡 Yellow | তুলনা হচ্ছে (2nd element) |
| 🔴 Red | Swap হচ্ছে |
| 🟢 Green | Sorted / Start node |
| 🟠 Orange | End node |
| 💙 Blue | Visited cell |
| 💜 Purple | Shortest path |

---

## সমস্যা হলে

**pygame not found:**
```bash
pip install pygame --upgrade
```

**python not recognized:**
```bash
python3 main.py
```

**Screen overlap হলে:**
Window টি drag করে সরাও অথবা constants.py তে
WIDTH ও HEIGHT কমাও।
