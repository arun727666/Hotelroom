// Main JS file for SRD Hotel

document.addEventListener('DOMContentLoaded', function () {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow-sm');
            navbar.style.backgroundColor = 'rgba(26, 26, 26, 1)';
        } else {
            navbar.classList.remove('shadow-sm');
            navbar.style.backgroundColor = 'rgba(26, 26, 26, 0.95)';
        }
    });

    // Initialize tooltips/popovers if needed (Bootstrap)
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
});
