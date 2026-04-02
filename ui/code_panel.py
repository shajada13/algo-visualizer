import pygame
from core.constants import (
    C_PANEL2, C_BORDER, C_CYAN, C_TEXT, C_TEXT_DIM, C_TEXT_MUTED,
    CODE_X, CANVAS_TOP, CODE_W, CANVAS_H,
)

CODE_LIBRARY = {
    "Bubble Sort": [
        "void bubbleSort(int arr[], int n) {",
        "  for (int i = 0; i < n-1; i++) {",
        "    bool swapped = false;",
        "    for (int j = 0; j < n-i-1; j++) {",
        "      // Compare adjacent elements",
        "      if (arr[j] > arr[j+1]) {",
        "        // Swap!",
        "        swap(arr[j], arr[j+1]);",
        "        swapped = true;",
        "      }",
        "    }",
        "    if (!swapped) break;",
        "  }",
        "}",
    ],
    "Selection Sort": [
        "void selectionSort(int arr[], int n) {",
        "  for (int i = 0; i < n-1; i++) {",
        "    int min_idx = i;",
        "    // Find minimum in rest",
        "    for (int j = i+1; j < n; j++) {",
        "      if (arr[j] < arr[min_idx]) {",
        "        min_idx = j;",
        "      }",
        "    }",
        "    // Swap min to position i",
        "    if (min_idx != i)",
        "      swap(arr[i], arr[min_idx]);",
        "  }",
        "}",
    ],
    "Merge Sort": [
        "void merge(int arr[], int l, int m, int r) {",
        "  int n1=m-l+1, n2=r-m;",
        "  int L[n1], R[n2];",
        "  for(int i=0;i<n1;i++) L[i]=arr[l+i];",
        "  for(int j=0;j<n2;j++) R[j]=arr[m+1+j];",
        "  int i=0, j=0, k=l;",
        "  while (i<n1 && j<n2) {",
        "    // Compare left and right",
        "    if (L[i] <= R[j])",
        "      arr[k++] = L[i++];",
        "    else",
        "      arr[k++] = R[j++];",
        "  }",
        "  while(i<n1) arr[k++]=L[i++];",
        "  while(j<n2) arr[k++]=R[j++];",
        "}",
        "void mergeSort(int arr[],int l,int r){",
        "  if (l >= r) return;",
        "  int m = (l+r)/2;",
        "  mergeSort(arr, l, m);",
        "  mergeSort(arr, m+1, r);",
        "  merge(arr, l, m, r);",
        "}",
    ],
    "BFS": [
        "#include <queue>",
        "using namespace std;",
        "",
        "void bfs(vector<vector<int>>& grid,",
        "         pair<int,int> start,",
        "         pair<int,int> end) {",
        "  queue<pair<int,int>> q;",
        "  set<pair<int,int>> visited;",
        "  q.push(start);",
        "  visited.insert(start);",
        "  while (!q.empty()) {",
        "    auto node = q.front(); q.pop();",
        "    if (node == end) return;",
        "    for (auto nb : neighbours(node)) {",
        "      if (!visited.count(nb)) {",
        "        visited.insert(nb);",
        "        q.push(nb);",
        "      }",
        "    }",
        "  }",
        "}",
    ],
    "Dijkstra": [
        "#include <queue>",
        "#include <climits>",
        "using namespace std;",
        "",
        "void dijkstra(vector<vector<int>>& g,",
        "    pair<int,int> start, pair<int,int> end){",
        "  map<pair<int,int>,int> dist;",
        "  priority_queue<pair<int,pair<int,int>>,",
        "    vector<...>,greater<...>> pq;",
        "  dist[start] = 0;",
        "  pq.push({0, start});",
        "  while (!pq.empty()) {",
        "    auto [d, u] = pq.top(); pq.pop();",
        "    if (u == end) return;",
        "    for (auto [v,w] : neighbours(u)) {",
        "      int nd = dist[u] + w;",
        "      if (nd < dist[v]) {",
        "        dist[v] = nd;",
        "        pq.push({nd, v});",
        "      }",
        "    }",
        "  }",
        "}",
    ],
}

HIGHLIGHT_MAP = {
    "Bubble Sort":    {"compare": 5, "swap": 7,  None: 3},
    "Selection Sort": {"compare": 5, "swap": 10, None: 2},
    "Merge Sort":     {"compare": 8, "swap": 9,  None: 6},
    "BFS":            {"visit": 15,  "path": 12, None: 11},
    "Dijkstra":       {"visit": 16,  "path": 13, None: 12},
}

CPP_KEYWORDS = (
    "void", "int", "bool", "return", "for", "while", "if", "else",
    "true", "false", "auto", "using", "namespace", "std", "#include",
    "break", "map", "set", "queue", "vector", "pair", "#include",
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

        # Orange dot + "C++ CODE" label
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
            if s.startswith(kw + " ") or s.startswith(kw + "(") or s == kw:
                return (100, 180, 255)
        return C_TEXT_DIM
