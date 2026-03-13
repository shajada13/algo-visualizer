// ─── NAVBAR ACTIVE LINK ───
(function() {
  const path = window.location.pathname;
  const links = document.querySelectorAll('.nav-links a[data-page]');
  links.forEach(link => {
    const page = link.getAttribute('data-page');
    if (page === 'cta') return;
    const href = link.getAttribute('href') || '';
    if (
      (page === 'home' && (path.endsWith('index.html') || path.endsWith('/'))) ||
      (page === 'visualizer' && path.includes('visualizer')) ||
      (page === 'about' && path.includes('about'))
    ) {
      link.classList.add('active');
    }
  });
})();
