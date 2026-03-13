# AlgoViz — Algorithm Visualizer

A full-stack web platform for learning algorithms through interactive, step-by-step visualization.

**Frontend:** HTML + CSS + Vanilla JS  
**Backend:** Python + Flask REST API

---

## Project Structure

```
algo-visualizer/
├── backend/                    # Python Flask API
│   ├── app/
│   │   ├── __init__.py         # App factory (Flask + CORS)
│   │   ├── algorithms/
│   │   │   ├── sorting/        # bubble, insertion, selection, merge, quick
│   │   │   ├── searching/      # linear, binary
│   │   │   └── graph/          # bfs, dfs, dijkstra
│   │   ├── routes/
│   │   │   ├── algo_routes.py  # POST /api/algorithms/<name>
│   │   │   └── health_routes.py# GET  /api/health
│   │   └── utils/
│   │       └── step_generator.py
│   ├── tests/
│   │   ├── test_sorting.py
│   │   ├── test_searching.py
│   │   └── test_graph.py
│   ├── requirements.txt
│   └── run.py
│
└── frontend/
    ├── pages/
    │   ├── index.html          # Home page
    │   ├── visualizer.html     # Algorithm visualizer (3-panel layout)
    │   └── about.html          # About page
    ├── assets/
    │   ├── css/
    │   │   ├── global.css      # Shared styles, navbar, footer
    │   │   ├── home.css
    │   │   ├── visualizer.css
    │   │   └── about.css
    │   └── js/
    │       ├── api.js          # Backend API client
    │       ├── navbar.js       # Active link highlighting
    │       ├── home.js         # Demo bar animation + scroll reveal
    │       └── visualizer.js   # Full animation engine (works offline too)
    └── components/
        ├── navbar.html
        └── footer.html
```

---

## Quick Start

### Option A — Frontend only (no backend needed)
Just open `frontend/pages/index.html` in your browser. All 10 algorithms run entirely in the browser via the built-in JS engine.

### Option B — Full stack (Flask backend)

```bash
# 1. Set up backend
cd backend
pip install -r requirements.txt

# 2. Run Flask server
python run.py
# → http://localhost:5000

# 3. Open frontend
open frontend/pages/index.html
```

The frontend auto-detects the backend. If Flask is running, it switches to live API mode; otherwise it falls back to browser-based simulation.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/api/health` | Health check |
| `GET`  | `/api/algorithms` | List all algorithms + metadata |
| `POST` | `/api/algorithms/<name>` | Run algorithm, get steps |

### POST /api/algorithms/bubble_sort
```json
// Request
{ "array": [5, 3, 8, 1, 9, 2, 7] }

// Response
{
  "algorithm": "bubble_sort",
  "total": 47,
  "meta": { "best": "O(n)", "worst": "O(n²)", ... },
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
```json
// Request
{ "array": [3, 7, 1, 9, 4], "target": 7 }
```

### Supported algorithm names
`bubble_sort`, `insertion_sort`, `selection_sort`, `merge_sort`, `quick_sort`,  
`linear_search`, `binary_search`, `bfs`, `dfs`, `dijkstra`

---

## Running Tests

```bash
cd backend
pip install -r requirements.txt
python -m pytest tests/ -v
```

---

## Algorithms Implemented

### Sorting
| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

### Searching
| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

### Graph
| Algorithm | Time | Space |
|-----------|------|-------|
| BFS | O(V+E) | O(V) |
| DFS | O(V+E) | O(V) |
| Dijkstra | O(E log V) | O(V) |

---

## Features
- **Real-time animation** — every swap, comparison, and pointer move animated
- **Live code highlighting** — Python source highlights the active line each step
- **Step explanations** — plain-English description at every step
- **Full playback control** — Start / Pause / Step / Reset + speed slider (1x–10x)
- **Custom arrays** — enter your own or generate random
- **Offline-first** — works without the backend via browser JS engine
- **Graph canvas** — BFS/DFS/Dijkstra rendered on an interactive node canvas

---

## Tech Stack
- **Python 3.12** + **Flask 3.0** + **Flask-CORS**
- **HTML5** + **CSS3** (custom properties, grid, animations)
- **Vanilla JavaScript** (no frameworks)
- **Google Fonts** — Syne (display) + Space Mono (code/mono)
