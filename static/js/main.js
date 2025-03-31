document.addEventListener('DOMContentLoaded', function() {
    // Tooltip initialization
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Add active class to current nav item
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (href !== '/' && currentPath.startsWith(href))) {
            link.classList.add('active');
        }
    });

    // Confirmation dialogs
    document.querySelectorAll('.confirm-action').forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm(this.getAttribute('data-confirm-message') || 'คุณแน่ใจหรือไม่?')) {
                e.preventDefault();
            }
        });
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Add thumbnail preview for file inputs
    document.querySelectorAll('.custom-file-input').forEach(input => {
        input.addEventListener('change', function() {
            const preview = document.querySelector(this.getAttribute('data-preview'));
            if (preview && this.files && this.files[0]) {
                const reader = new FileReader();

                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                }

                reader.readAsDataURL(this.files[0]);
            }
        });
    });

    // Enable search highlight in tables
    function highlightText(text, search) {
        if (!search) return text;
        const pattern = new RegExp(`(${search})`, 'gi');
        return text.replace(pattern, '<mark>$1</mark>');
    }

    document.querySelectorAll('.searchable-table').forEach(table => {
        const searchInput = document.querySelector(`[data-search-table="${table.id}"]`);

        if (searchInput) {
            searchInput.addEventListener('input', function() {
                const searchTerm = this.value.trim().toLowerCase();
                const rows = table.querySelectorAll('tbody tr');

                rows.forEach(row => {
                    const cells = row.querySelectorAll('td');
                    let found = false;

                    cells.forEach(cell => {
                        const text = cell.textContent.toLowerCase();

                        if (text.includes(searchTerm)) {
                            found = true;
                            cell.innerHTML = highlightText(cell.textContent, searchTerm);
                        } else {
                            cell.innerHTML = cell.textContent;
                        }
                    });

                    row.style.display = found ? '' : 'none';
                });
            });
        }
    });

    // Date picker enhancement
    const datePickers = document.querySelectorAll('.date-picker');
    if (datePickers.length > 0 && typeof flatpickr !== 'undefined') {
        flatpickr(datePickers, {
            dateFormat: 'd/m/Y',
            locale: 'th'
        });
    }
});
