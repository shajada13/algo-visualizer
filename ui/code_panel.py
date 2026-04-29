import pygame
from core.constants import (
    C_PANEL2, C_BORDER, C_CYAN, C_TEXT, C_TEXT_DIM, C_TEXT_MUTED,
    CODE_X, CANVAS_TOP, CODE_W, CANVAS_H,
)

CODE_LIBRARY = {
    "Bubble Sort": [
        "void bubbleSort(int a[], int n) {",
        "  for (int i=0; i<n-1; i++) {",
        "    bool swapped = false;",
        "    for (int j=0; j<n-i-1; j++) {",
        "      // Compare adjacent",
        "      if (a[j] > a[j+1]) {",
        "        swap(a[j], a[j+1]);",
        "        swapped = true;",
        "      }",
        "    }",
        "    if (!swapped) break;",
        "  }",
        "}",
    ],
    "Selection Sort": [
        "void selectionSort(int a[], int n) {",
        "  for (int i=0; i<n-1; i++) {",
        "    int min_idx = i;",
        "    for (int j=i+1; j<n; j++) {",
        "      // Scan for minimum",
        "      if (a[j] < a[min_idx])",
        "        min_idx = j;",
        "    }",
        "    // Place minimum at i",
        "    if (min_idx != i)",
        "      swap(a[i], a[min_idx]);",
        "  }",
        "}",
    ],
    "Insertion Sort": [
        "void insertionSort(int a[], int n) {",
        "  for (int i=1; i<n; i++) {",
        "    int key = a[i];",
        "    int j   = i - 1;",
        "    // Shift larger elements right",
        "    while (j>=0 && a[j]>key) {",
        "      a[j+1] = a[j];  // shift",
        "      j--;",
        "    }",
        "    // Insert key at correct pos",
        "    a[j+1] = key;",
        "  }",
        "}",
    ],
    "Merge Sort": [
        "void merge(int a[],int l,int m,int r){",
        "  int n1=m-l+1, n2=r-m;",
        "  int L[n1], R[n2];",
        "  for(int i=0;i<n1;i++) L[i]=a[l+i];",
        "  for(int j=0;j<n2;j++) R[j]=a[m+1+j];",
        "  int i=0,j=0,k=l;",
        "  while(i<n1 && j<n2) {",
        "    // Compare L and R",
        "    if(L[i]<=R[j]) a[k++]=L[i++];",
        "    else           a[k++]=R[j++];",
        "  }",
        "  while(i<n1) a[k++]=L[i++];",
        "  while(j<n2) a[k++]=R[j++];",
        "}",
        "void mergeSort(int a[],int l,int r){",
        "  if(l>=r) return;",
        "  int m=(l+r)/2;",
        "  mergeSort(a,l,m);",
        "  mergeSort(a,m+1,r);",
        "  merge(a,l,m,r);",
        "}",
    ],
    "Quick Sort": [
        "int partition(int a[],int lo,int hi){",
        "  int pivot = a[hi]; // last as pivot",
        "  int i = lo - 1;",
        "  for(int j=lo; j<hi; j++) {",
        "    // Compare with pivot",
        "    if(a[j] <= pivot) {",
        "      i++;",
        "      swap(a[i], a[j]); // to left",
        "    }",
        "  }",
        "  swap(a[i+1], a[hi]); // place pivot",
        "  return i + 1;",
        "}",
        "void quickSort(int a[],int lo,int hi){",
        "  if(lo >= hi) return;",
        "  int p = partition(a, lo, hi);",
        "  quickSort(a, lo, p-1);  // left",
        "  quickSort(a, p+1, hi);  // right",
        "}",
    ],
    "Binary Search": [
        "int binarySearch(int a[],int n,int t){",
        "  int lo=0, hi=n-1;",
        "  while(lo <= hi) {",
        "    int mid = (lo+hi) / 2;",
        "    // Check mid element",
        "    if(a[mid] == t)",
        "      return mid;     // found!",
        "    else if(a[mid] < t)",
        "      lo = mid + 1;   // right half",
        "    else",
        "      hi = mid - 1;   // left half",
        "  }",
        "  return -1; // not found",
        "}",
    ],
    "Linear Search": [
        "int linearSearch(int a[],int n,int t){",
        "  for(int i=0; i<n; i++) {",
        "    // Check each element",
        "    if(a[i] == t)",
        "      return i;   // found at i",
        "  }",
        "  return -1;      // not found",
        "}",
    ],
    "BFS": [
        "#include <queue>",
        "using namespace std;",
        "void bfs(Grid& g, Node start,",
        "         Node end) {",
        "  queue<Node> q;",
        "  set<Node> visited;",
        "  q.push(start);",
        "  visited.insert(start);",
        "  while(!q.empty()) {",
        "    Node cur = q.front(); q.pop();",
        "    if(cur==end) { reconstruct(); return; }",
        "    for(auto nb : neighbours(cur)) {",
        "      if(!visited.count(nb)) {",
        "        visited.insert(nb);",
        "        q.push(nb);",
        "      }",
        "    }",
        "  }",
        "}",
    ],
    "DFS": [
        "#include <stack>",
        "using namespace std;",
        "void dfs(Grid& g, Node start,",
        "         Node end) {",
        "  stack<Node> stk;",
        "  set<Node> visited;",
        "  stk.push(start);",
        "  while(!stk.empty()) {",
        "    Node cur = stk.top(); stk.pop();",
        "    if(visited.count(cur)) continue;",
        "    visited.insert(cur);",
        "    if(cur==end){ reconstruct(); return; }",
        "    // Go deeper (backtrack on dead end)",
        "    for(auto nb : neighbours(cur)) {",
        "      if(!visited.count(nb))",
        "        stk.push(nb);",
        "    }",
        "  }",
        "}",
    ],
    "Dijkstra": [
        "#include <queue>",
        "#include <climits>",
        "using namespace std;",
        "void dijkstra(Grid& g, Node s, Node e){",
        "  map<Node,int> dist;",
        "  priority_queue<pair<int,Node>,",
        "    vector<...>,greater<...>> pq;",
        "  dist[s]=0; pq.push({0,s});",
        "  while(!pq.empty()) {",
        "    auto [d,u]=pq.top(); pq.pop();",
        "    if(u==e){ reconstruct(); return; }",
        "    for(auto [v,w] : neighbours(u)) {",
        "      int nd = dist[u]+w;",
        "      if(nd < dist[v]) {",
        "        dist[v]=nd;",
        "        pq.push({nd,v});",
        "      }",
        "    }",
        "  }",
        "}",
    ],
}

HIGHLIGHT_MAP = {
    "Bubble Sort":    {"compare": 5, "swap": 6,  None: 3},
    "Selection Sort": {"compare": 5, "swap": 10, None: 2},
    "Insertion Sort": {"compare": 5, "swap": 6,  None: 2},
    "Merge Sort":     {"compare": 7, "swap": 8,  None: 6},
    "Quick Sort":     {"compare": 4, "swap": 6,  None: 1},
    "Binary Search":  {"compare": 4, "swap": 5,  None: 3},
    "Linear Search":  {"compare": 2, "swap": 3,  None: 1},
    "BFS":            {"visit": 13,  "path": 10, None: 9},
    "DFS":            {"visit": 14,  "path": 11, None: 8},
    "Dijkstra":       {"visit": 12,  "path": 9,  None: 8},
}

CPP_KEYWORDS = (
    "void", "int", "bool", "return", "for", "while", "if", "else",
    "true", "false", "auto", "using", "namespace", "std",
    "#include", "break", "map", "set", "queue", "stack",
    "vector", "pair", "continue",
)


class CodePanel:
    def __init__(self, state):
        self.state = state
        self.active_line = -1
        self.font_title = pygame.font.SysFont("Consolas", 13, bold=True)
        self.font_code  = pygame.font.SysFont("Consolas", 12)
        self.font_lnum  = pygame.font.SysFont("Consolas", 11)

    def set_line_from_stat(self, stat):
        m = HIGHLIGHT_MAP.get(self.state.algo_name, {})
        self.active_line = m.get(stat, m.get(None, -1))

    def draw(self, surface):
        pygame.draw.rect(surface, C_PANEL2,
                         pygame.Rect(CODE_X, CANVAS_TOP, CODE_W, CANVAS_H))
        pygame.draw.line(surface, C_BORDER,
                         (CODE_X + CODE_W, CANVAS_TOP),
                         (CODE_X + CODE_W, CANVAS_TOP + CANVAS_H))

        hh = 36
        pygame.draw.rect(surface, (12, 18, 32),
                         pygame.Rect(CODE_X, CANVAS_TOP, CODE_W, hh))
        pygame.draw.line(surface, C_BORDER,
                         (CODE_X, CANVAS_TOP + hh),
                         (CODE_X + CODE_W, CANVAS_TOP + hh))

        pygame.draw.circle(surface, (255, 107, 43),
                           (CODE_X + 14, CANVAS_TOP + hh // 2), 5)
        lbl = self.font_title.render("C++ CODE", True, C_TEXT_DIM)
        surface.blit(lbl, (CODE_X + 28, CANVAS_TOP + hh // 2 - lbl.get_height() // 2))

        lines  = CODE_LIBRARY.get(self.state.algo_name, [])
        line_h = 20
        sy     = CANVAS_TOP + hh + 6

        for i, line in enumerate(lines):
            y = sy + i * line_h
            if y + line_h > CANVAS_TOP + CANVAS_H:
                break
            active = (i == self.active_line)

            if active:
                pygame.draw.rect(surface, (60, 30, 0),
                                 pygame.Rect(CODE_X + 1, y - 1, CODE_W - 2, line_h),
                                 border_radius=3)
                pygame.draw.rect(surface, (255, 107, 43),
                                 pygame.Rect(CODE_X + 1, y - 1, 3, line_h),
                                 border_radius=2)

            ln = self.font_lnum.render(f"{i+1:2}", True,
                                       (255, 107, 43) if active else C_TEXT_MUTED)
            surface.blit(ln, (CODE_X + 6, y + 3))

            col = (255, 107, 43) if active else self._col(line)
            cs  = self.font_code.render(line, True, col)
            clip = pygame.Rect(CODE_X + 30, y, CODE_W - 34, line_h)
            surface.set_clip(clip)
            surface.blit(cs, (CODE_X + 30, y + 2))
            surface.set_clip(None)

    def _col(self, line):
        s = line.strip()
        if s.startswith("//") or s.startswith("#include"):
            return C_TEXT_MUTED
        for kw in CPP_KEYWORDS:
            if (s.startswith(kw + " ") or s.startswith(kw + "(")
                    or s.startswith(kw + "<") or s == kw):
                return (100, 180, 255)
        return C_TEXT_DIM
