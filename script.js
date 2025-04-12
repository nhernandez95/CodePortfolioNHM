// Theme toggle and persistence
const themeToggleBtn = document.getElementById('theme-toggle');
const savedTheme = localStorage.getItem('theme');

// Apply saved theme on load
if (savedTheme === 'dark') {
  document.body.setAttribute('data-theme', 'dark');
  // Set toggle icon to sun (to indicate switch to light mode)
  themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
} else {
  // Default to light theme
  document.body.setAttribute('data-theme', 'light');
  themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
}

// Toggle theme on button click
themeToggleBtn.addEventListener('click', () => {
  const currentTheme = document.body.getAttribute('data-theme');
  if (currentTheme === 'light') {
    // Switch to dark mode
    document.body.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
  } else {
    // Switch to light mode
    document.body.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
  }
});
