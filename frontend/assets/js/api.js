// ─── API MODULE ───
const API_BASE = 'http://localhost:5000/api';

const Api = {
  async health() {
    try {
      const res = await fetch(`${API_BASE}/health`, { signal: AbortSignal.timeout(3000) });
      return res.ok;
    } catch { return false; }
  },

  async getSteps(algorithm, array, target = null) {
    const body = { array };
    if (target !== null) body.target = target;
    const res = await fetch(`${API_BASE}/algorithms/${algorithm}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return res.json();
  },

  async getAlgorithms() {
    const res = await fetch(`${API_BASE}/algorithms`);
    return res.json();
  }
};

// Check backend connection on load
(async () => {
  const apiStatusEl = document.getElementById('apiStatus');
  const apiStatusText = document.getElementById('apiStatusText');
  const online = await Api.health();
  if (online) {
    apiStatusText.textContent = 'Backend connected — live API mode active';
  } else {
    apiStatusEl.classList.add('offline');
    apiStatusText.textContent = 'Backend offline — running in browser simulation mode';
  }
  window._backendOnline = online;
})();
