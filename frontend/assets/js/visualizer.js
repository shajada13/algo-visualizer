// ─── ALGORITHM VISUALIZER ENGINE ───

// Prevent any external syntax highlighter (browser extensions, Highlight.js,
// Prism.js injected by dev tools) from touching our code panel and throwing
// "Code language not supported or defined" errors.
(function disableExternalHighlighters() {
  if (window.hljs) window.hljs.configure({ languages: [] });
  if (window.Prism) window.Prism.manual = true;
  document.addEventListener('DOMContentLoaded', () => {
    if (window.hljs) window.hljs.configure({ languages: [] });
    if (window.Prism) window.Prism.manual = true;
  });
})();

// ─── ALGORITHM METADATA ───
const ALGOS = {
  bubble_sort: {
    name: 'Bubble Sort', category: 'sorting',
    best: 'O(n)', avg: 'O(n²)', worst: 'O(n²)', space: 'O(1)',
    timeTag: 'O(n²) time', spaceTag: 'O(1) space',
    code: [
      'def bubble_sort(arr):',
      '    n = len(arr)',
      '    for i in range(n):',
      '        for j in range(0, n-i-1):',
      '            # Compare adjacent elements',
      '            if arr[j] > arr[j+1]:',
      '                # Swap if out of order',
      '                arr[j], arr[j+1] = arr[j+1], arr[j]',
      '    return arr',
    ]
  },
  insertion_sort: {
    name: 'Insertion Sort', category: 'sorting',
    best: 'O(n)', avg: 'O(n²)', worst: 'O(n²)', space: 'O(1)',
    timeTag: 'O(n²) time', spaceTag: 'O(1) space',
    code: [
      'def insertion_sort(arr):',
      '    for i in range(1, len(arr)):',
      '        key = arr[i]',
      '        j = i - 1',
      '        # Shift elements greater than key',
      '        while j >= 0 and arr[j] > key:',
      '            arr[j+1] = arr[j]',
      '            j -= 1',
      '        arr[j+1] = key',
      '    return arr',
    ]
  },
  selection_sort: {
    name: 'Selection Sort', category: 'sorting',
    best: 'O(n²)', avg: 'O(n²)', worst: 'O(n²)', space: 'O(1)',
    timeTag: 'O(n²) time', spaceTag: 'O(1) space',
    code: [
      'def selection_sort(arr):',
      '    n = len(arr)',
      '    for i in range(n):',
      '        min_idx = i',
      '        # Find minimum element',
      '        for j in range(i+1, n):',
      '            if arr[j] < arr[min_idx]:',
      '                min_idx = j',
      '        # Swap minimum to front',
      '        arr[i], arr[min_idx] = arr[min_idx], arr[i]',
      '    return arr',
    ]
  },
  merge_sort: {
    name: 'Merge Sort', category: 'sorting',
    best: 'O(n log n)', avg: 'O(n log n)', worst: 'O(n log n)', space: 'O(n)',
    timeTag: 'O(n log n) time', spaceTag: 'O(n) space',
    code: [
      'def merge_sort(arr):',
      '    if len(arr) <= 1:',
      '        return arr',
      '    mid = len(arr) // 2',
      '    left = merge_sort(arr[:mid])',
      '    right = merge_sort(arr[mid:])',
      '    return merge(left, right)',
      '',
      'def merge(left, right):',
      '    result = []',
      '    i = j = 0',
      '    while i < len(left) and j < len(right):',
      '        if left[i] <= right[j]:',
      '            result.append(left[i]); i += 1',
      '        else:',
      '            result.append(right[j]); j += 1',
      '    return result + left[i:] + right[j:]',
    ]
  },
  quick_sort: {
    name: 'Quick Sort', category: 'sorting',
    best: 'O(n log n)', avg: 'O(n log n)', worst: 'O(n²)', space: 'O(log n)',
    timeTag: 'O(n log n) avg', spaceTag: 'O(log n) space',
    code: [
      'def quick_sort(arr, low, high):',
      '    if low < high:',
      '        pivot_idx = partition(arr, low, high)',
      '        quick_sort(arr, low, pivot_idx-1)',
      '        quick_sort(arr, pivot_idx+1, high)',
      '',
      'def partition(arr, low, high):',
      '    pivot = arr[high]  # Choose last as pivot',
      '    i = low - 1',
      '    for j in range(low, high):',
      '        if arr[j] <= pivot:',
      '            i += 1',
      '            arr[i], arr[j] = arr[j], arr[i]',
      '    arr[i+1], arr[high] = arr[high], arr[i+1]',
      '    return i + 1',
    ]
  },
  linear_search: {
    name: 'Linear Search', category: 'searching',
    best: 'O(1)', avg: 'O(n)', worst: 'O(n)', space: 'O(1)',
    timeTag: 'O(n) time', spaceTag: 'O(1) space',
    code: [
      'def linear_search(arr, target):',
      '    for i in range(len(arr)):',
      '        # Check each element',
      '        if arr[i] == target:',
      '            return i  # Found!',
      '    return -1  # Not found',
    ]
  },
  binary_search: {
    name: 'Binary Search', category: 'searching',
    best: 'O(1)', avg: 'O(log n)', worst: 'O(log n)', space: 'O(1)',
    timeTag: 'O(log n) time', spaceTag: 'O(1) space',
    code: [
      'def binary_search(arr, target):',
      '    low, high = 0, len(arr) - 1',
      '    while low <= high:',
      '        mid = (low + high) // 2',
      '        if arr[mid] == target:',
      '            return mid  # Found!',
      '        elif arr[mid] < target:',
      '            low = mid + 1',
      '        else:',
      '            high = mid - 1',
      '    return -1  # Not found',
    ]
  },
  bfs: {
    name: 'Breadth-First Search', category: 'graph',
    best: 'O(V+E)', avg: 'O(V+E)', worst: 'O(V+E)', space: 'O(V)',
    timeTag: 'O(V+E) time', spaceTag: 'O(V) space',
    code: [
      'from collections import deque',
      '',
      'def bfs(graph, start):',
      '    visited = set()',
      '    queue = deque([start])',
      '    visited.add(start)',
      '    order = []',
      '    while queue:',
      '        node = queue.popleft()',
      '        order.append(node)',
      '        for neighbor in graph[node]:',
      '            if neighbor not in visited:',
      '                visited.add(neighbor)',
      '                queue.append(neighbor)',
      '    return order',
    ]
  },
  dfs: {
    name: 'Depth-First Search', category: 'graph',
    best: 'O(V+E)', avg: 'O(V+E)', worst: 'O(V+E)', space: 'O(V)',
    timeTag: 'O(V+E) time', spaceTag: 'O(V) space',
    code: [
      'def dfs(graph, start, visited=None):',
      '    if visited is None:',
      '        visited = set()',
      '    visited.add(start)',
      '    order = [start]',
      '    for neighbor in graph[start]:',
      '        if neighbor not in visited:',
      '            order += dfs(graph,',
      '                         neighbor,',
      '                         visited)',
      '    return order',
    ]
  },
  dijkstra: {
    name: "Dijkstra's Algorithm", category: 'graph',
    best: 'O(E log V)', avg: 'O(E log V)', worst: 'O(E log V)', space: 'O(V)',
    timeTag: 'O(E log V) time', spaceTag: 'O(V) space',
    code: [
      'import heapq',
      '',
      'def dijkstra(graph, start):',
      '    dist = {v: float("inf") for v in graph}',
      '    dist[start] = 0',
      '    pq = [(0, start)]',
      '    while pq:',
      '        d, u = heapq.heappop(pq)',
      '        if d > dist[u]: continue',
      '        for v, w in graph[u]:',
      '            if dist[u] + w < dist[v]:',
      '                dist[v] = dist[u] + w',
      '                heapq.heappush(pq, (dist[v], v))',
      '    return dist',
    ]
  },
};

// ─── CATEGORY → ALGO OPTIONS ───
const CATEGORY_OPTIONS = {
  sorting: ['bubble_sort','insertion_sort','selection_sort','merge_sort','quick_sort'],
  searching: ['linear_search','binary_search'],
  graph: ['bfs','dfs','dijkstra'],
};

// ─── IN-BROWSER STEP GENERATORS ───
function generateBubbleSortSteps(arr) {
  const a = [...arr]; const steps = [];
  const n = a.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      steps.push({ arr:[...a], active:j, compared:j+1, sorted:Array.from({length:i},(_,k)=>n-1-k),
        codeLine:3, text:`Comparing <strong>${a[j]}</strong> and <strong>${a[j+1]}</strong>` });
      if (a[j] > a[j+1]) {
        [a[j],a[j+1]] = [a[j+1],a[j]];
        steps.push({ arr:[...a], active:j+1, compared:j, sorted:Array.from({length:i},(_,k)=>n-1-k),
          codeLine:7, text:`<strong>${a[j+1]}</strong> > <strong>${a[j]}</strong> — Swapped! ↕` });
      }
    }
    steps.push({ arr:[...a], active:-1, compared:-1, sorted:Array.from({length:i+1},(_,k)=>n-1-k),
      codeLine:2, text:`Pass ${i+1} complete. Element <strong>${a[n-1-i]}</strong> is in its final position ✓` });
  }
  steps.push({ arr:[...a], active:-1, compared:-1, sorted:[...Array(n).keys()], codeLine:8,
    text:'✓ Array is fully sorted!' });
  return steps;
}

function generateInsertionSortSteps(arr) {
  const a = [...arr]; const steps = [];
  for (let i = 1; i < a.length; i++) {
    const key = a[i];
    steps.push({ arr:[...a], active:i, compared:-1, sorted:[], codeLine:2, text:`Picking key = <strong>${key}</strong> at index ${i}` });
    let j = i - 1;
    while (j >= 0 && a[j] > key) {
      steps.push({ arr:[...a], active:j+1, compared:j, sorted:[], codeLine:5, text:`<strong>${a[j]}</strong> > <strong>${key}</strong> — Shifting ${a[j]} right` });
      a[j+1] = a[j]; j--;
    }
    a[j+1] = key;
    steps.push({ arr:[...a], active:j+1, compared:-1, sorted:[], codeLine:8, text:`Inserted <strong>${key}</strong> at position ${j+1}` });
  }
  steps.push({ arr:[...a], active:-1, compared:-1, sorted:[...Array(a.length).keys()], codeLine:9, text:'✓ Array is fully sorted!' });
  return steps;
}

function generateSelectionSortSteps(arr) {
  const a = [...arr]; const steps = []; const n = a.length;
  for (let i = 0; i < n; i++) {
    let minIdx = i;
    steps.push({ arr:[...a], active:i, compared:-1, sorted:[...Array(i).keys()], codeLine:3, text:`Looking for minimum in range [${i}..${n-1}]` });
    for (let j = i+1; j < n; j++) {
      steps.push({ arr:[...a], active:minIdx, compared:j, sorted:[...Array(i).keys()], codeLine:5,
        text:`Comparing current min <strong>${a[minIdx]}</strong> with <strong>${a[j]}</strong>` });
      if (a[j] < a[minIdx]) { minIdx = j;
        steps.push({ arr:[...a], active:minIdx, compared:-1, sorted:[...Array(i).keys()], codeLine:6, text:`New minimum found: <strong>${a[minIdx]}</strong>` }); }
    }
    [a[i],a[minIdx]] = [a[minIdx],a[i]];
    steps.push({ arr:[...a], active:i, compared:-1, sorted:[...Array(i+1).keys()], codeLine:9, text:`Placed <strong>${a[i]}</strong> at position ${i} ✓` });
  }
  return steps;
}

function generateMergeSortSteps(arr) {
  const steps = [];
  function mergeSort(a, offset=0) {
    if (a.length <= 1) return a;
    const mid = Math.floor(a.length/2);
    steps.push({ arr:[...arr], highlight:Array.from({length:a.length},(_,i)=>i+offset), codeLine:3, active:-1, compared:-1, sorted:[],
      text:`Splitting array of ${a.length} elements at midpoint (index ${mid})` });
    const left = mergeSort(a.slice(0,mid), offset);
    const right = mergeSort(a.slice(mid), offset+mid);
    const merged = [];
    let i=0,j=0;
    while(i<left.length && j<right.length){
      if(left[i]<=right[j]){ merged.push(left[i]); i++; }
      else { merged.push(right[j]); j++; }
    }
    const result = [...merged,...left.slice(i),...right.slice(j)];
    for(let k=0;k<result.length;k++) arr[offset+k]=result[k];
    steps.push({ arr:[...arr], highlight:Array.from({length:result.length},(_,i)=>i+offset), codeLine:16, active:-1, compared:-1, sorted:[],
      text:`Merged subarray → [${result.join(', ')}]` });
    return result;
  }
  mergeSort([...arr]);
  steps.push({ arr:[...arr.slice().sort((a,b)=>a-b)], active:-1, compared:-1, sorted:[...Array(arr.length).keys()], codeLine:6, text:'✓ Merge sort complete!' });
  return steps;
}

function generateQuickSortSteps(arr) {
  const a = [...arr]; const steps = [];
  function partition(low, high) {
    const pivot = a[high];
    steps.push({ arr:[...a], active:high, compared:-1, sorted:[], codeLine:7, text:`Pivot selected: <strong>${pivot}</strong> (index ${high})` });
    let i = low - 1;
    for (let j = low; j < high; j++) {
      steps.push({ arr:[...a], active:j, compared:high, sorted:[], codeLine:9, text:`Comparing <strong>${a[j]}</strong> with pivot <strong>${pivot}</strong>` });
      if (a[j] <= pivot) { i++; [a[i],a[j]]=[a[j],a[i]];
        steps.push({ arr:[...a], active:i, compared:j, sorted:[], codeLine:12, text:`<strong>${a[i]}</strong> ≤ pivot — swapping to left partition` }); }
    }
    [a[i+1],a[high]]=[a[high],a[i+1]];
    steps.push({ arr:[...a], active:i+1, compared:-1, sorted:[i+1], codeLine:13, text:`Pivot <strong>${pivot}</strong> placed at final position ${i+1} ✓` });
    return i+1;
  }
  function qs(low, high) {
    if (low < high) { const pi = partition(low, high); qs(low,pi-1); qs(pi+1,high); }
  }
  qs(0, a.length-1);
  steps.push({ arr:[...a], active:-1, compared:-1, sorted:[...Array(a.length).keys()], codeLine:4, text:'✓ Quick sort complete!' });
  return steps;
}

function generateLinearSearchSteps(arr, target) {
  const steps = [];
  steps.push({ arr:[...arr], active:-1, compared:-1, sorted:[], found:-1, codeLine:0, text:`Searching for <strong>${target}</strong> using linear scan...` });
  for (let i=0;i<arr.length;i++) {
    steps.push({ arr:[...arr], active:i, compared:-1, sorted:[], found:-1, codeLine:2, text:`Checking index ${i}: <strong>${arr[i]}</strong> === <strong>${target}</strong>?` });
    if (arr[i]===target) {
      steps.push({ arr:[...arr], active:-1, compared:-1, sorted:[], found:i, codeLine:3, text:`🎉 Found <strong>${target}</strong> at index <strong>${i}</strong>!` });
      return steps;
    }
    steps.push({ arr:[...arr], active:-1, compared:i, sorted:[], found:-1, codeLine:1, text:`<strong>${arr[i]}</strong> ≠ <strong>${target}</strong> — moving to next element` });
  }
  steps.push({ arr:[...arr], active:-1, compared:-1, sorted:[], found:-1, codeLine:5, text:`❌ <strong>${target}</strong> not found in array.` });
  return steps;
}

function generateBinarySearchSteps(arr, target) {
  const sorted = [...arr].sort((a,b)=>a-b);
  const steps = [];
  steps.push({ arr:[...sorted], active:-1, compared:-1, sorted:[], found:-1, codeLine:0, text:`Array sorted for binary search. Searching for <strong>${target}</strong>...` });
  let low=0, high=sorted.length-1;
  while (low<=high) {
    const mid = Math.floor((low+high)/2);
    steps.push({ arr:[...sorted], active:mid, compared:-1, range:[low,high], found:-1, codeLine:3,
      text:`Range [${low}..${high}] — Checking midpoint index ${mid}: <strong>${sorted[mid]}</strong>` });
    if (sorted[mid]===target) {
      steps.push({ arr:[...sorted], active:-1, compared:-1, sorted:[], found:mid, codeLine:4, text:`🎉 Found <strong>${target}</strong> at index <strong>${mid}</strong>!` });
      return steps;
    } else if (sorted[mid]<target) {
      steps.push({ arr:[...sorted], active:mid, compared:-1, range:[low,high], found:-1, codeLine:6, text:`<strong>${sorted[mid]}</strong> < <strong>${target}</strong> — Eliminate left half, search right` });
      low = mid+1;
    } else {
      steps.push({ arr:[...sorted], active:mid, compared:-1, range:[low,high], found:-1, codeLine:8, text:`<strong>${sorted[mid]}</strong> > <strong>${target}</strong> — Eliminate right half, search left` });
      high = mid-1;
    }
  }
  steps.push({ arr:[...sorted], active:-1, compared:-1, sorted:[], found:-1, codeLine:9, text:`❌ <strong>${target}</strong> not found.` });
  return steps;
}

function generateGraphSteps(algoKey) {
  const nodes = ['A','B','C','D','E','F'];
  const edges = { A:['B','C'], B:['A','D','E'], C:['A','F'], D:['B'], E:['B','F'], F:['C','E'] };
  const steps = [];
  if (algoKey === 'bfs') {
    const visited = new Set(); const queue = ['A']; const order = [];
    visited.add('A');
    steps.push({ nodes:[...nodes], visited:[...visited], current:null, queue:[...queue], codeLine:4, text:`Initialize BFS from node <strong>A</strong>. Add A to queue.` });
    while (queue.length) {
      const node = queue.shift(); order.push(node);
      steps.push({ nodes:[...nodes], visited:[...visited], current:node, queue:[...queue], codeLine:8, text:`Dequeue <strong>${node}</strong> — visit it. BFS order so far: [${order.join(', ')}]` });
      for (const n of edges[node]) {
        if (!visited.has(n)) { visited.add(n); queue.push(n);
          steps.push({ nodes:[...nodes], visited:[...visited], current:node, queue:[...queue], codeLine:12, text:`Neighbor <strong>${n}</strong> not visited — add to queue` }); }
      }
    }
    steps.push({ nodes:[...nodes], visited:[...visited], current:null, queue:[], codeLine:13, text:`✓ BFS complete! Traversal order: [${order.join(' → ')}]` });
  } else if (algoKey === 'dfs') {
    const visited = new Set(); const order = [];
    function dfs(node) {
      visited.add(node); order.push(node);
      steps.push({ nodes:[...nodes], visited:[...visited], current:node, queue:[], codeLine:3, text:`Visit <strong>${node}</strong>. DFS order: [${order.join(', ')}]` });
      for (const n of edges[node]) {
        if (!visited.has(n)) {
          steps.push({ nodes:[...nodes], visited:[...visited], current:node, queue:[], codeLine:5, text:`Exploring edge ${node}→<strong>${n}</strong>` });
          dfs(n);
        }
      }
    }
    dfs('A');
    steps.push({ nodes:[...nodes], visited:[...visited], current:null, queue:[], codeLine:9, text:`✓ DFS complete! Traversal order: [${order.join(' → ')}]` });
  } else {
    steps.push({ nodes:[...nodes], visited:new Set(['A']), current:'A', queue:[], codeLine:2,
      text:`Dijkstra from A: Initialize distances. dist[A]=0, all others=∞` });
    steps.push({ nodes:[...nodes], visited:new Set(['A','B']), current:'B', queue:[], codeLine:7, text:`Process A → B (cost 1). Update dist[B]=1` });
    steps.push({ nodes:[...nodes], visited:new Set(['A','B','C']), current:'C', queue:[], codeLine:7, text:`Process A → C (cost 4). Update dist[C]=4` });
    steps.push({ nodes:[...nodes], visited:new Set(['A','B','C','D']), current:'D', queue:[], codeLine:9, text:`Process B → D (cost 1+2=3). Update dist[D]=3` });
    steps.push({ nodes:[...nodes], visited:new Set(['A','B','C','D','E']), current:'E', queue:[], codeLine:9, text:`Process B → E (cost 1+3=4). Update dist[E]=4` });
    steps.push({ nodes:[...nodes], visited:new Set(nodes), current:'F', queue:[], codeLine:11, text:`✓ Dijkstra complete! All shortest paths computed.` });
  }
  return steps;
}

// ─── GRAPH RENDERER ───
function renderGraph(step, canvas, algoKey) {
  const ctx = canvas.getContext('2d');
  const W = canvas.width = canvas.offsetWidth;
  const H = canvas.height = canvas.offsetHeight || 300;
  ctx.clearRect(0,0,W,H);
  const nodePos = {
    A:[W*0.5, H*0.15], B:[W*0.25, H*0.42], C:[W*0.75, H*0.42],
    D:[W*0.1, H*0.72], E:[W*0.4, H*0.72], F:[W*0.72, H*0.72]
  };
  const edgeDefs = [['A','B'],['A','C'],['B','D'],['B','E'],['C','F'],['E','F']];
  // Draw edges
  ctx.lineWidth = 2;
  edgeDefs.forEach(([a,b]) => {
    ctx.beginPath();
    ctx.moveTo(...nodePos[a]); ctx.lineTo(...nodePos[b]);
    ctx.strokeStyle = '#1e2d45'; ctx.stroke();
  });
  // Draw nodes
  const nodes = ['A','B','C','D','E','F'];
  nodes.forEach(n => {
    const [x,y] = nodePos[n];
    const isVisited = step.visited instanceof Set ? step.visited.has(n) : (step.visited||[]).includes(n);
    const isCurrent = step.current === n;
    ctx.beginPath();
    ctx.arc(x, y, 22, 0, Math.PI*2);
    ctx.fillStyle = isCurrent ? '#00e5ff' : isVisited ? '#39ff14' : '#1e2d45';
    ctx.fill();
    ctx.strokeStyle = isCurrent ? '#00e5ff' : isVisited ? '#39ff1499' : '#2a4070';
    ctx.lineWidth = 2; ctx.stroke();
    ctx.fillStyle = isCurrent ? '#080c12' : isVisited ? '#080c12' : '#8899bb';
    ctx.font = 'bold 14px Space Mono, monospace';
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText(n, x, y);
  });
}

// ─── STATE ───
let currentAlgo = 'bubble_sort';
let steps = [];
let stepIndex = 0;
let isRunning = false;
let isPaused = false;
let animTimer = null;
let currentArray = [8,3,6,1,9,2,7,4];

// ─── ELEMENTS ───
const categorySelect = document.getElementById('categorySelect');
const algoSelect = document.getElementById('algoSelect');
const barContainer = document.getElementById('barContainer');
const graphCanvas = document.getElementById('graphCanvas');
const codePanel = document.getElementById('codePanel');
const stepText = document.getElementById('stepText');
const stepNum = document.getElementById('stepNum');
const totalSteps = document.getElementById('totalSteps');
const stepLog = document.getElementById('stepLog');
const algoTitleDisplay = document.getElementById('algoTitleDisplay');
const algoComplexity = document.getElementById('algoComplexity');
const statusBadge = document.getElementById('statusBadge');
const startBtn = document.getElementById('startBtn');
const pauseBtn = document.getElementById('pauseBtn');
const stepBtn = document.getElementById('stepBtn');
const resetBtn = document.getElementById('resetBtn');
const speedSlider = document.getElementById('speedSlider');
const speedLabel = document.getElementById('speedLabel');
const arrayInput = document.getElementById('arrayInput');
const searchInputRow = document.getElementById('searchInputRow');
const searchTarget = document.getElementById('searchTarget');
const bestCase = document.getElementById('bestCase');
const avgCase = document.getElementById('avgCase');
const worstCase = document.getElementById('worstCase');
const spaceCase = document.getElementById('spaceCase');

// ─── INIT ───
function init() {
  updateAlgoOptions();
  loadAlgo();
  renderBars(currentArray, {active:-1, compared:-1, sorted:[], found:-1});
  // URL params
  const params = new URLSearchParams(location.search);
  if (params.get('algo')) {
    const a = params.get('algo');
    const meta = ALGOS[a];
    if (meta) {
      categorySelect.value = meta.category;
      updateAlgoOptions();
      algoSelect.value = a;
      loadAlgo();
    }
  }
  if (params.get('category')) {
    categorySelect.value = params.get('category');
    updateAlgoOptions();
    loadAlgo();
  }
}

function updateAlgoOptions() {
  const cat = categorySelect.value;
  const opts = CATEGORY_OPTIONS[cat];
  algoSelect.innerHTML = opts.map(k => `<option value="${k}">${ALGOS[k].name}</option>`).join('');
  searchInputRow.classList.toggle('visible', cat === 'searching');
}

function loadAlgo() {
  currentAlgo = algoSelect.value;
  const meta = ALGOS[currentAlgo];
  algoTitleDisplay.textContent = meta.name;
  algoComplexity.innerHTML = `<span class="tag tag-cyan">${meta.timeTag}</span><span class="tag tag-orange">${meta.spaceTag}</span>`;
  bestCase.textContent = meta.best;
  avgCase.textContent = meta.avg;
  worstCase.textContent = meta.worst;
  spaceCase.textContent = meta.space;
  renderCode(meta.code, -1);
  resetViz();

  const isGraph = meta.category === 'graph';
  barContainer.style.display = isGraph ? 'none' : 'flex';
  graphCanvas.style.display = isGraph ? 'block' : 'none';
  if (isGraph) setTimeout(() => renderGraph({ nodes:[], visited:new Set(), current:null }, graphCanvas, currentAlgo), 50);
}

function renderCode(lines, activeLine) {
  // Use a plain <pre> wrapper — prevents any browser extension or
  // external syntax highlighter (Prism, Highlight.js, etc.) from
  // throwing "Code language not supported or defined" errors.
  const rows = lines.map((line, i) => {
    const cls = i === activeLine ? 'code-line highlight' : 'code-line';
    // Escape HTML entities so < > & render as text, not markup
    const safe = line
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      // Preserve leading spaces using non-breaking space trick inside <pre>
      || '&nbsp;';
    const lineNum = String(i + 1).padStart(2, ' ');
    return `<div class="${cls}" data-line="${i}"><span class="ln">${lineNum}</span>${safe}</div>`;
  }).join('');

  // nohighlight class tells Highlight.js to skip this block
  // data-highlighted tells some extensions it's already processed
  codePanel.innerHTML = `<pre class="nohighlight" data-highlighted="yes" style="margin:0;background:transparent;padding:0;">${rows}</pre>`;
}

function renderBars(arr, step) {
  if (!arr || !arr.length) return;
  const max = Math.max(...arr);
  barContainer.innerHTML = arr.map((val, i) => {
    let cls = 'bar default';
    if (step.found === i) cls = 'bar found';
    else if (i === step.active) cls = 'bar active';
    else if (i === step.compared) cls = 'bar compared';
    else if ((step.sorted||[]).includes(i)) cls = 'bar sorted';
    else if ((step.highlight||[]).includes(i)) cls = 'bar compared';
    const pct = Math.max(4, (val / max) * 100);
    return `<div class="${cls}" style="height:${pct}%"><span class="bar-val">${val}</span></div>`;
  }).join('');
}

function applyStep(s) {
  const meta = ALGOS[currentAlgo];
  const isGraph = meta.category === 'graph';
  if (!isGraph) renderBars(s.arr, s);
  else renderGraph(s, graphCanvas, currentAlgo);
  renderCode(meta.code, s.codeLine);
  stepText.innerHTML = s.text || '';
  stepNum.textContent = stepIndex + 1;
  const entry = document.createElement('div');
  entry.className = 'log-entry new';
  entry.textContent = `[${stepIndex+1}] ${(s.text||'').replace(/<[^>]*>/g,'')}`;
  stepLog.prepend(entry);
  setTimeout(() => entry.classList.remove('new'), 600);
  if (stepLog.children.length > 20) stepLog.removeChild(stepLog.lastChild);
}

function generateSteps() {
  const meta = ALGOS[currentAlgo];
  stepLog.innerHTML = '';
  if (meta.category === 'graph') return generateGraphSteps(currentAlgo);
  const target = parseInt(searchTarget.value) || 7;
  switch (currentAlgo) {
    case 'bubble_sort':    return generateBubbleSortSteps([...currentArray]);
    case 'insertion_sort': return generateInsertionSortSteps([...currentArray]);
    case 'selection_sort': return generateSelectionSortSteps([...currentArray]);
    case 'merge_sort':     return generateMergeSortSteps([...currentArray]);
    case 'quick_sort':     return generateQuickSortSteps([...currentArray]);
    case 'linear_search':  return generateLinearSearchSteps([...currentArray], target);
    case 'binary_search':  return generateBinarySearchSteps([...currentArray], target);
    default: return [];
  }
}

function setStatus(s) {
  statusBadge.className = 'status-badge status-'+s;
  statusBadge.textContent = { idle:'● Idle', running:'● Running', done:'● Done', paused:'⏸ Paused' }[s];
}

function getDelay() { return Math.round(1200 / parseInt(speedSlider.value)); }

function runStep() {
  if (stepIndex >= steps.length) { finish(); return; }
  applyStep(steps[stepIndex]);
  stepIndex++;
  if (isRunning && !isPaused) animTimer = setTimeout(runStep, getDelay());
}

function finish() {
  isRunning = false; isPaused = false;
  startBtn.disabled = false; pauseBtn.disabled = true; stepBtn.disabled = true;
  pauseBtn.textContent = '⏸ Pause';
  setStatus('done');
  stepText.innerHTML += ' <br><span style="color:var(--accent-green);font-family:var(--font-mono);font-size:0.8rem;">✓ Visualization complete!</span>';
}

function resetViz() {
  clearTimeout(animTimer);
  isRunning = false; isPaused = false;
  steps = []; stepIndex = 0;
  startBtn.disabled = false; pauseBtn.disabled = true; stepBtn.disabled = true;
  pauseBtn.textContent = '⏸ Pause';
  stepNum.textContent = '0'; totalSteps.textContent = '0';
  stepText.innerHTML = `Choose an algorithm, set your array, and press <strong>Start</strong> to begin.`;
  stepLog.innerHTML = '';
  setStatus('idle');
  const meta = ALGOS[currentAlgo];
  if (meta.category !== 'graph') renderBars(currentArray, {active:-1,compared:-1,sorted:[],found:-1});
  else setTimeout(() => renderGraph({ nodes:[], visited:new Set(), current:null }, graphCanvas, currentAlgo), 50);
  renderCode(meta.code, -1);
}

// ─── EVENT LISTENERS ───
categorySelect.addEventListener('change', () => { updateAlgoOptions(); loadAlgo(); });
algoSelect.addEventListener('change', loadAlgo);

startBtn.addEventListener('click', () => {
  if (!isRunning) {
    steps = generateSteps();
    totalSteps.textContent = steps.length;
    stepIndex = 0; stepLog.innerHTML = '';
  }
  isRunning = true; isPaused = false;
  startBtn.disabled = true; pauseBtn.disabled = false; stepBtn.disabled = false;
  pauseBtn.textContent = '⏸ Pause';
  setStatus('running');
  runStep();
});

pauseBtn.addEventListener('click', () => {
  if (!isPaused) {
    isPaused = true; clearTimeout(animTimer);
    pauseBtn.textContent = '▶ Resume'; setStatus('paused');
  } else {
    isPaused = false;
    pauseBtn.textContent = '⏸ Pause'; setStatus('running');
    runStep();
  }
});

stepBtn.addEventListener('click', () => {
  if (!steps.length) { steps = generateSteps(); totalSteps.textContent = steps.length; stepIndex = 0; }
  isPaused = true; clearTimeout(animTimer);
  pauseBtn.textContent = '▶ Resume'; setStatus('paused');
  if (stepIndex < steps.length) { applyStep(steps[stepIndex]); stepIndex++; }
  else finish();
});

resetBtn.addEventListener('click', resetViz);

speedSlider.addEventListener('input', () => { speedLabel.textContent = speedSlider.value + 'x'; });

document.getElementById('randomBtn').addEventListener('click', () => {
  const n = 10 + Math.floor(Math.random()*6);
  currentArray = Array.from({length:n}, () => 1+Math.floor(Math.random()*99));
  arrayInput.value = currentArray.join(',');
  resetViz();
});

document.getElementById('applyBtn').addEventListener('click', () => {
  const val = arrayInput.value.split(',').map(s=>parseInt(s.trim())).filter(n=>!isNaN(n));
  if (val.length >= 2) { currentArray = val; resetViz(); }
});

// ─── BOOT ───
init();
