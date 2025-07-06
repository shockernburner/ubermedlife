// Main JavaScript for UberMed.Life

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert && alert.parentNode) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 5000);
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Loading button states
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(button => {
        button.addEventListener('click', function() {
            const form = this.closest('form');
            if (form && form.checkValidity()) {
                this.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span>Loading...';
                this.disabled = true;
            }
        });
    });

    // Search functionality
    const searchForms = document.querySelectorAll('.search-form');
    searchForms.forEach(form => {
        const input = form.querySelector('input[type="search"], input[name="search"]');
        if (input) {
            input.addEventListener('input', debounce(function() {
                // Add search suggestions or live search functionality here
                console.log('Search query:', this.value);
            }, 300));
        }
    });

    // Language switcher
    const languageLinks = document.querySelectorAll('[data-language]');
    languageLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const language = this.dataset.language;
            const currentPath = window.location.pathname;
            
            // Remove current language prefix
            let newPath = currentPath.replace(/^\/(en|bn)/, '');
            
            // Add new language prefix
            if (language !== 'en') {
                newPath = '/' + language + newPath;
            }
            
            window.location.href = newPath;
        });
    });

    // Image lazy loading fallback
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // Back to top button
    const backToTopButton = createBackToTopButton();
    document.body.appendChild(backToTopButton);

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    // Consultation form enhancements
    const consultationForms = document.querySelectorAll('.consultation-form');
    consultationForms.forEach(form => {
        const doctorSelect = form.querySelector('select[name="doctor"]');
        const feeDisplay = form.querySelector('.consultation-fee');
        
        if (doctorSelect && feeDisplay) {
            doctorSelect.addEventListener('change', function() {
                const selectedOption = this.options[this.selectedIndex];
                const fee = selectedOption.dataset.fee;
                if (fee) {
                    feeDisplay.textContent = `Consultation Fee: $${fee} USD`;
                    feeDisplay.style.display = 'block';
                } else {
                    feeDisplay.style.display = 'none';
                }
            });
        }
    });

    // File upload preview
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const preview = document.createElement('div');
                preview.className = 'file-preview mt-2 p-2 bg-light rounded';
                preview.innerHTML = `
                    <i class="fas fa-file me-2"></i>
                    <span class="file-name">${file.name}</span>
                    <span class="file-size text-muted ms-2">(${formatFileSize(file.size)})</span>
                `;
                
                // Remove existing preview
                const existingPreview = this.parentNode.querySelector('.file-preview');
                if (existingPreview) {
                    existingPreview.remove();
                }
                
                this.parentNode.appendChild(preview);
            }
        });
    });
});

// Utility functions
function debounce(func, wait, immediate) {
    let timeout;
    return function executedFunction() {
        const context = this;
        const args = arguments;
        const later = function() {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function createBackToTopButton() {
    const button = document.createElement('button');
    button.innerHTML = '<i class="fas fa-arrow-up"></i>';
    button.className = 'btn btn-primary back-to-top';
    button.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: none;
        z-index: 999;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    `;
    
    button.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    return button;
}

// AJAX helper for form submissions
function submitFormAjax(form, successCallback, errorCallback) {
    const formData = new FormData(form);
    const url = form.action || window.location.href;
    
    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (successCallback) successCallback(data);
        } else {
            if (errorCallback) errorCallback(data);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        if (errorCallback) errorCallback({error: 'Network error occurred'});
    });
}

// Notification system
function showNotification(message, type = 'info', duration = 5000) {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
    `;
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after duration
    setTimeout(() => {
        if (notification.parentNode) {
            const bsAlert = new bootstrap.Alert(notification);
            bsAlert.close();
        }
    }, duration);
}

// Language detection and switching
function detectUserLanguage() {
    const browserLang = navigator.language || navigator.userLanguage;
    const supportedLangs = ['en', 'bn'];
    
    for (let lang of supportedLangs) {
        if (browserLang.startsWith(lang)) {
            return lang;
        }
    }
    
    return 'en'; // Default fallback
}

// Cookie helpers
function setCookie(name, value, days) {
    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
}

function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Export functions for global use
window.UberMed = {
    showNotification,
    submitFormAjax,
    detectUserLanguage,
    setCookie,
    getCookie,
    formatFileSize
};
