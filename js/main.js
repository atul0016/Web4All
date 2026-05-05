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

    // --- Prefill contact form from service page links ---
    const params = new URLSearchParams(window.location.search);
    const hashParams = new URLSearchParams((window.location.hash.split('?')[1] || ''));
    const serviceParam = params.get('service') || hashParams.get('service');
    const planParam = params.get('plan') || hashParams.get('plan');

    if (serviceParam === 'advertising') {
        const business = document.getElementById('business');
        const plan = document.getElementById('plan');
        const message = document.getElementById('message');

        if (business) business.value = 'Advertising & Digital Marketing';
        if (plan && planParam) {
            const matchedOption = Array.from(plan.options).find(option => option.textContent.toLowerCase().includes(planParam.toLowerCase()));
            if (matchedOption) plan.value = matchedOption.value;
        }
        if (message && !message.value) {
            message.value = 'I am interested in SA-Flow advertising services. Please share the best plan and next steps.';
        }
    }
});

// --- Contact Form Handler ---
async function handleSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.textContent;

    // Show loading state
    btn.textContent = 'Sending...';
    btn.disabled = true;

    try {
        const formData = new FormData(form);
        const response = await fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();

        if (data.success) {
            btn.textContent = '✓ Enquiry Sent!';
            btn.style.background = '#22c55e';
            form.reset();
            setTimeout(() => {
                btn.textContent = originalText;
                btn.style.background = '';
                btn.disabled = false;
            }, 4000);
        } else {
            throw new Error(data.message || 'Submission failed');
        }
    } catch (err) {
        btn.textContent = '✗ Failed — Try Again';
        btn.style.background = '#ef4444';
        setTimeout(() => {
            btn.textContent = originalText;
            btn.style.background = '';
            btn.disabled = false;
        }, 3000);
    }
}
