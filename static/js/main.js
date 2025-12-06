/**
 * Main JavaScript file for Django Tour & Travel site
 */

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide alert messages after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Image lazy loading for gallery
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img.lazy').forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Price calculator for booking form (if number_of_people changes)
    const peopleInput = document.querySelector('input[name="number_of_people"]');
    if (peopleInput) {
        peopleInput.addEventListener('change', function() {
            const pricePerPerson = parseFloat(this.dataset.price || 0);
            const numPeople = parseInt(this.value) || 1;
            const totalPrice = pricePerPerson * numPeople;
            
            const priceDisplay = document.querySelector('#total-price-display');
            if (priceDisplay) {
                priceDisplay.textContent = totalPrice.toFixed(2);
            }
        });
    }

    console.log('Django Tour & Travel site initialized successfully!');
});
