// ─── SCROLL REVEAL ───
const revealElements = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver(
  (entries) => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
  { threshold: 0.12 }
);
revealElements.forEach(el => observer.observe(el));

// ─── DEMO BAR ANIMATION ───
const demoSteps = [
  { active: [1,2], sorted: [], info: '▶ Step 1 — Comparing elements 8 and 6 → Swap!' },
  { active: [2,3], sorted: [], info: '▶ Step 2 — Comparing elements 6 and 2 → Swap!' },
  { active: [3,4], sorted: [4], info: '▶ Step 3 — Element 9 is already in place ✓' },
  { active: [0,1], sorted: [4,5,6], info: '▶ Step 4 — Comparing elements 3 and 8 → No swap' },
  { active: [], sorted: [0,1,2,3,4,5,6], info: '✓ Complete — Array is fully sorted!' },
];

let stepIdx = 0;
const bars = document.querySelectorAll('#demoBars .mini-bar');
const stepInfo = document.getElementById('demoStepInfo');

function runDemoStep() {
  const step = demoSteps[stepIdx % demoSteps.length];
  bars.forEach((bar, i) => {
    bar.className = 'mini-bar';
    if (step.sorted.includes(i)) bar.classList.add('sorted');
    else if (step.active.includes(i)) bar.classList.add(step.active.indexOf(i) === 0 ? 'active' : 'compared');
    else bar.classList.add('default');
  });
  if (stepInfo) stepInfo.textContent = step.info;
  stepIdx++;
}

setInterval(runDemoStep, 1800);
