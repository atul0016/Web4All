/* ============================================
   SA-Flow — Main JavaScript
   Handles animations, navigation, interactions
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

    // --- Scroll Animations (Intersection Observer) ---
    const animatedElements = document.querySelectorAll('[data-animate]');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Stagger animations for sibling elements
                const siblings = entry.target.parentElement.querySelectorAll('[data-animate]');
                let delay = 0;
                siblings.forEach((sib, i) => {
                    if (sib === entry.target) delay = i * 80;
                });
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, delay);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    });

    animatedElements.forEach(el => observer.observe(el));

    // --- Navbar Scroll Effect ---
    const nav = document.getElementById('nav');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;
        if (currentScroll > 60) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
        lastScroll = currentScroll;
    }, { passive: true });

    // --- Mobile Menu Toggle ---
    const mobileToggle = document.getElementById('mobileToggle');
    const navLinks = document.getElementById('navLinks');

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
            mobileToggle.classList.toggle('active');
            document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
        });

        // Close mobile menu on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('open');
                mobileToggle.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // --- Category Card Expand/Collapse ---
    document.querySelectorAll('.category-card').forEach(card => {
        const toggle = card.querySelector('.category-toggle');
        const info = card.querySelector('.category-info');

        const handleToggle = (e) => {
            // Don't toggle if clicking a shop link
            if (e.target.closest('.shop-link')) return;
            
            // Close other cards
            document.querySelectorAll('.category-card.expanded').forEach(other => {
                if (other !== card) other.classList.remove('expanded');
            });

            card.classList.toggle('expanded');
        };

        card.addEventListener('click', handleToggle);
    });

    // --- Smooth Scroll for Anchor Links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const navHeight = nav.offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.scrollY - navHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// --- Contact Form Handler ---
function handleSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const name = form.querySelector('#name').value;
    const phone = form.querySelector('#phone').value;
    const business = form.querySelector('#business').value;
    const plan = form.querySelector('#plan').value;
    const message = form.querySelector('#message').value;

    // Construct email
    const mailSubject = encodeURIComponent(`Website Enquiry — ${business}`);
    const mailBody = encodeURIComponent(
        `Name: ${name}\n${phone ? 'Phone: ' + phone + '\n' : ''}Business: ${business}\nPlan: ${plan}\n${message ? 'Message: ' + message : ''}`
    );

    // Show success state
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.textContent;
    btn.textContent = '✓ Enquiry Sent!';
    btn.style.background = '#22c55e';

    // Open email client
    window.location.href = `mailto:saflowtech@gmail.com?subject=${mailSubject}&body=${mailBody}`;

    setTimeout(() => {
        btn.textContent = originalText;
        btn.style.background = '';
        form.reset();
    }, 3000);
}
