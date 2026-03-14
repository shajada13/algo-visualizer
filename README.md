# 🧠 AlgoViz — Interactive Algorithm Visualizer

<div align="center">

![AlgoViz Banner](https://img.shields.io/badge/AlgoViz-Algorithm%20Visualizer-00e5ff?style=for-the-badge&logo=python&logoColor=white)

**A full-stack interactive platform for learning algorithms through step-by-step visual animation.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Netlify-39ff14?style=flat-square&logo=netlify)](https://your-site.netlify.app)
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![HTML5](https://img.shields.io/badge/HTML5-CSS3-orange?style=flat-square&logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-yellow?style=flat-square&logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)](LICENSE)

</div>

---

## 👥 Team Members

<div align="center">

| # | Name | Role |
|---|------|------|
| 1 | **Shajada Masum** | Project Lead & Full-Stack Developer |
| 2 | **Sabur** | Backend Developer (Python / Flask) |
| 3 | **Sojib** | Frontend Developer (HTML / CSS) |
| 4 | **Joy** | Frontend Developer (JavaScript / Animation Engine) |
| 5 | **Saikot** | UI/UX Design & Testing |

</div>

---

## 📌 About the Project

**AlgoViz** is a web-based algorithm visualization platform that allows users to watch **sorting**, **searching**, and **graph algorithms** execute step by step in real time.

Instead of reading static pseudocode, you can:
- 👁️ **Watch** every comparison, swap, and pointer move animate live
- 📄 **See** the exact Python code line highlighted as it executes
- 📖 **Read** a plain-English explanation at every single step
- 🎛️ **Control** the speed and replay any step as many times as you need

> Built as a **university group project** to help students understand algorithms visually — because seeing is understanding.

---

## 🚀 Live Demo

> 🌐 **[View Live on Netlify →](https://your-site.netlify.app)**
>
> *(Replace this link with your actual Netlify URL after deploying)*

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ⚡ Real-Time Animation | Every swap, comparison & pointer move animated smoothly |
| 📄 Live Code Highlighting | Python source code highlights the active line each step |
| 📊 Sorting Algorithms | Bubble, Insertion, Selection, Merge, Quick Sort |
| 🔍 Searching Algorithms | Linear Search & Binary Search with custom target |
| 🕸️ Graph Algorithms | BFS, DFS, Dijkstra on an interactive node graph |
| ✏️ Custom Input Arrays | Enter your own array or generate a random one |
| 🎛️ Playback Controls | Start / Pause / Step / Reset + speed slider (1x–10x) |
| 📖 Step Explanations | Plain-English description of what's happening and why |
| 📱 Responsive Design | Works on desktop, tablet, and mobile |
| 🔌 Offline-First | Runs fully in the browser — no backend required |

---

## 🧮 Algorithms Implemented

### 📊 Sorting

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

### 🔍 Searching

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

### 🕸️ Graph

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| BFS (Breadth-First Search) | O(V + E) | O(V) |
| DFS (Depth-First Search) | O(V + E) | O(V) |
| Dijkstra's Algorithm | O(E log V) | O(V) |

---

## 🗂️ Project Structure

```
algo-visualizer/
│
├── index.html                  # 🏠 Home page  (Netlify root)
├── visualizer.html             # 🎯 Algorithm Visualizer — 3-panel layout
├── about.html                  # ℹ️  About page
├── netlify.toml                # ⚙️  Netlify deployment config
│
├── assets/
│   ├── css/
│   │   ├── global.css          # Shared styles — navbar, footer, variables
│   │   ├── home.css            # Home page styles
│   │   ├── visualizer.css      # Visualizer panel styles
│   │   └── about.css           # About page styles
│   └── js/
│       ├── api.js              # Flask API client (auto-detects backend)
│       ├── navbar.js           # Active link highlighting
│       ├── home.js             # Demo animation + scroll reveal
│       └── visualizer.js       # Full animation engine (works offline too)
│
├── components/
│   ├── navbar.html             # Reusable navbar snippet
│   └── footer.html             # Reusable footer snippet
│
└── backend/                    # Python Flask REST API
    ├── run.py                  # Entry point — start the server
    ├── requirements.txt        # pip dependencies
    ├── .env                    # Environment variables
    ├── app/
    │   ├── __init__.py         # Flask app factory + CORS setup
    │   ├── algorithms/
    │   │   ├── sorting/        # bubble, insertion, selection, merge, quick
    │   │   ├── searching/      # linear, binary
    │   │   └── graph/          # bfs, dfs, dijkstra
    │   ├── routes/
    │   │   ├── algo_routes.py  # POST /api/algorithms/<name>
    │   │   └── health_routes.py# GET  /api/health
    │   └── utils/
    │       └── step_generator.py
    └── tests/
        ├── test_sorting.py
        ├── test_searching.py
        └── test_graph.py
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Pages** | HTML5 | Structure & markup |
| **Styling** | CSS3 | Custom properties, grid, animations |
| **Logic** | Vanilla JavaScript | Animation engine, DOM, API calls |
| **Backend** | Python 3.12 + Flask 3.0 | REST API, algorithm step data |
| **CORS** | Flask-CORS | Allow frontend ↔ backend requests |
| **Fonts** | Google Fonts | Syne (display) + Space Mono (code) |
| **Hosting** | Netlify | Free frontend deployment |

</div>

> **No frontend frameworks used** — pure HTML, CSS, and JavaScript.
> This keeps the project simple, fast, and easy to understand line by line.

---

## ⚙️ Getting Started

### ▶️ Option A — Open Directly (No Install Needed)

The whole frontend works in your browser with **zero setup**:

1. Download or clone this repo
2. Open **`index.html`** in your browser
3. Done ✅ — all 10 algorithms run in the browser

---

### 🐍 Option B — Run with Flask Backend

**1. Clone the repository**
```bash
git clone https://github.com/your-username/algo-visualizer.git
cd algo-visualizer
```

**2. Install Python dependencies**
```bash
cd backend
pip install -r requirements.txt
```

**3. Start the backend server**
```bash
python run.py
```
Terminal output:
```
* Running on http://localhost:5000
* Debug mode: on
```

**4. Open the frontend**

Open `index.html` in your browser. The visualizer page will show:
```
✅ Backend connected — live API mode active
```

If Flask is not running, it automatically falls back to the built-in browser engine — everything still works.

---

## 🌐 Deploy to Netlify

### Method 1 — Drag & Drop (Fastest)
1. Go to [netlify.com](https://netlify.com) and log in
2. Click **"Add new site"** → **"Deploy manually"**
3. Drag the **entire project folder** onto the upload area
4. Live in seconds ✅

### Method 2 — GitHub Auto-Deploy
1. Push this repo to GitHub
2. Go to Netlify → **"Add new site"** → **"Import from Git"**
3. Connect your GitHub account and select this repo
4. Netlify reads `netlify.toml` automatically
5. Click **Deploy site** ✅

> After deploying, update the **Live Demo** badge link at the top of this README with your real Netlify URL.

---

## 🔌 API Reference

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/health` | Server health check |
| `GET` | `/api/algorithms` | List all algorithms + complexity data |
| `POST` | `/api/algorithms/<name>` | Run an algorithm, returns step data |

---

### POST /api/algorithms/bubble_sort

**Request body:**
```json
{
  "array": [5, 3, 8, 1, 9, 2, 7]
}
```

**Response:**
```json
{
  "algorithm": "bubble_sort",
  "total": 47,
  "meta": {
    "name": "Bubble Sort",
    "best": "O(n)",
    "avg": "O(n²)",
    "worst": "O(n²)",
    "space": "O(1)"
  },
  "steps": [
    {
      "array": [5, 3, 8, 1, 9, 2, 7],
      "active": 0,
      "compared": 1,
      "sorted": [],
      "code_line": 3,
      "text": "Comparing 5 and 3"
    },
    ...
  ]
}
```

### POST /api/algorithms/binary_search

**Request body:**
```json
{
  "array": [3, 7, 1, 9, 4],
  "target": 7
}
```

### All supported algorithm names

```
Sorting:   bubble_sort  insertion_sort  selection_sort  merge_sort  quick_sort
Searching: linear_search  binary_search
Graph:     bfs  dfs  dijkstra
```

---

## 🧪 Running Tests

```bash
cd backend
pip install -r requirements.txt
python -m pytest tests/ -v
```

Expected output:
```
tests/test_sorting.py    PASSED  [8 tests]
tests/test_searching.py  PASSED  [5 tests]
tests/test_graph.py      PASSED  [5 tests]

================== 18 passed in 0.42s ==================
```

---

## 🔮 Future Improvements

- [ ] A* Pathfinding algorithm
- [ ] Side-by-side algorithm comparison mode
- [ ] Live performance benchmark charts
- [ ] Tree visualizations (BST, AVL Tree, Heap)
- [ ] Dark / Light theme toggle
- [ ] Algorithm quiz and challenge mode
- [ ] Export animation as GIF or video
- [ ] User accounts to save progress

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-algorithm`)
3. Commit your changes (`git commit -m 'Add heap sort visualization'`)
4. Push to the branch (`git push origin feature/new-algorithm`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute for personal or educational purposes.

---

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/) — Python micro web framework
- [Google Fonts](https://fonts.google.com/) — Syne & Space Mono typefaces
- [Netlify](https://netlify.com/) — Free static site hosting
- [Shields.io](https://shields.io/) — README badges

---

<div align="center">

### 💻 Built with ❤️ by the AlgoViz Team

| 👤 Shajada Masum | 👤 Sabur | 👤 Sojib | 👤 Joy | 👤 Saikot |
|:-:|:-:|:-:|:-:|:-:|

<br/>

*Department of Computer Science & Engineering*

⭐ **Star this repo if you found it helpful!** ⭐

</div>
