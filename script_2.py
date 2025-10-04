
# Create comprehensive JavaScript file
js_content = """/**
 * KUMAON DRIVE - PRODUCTION JAVASCRIPT
 * Version: 1.0
 * All interactive features and booking automation
 */

(function() {
    'use strict';
    
    // ===== CONFIGURATION =====
    const CONFIG = {
        phone: '+919876543210',
        email: 'bookings@kumaondrive.com',
        rates: {
            hatchback: 9,
            sedan: 11,
            suv: 13,
            innova: 18
        },
        fullDayRates: {
            hatchback: 1400,
            sedan: 1500,
            suv: 2000,
            innova: 5500
        }
    };
    
    // ===== DOM ELEMENTS =====
    const elements = {
        bookingForm: document.getElementById('booking-form'),
        calculateBtn: document.getElementById('calculate-fare'),
        fareDisplay: document.getElementById('fare-display'),
        fareAmount: document.getElementById('fare-amount'),
        baseFare: document.getElementById('base-fare'),
        driverAllowanceRow: document.getElementById('driver-allowance-row'),
        tollChargesRow: document.getElementById('toll-charges-row'),
        mobileToggle: document.getElementById('mobile-toggle'),
        navMenu: document.getElementById('nav-menu'),
        scrollToTop: document.getElementById('scroll-to-top'),
        successModal: document.getElementById('success-modal'),
        closeModal: document.getElementById('close-modal'),
        modalCloseBtn: document.getElementById('modal-close-btn')
    };
    
    // ===== POPULAR LOCATIONS =====
    const popularLocations = [
        'Kathgodam Railway Station',
        'Nainital Mall Road',
        'Nainital',
        'Ranikhet',
        'Jim Corbett National Park',
        'Mukteshwar',
        'Bhimtal',
        'Delhi Airport',
        'Delhi',
        'Haldwani',
        'Almora',
        'Kausani',
        'Binsar',
        'Ramgarh'
    ];
    
    // ===== UTILITY FUNCTIONS =====
    function showElement(element) {
        if (element) element.style.display = 'block';
    }
    
    function hideElement(element) {
        if (element) element.style.display = 'none';
    }
    
    function formatCurrency(amount) {
        return '₹' + Math.round(amount).toLocaleString('en-IN');
    }
    
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    function validatePhone(phone) {
        const re = /^[0-9]{10}$/;
        return re.test(phone);
    }
    
    // ===== FARE CALCULATION =====
    function calculateFare() {
        const distance = parseFloat(document.getElementById('distance').value);
        const vehicleType = document.getElementById('vehicle_type').value;
        const bookingType = document.getElementById('booking_type').value;
        
        if (!distance || !vehicleType || !bookingType) {
            alert('⚠️ Please fill in distance, vehicle type, and booking type');
            return null;
        }
        
        if (distance < 1 || distance > 1000) {
            alert('⚠️ Please enter a valid distance between 1 and 1000 km');
            return null;
        }
        
        let baseFare = 0;
        let driverAllowance = 0;
        let tollCharges = 0;
        
        // Calculate base fare
        if (bookingType === 'full_day') {
            baseFare = CONFIG.fullDayRates[vehicleType] || 0;
        } else {
            const ratePerKm = CONFIG.rates[vehicleType] || 0;
            baseFare = distance * ratePerKm;
            
            // Round trip discount
            if (bookingType === 'round_trip') {
                baseFare = (distance * 2 * ratePerKm) * 0.90;
            }
        }
        
        // Add driver allowance for outstation (>100km)
        if (distance > 100) {
            driverAllowance = 500;
        }
        
        // Add toll charges estimate
        if (distance > 50) {
            tollCharges = 200;
        }
        
        const totalFare = Math.round(baseFare + driverAllowance + tollCharges);
        
        return {
            baseFare: Math.round(baseFare),
            driverAllowance,
            tollCharges,
            totalFare
        };
    }
    
    // ===== SMOOTH SCROLLING =====
    function initSmoothScrolling() {
        document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href === '#') return;
                
                e.preventDefault();
                const target = document.querySelector(href);
                
                if (target) {
                    const offset = 80;
                    const targetPosition = target.offsetTop - offset;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    if (elements.navMenu) {
                        elements.navMenu.classList.remove('active');
                    }
                }
            });
        });
    }
    
    // ===== MOBILE MENU =====
    function initMobileMenu() {
        if (elements.mobileToggle && elements.navMenu) {
            elements.mobileToggle.addEventListener('click', function() {
                elements.navMenu.classList.toggle('active');
                this.classList.toggle('active');
            });
        }
    }
    
    // ===== SCROLL TO TOP =====
    function initScrollToTop() {
        if (!elements.scrollToTop) return;
        
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                showElement(elements.scrollToTop);
            } else {
                hideElement(elements.scrollToTop);
            }
        });
        
        elements.scrollToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // ===== STICKY HEADER =====
    function initStickyHeader() {
        const header = document.querySelector('.site-header');
        if (!header) return;
        
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 100) {
                header.style.padding = '8px 0';
            } else {
                header.style.padding = '12px 0';
            }
        });
    }
    
    // ===== FARE CALCULATOR =====
    function initFareCalculator() {
        if (!elements.calculateBtn) return;
        
        elements.calculateBtn.addEventListener('click', function() {
            const calcText = document.getElementById('calc-text');
            const calcLoader = document.getElementById('calc-loader');
            
            // Show loader
            hideElement(calcText);
            showElement(calcLoader);
            
            // Simulate API call delay
            setTimeout(function() {
                const fareData = calculateFare();
                
                if (fareData) {
                    // Update fare display
                    elements.fareAmount.textContent = fareData.totalFare.toLocaleString('en-IN');
                    elements.baseFare.textContent = formatCurrency(fareData.baseFare);
                    
                    // Show/hide additional charges
                    if (fareData.driverAllowance > 0) {
                        showElement(elements.driverAllowanceRow);
                    } else {
                        hideElement(elements.driverAllowanceRow);
                    }
                    
                    if (fareData.tollCharges > 0) {
                        showElement(elements.tollChargesRow);
                    } else {
                        hideElement(elements.tollChargesRow);
                    }
                    
                    // Show fare display with animation
                    elements.fareDisplay.style.display = 'block';
                    setTimeout(() => {
                        elements.fareDisplay.scrollIntoView({ 
                            behavior: 'smooth', 
                            block: 'nearest' 
                        });
                    }, 100);
                    
                    calcText.textContent = '🔄 Recalculate Fare';
                }
                
                // Hide loader
                hideElement(calcLoader);
                showElement(calcText);
            }, 800);
        });
    }
    
    // ===== ROUTE AUTO-FILL =====
    function initRouteAutoFill() {
        document.querySelectorAll('.route-card, .btn-book-route').forEach(function(card) {
            card.addEventListener('click', function(e) {
                e.preventDefault();
                
                const routeCard = this.classList.contains('route-card') ? 
                    this : this.closest('.route-card');
                
                const from = routeCard.getAttribute('data-from');
                const to = routeCard.getAttribute('data-to');
                const distance = routeCard.getAttribute('data-distance');
                
                if (from && to && distance) {
                    document.getElementById('pickup_location').value = from;
                    document.getElementById('dropoff_location').value = to;
                    document.getElementById('distance').value = distance;
                    
                    // Scroll to booking form
                    const bookingSection = document.getElementById('booking');
                    if (bookingSection) {
                        bookingSection.scrollIntoView({ behavior: 'smooth' });
                    }
                    
                    // Flash effect on filled inputs
                    [
                        document.getElementById('pickup_location'),
                        document.getElementById('dropoff_location'),
                        document.getElementById('distance')
                    ].forEach(input => {
                        input.style.transition = 'all 0.3s ease';
                        input.style.backgroundColor = '#90EE90';
                        setTimeout(() => {
                            input.style.backgroundColor = '';
                        }, 1000);
                    });
                }
            });
        });
    }
    
    // ===== VEHICLE SELECTION =====
    function initVehicleSelection() {
        document.querySelectorAll('.btn-select-vehicle').forEach(function(btn) {
            btn.addEventListener('click', function() {
                const vehicle = this.getAttribute('data-vehicle');
                const vehicleSelect = document.getElementById('vehicle_type');
                
                if (vehicle && vehicleSelect) {
                    vehicleSelect.value = vehicle;
                    
                    // Visual feedback
                    this.textContent = '✓ Selected!';
                    this.style.backgroundColor = '#228B22';
                    this.style.color = '#FFFFFF';
                    
                    setTimeout(() => {
                        this.textContent = 'Select This Vehicle';
                        this.style.backgroundColor = '';
                        this.style.color = '';
                    }, 2000);
                    
                    // Scroll to booking
                    const bookingSection = document.getElementById('booking');
                    if (bookingSection) {
                        bookingSection.scrollIntoView({ behavior: 'smooth' });
                    }
                }
            });
        });
    }
    
    // ===== FORM VALIDATION =====
    function validateBookingForm() {
        const pickupLocation = document.getElementById('pickup_location').value.trim();
        const dropoffLocation = document.getElementById('dropoff_location').value.trim();
        const pickupDate = document.getElementById('pickup_date').value;
        const pickupTime = document.getElementById('pickup_time').value;
        const vehicleType = document.getElementById('vehicle_type').value;
        const bookingType = document.getElementById('booking_type').value;
        const distance = document.getElementById('distance').value;
        const customerName = document.getElementById('customer_name').value.trim();
        const customerEmail = document.getElementById('customer_email').value.trim();
        const customerPhone = document.getElementById('customer_phone').value.trim();
        const terms = document.getElementById('terms').checked;
        const fareAmount = elements.fareAmount.textContent.replace(/,/g, '');
        
        // Check all required fields
        if (!pickupLocation || !dropoffLocation) {
            alert('⚠️ Please enter both pickup and drop-off locations');
            return false;
        }
        
        if (!pickupDate || !pickupTime) {
            alert('⚠️ Please select pickup date and time');
            return false;
        }
        
        // Validate date is not in the past
        const selectedDate = new Date(pickupDate + ' ' + pickupTime);
        const now = new Date();
        if (selectedDate < now) {
            alert('⚠️ Pickup date and time cannot be in the past');
            return false;
        }
        
        if (!vehicleType || !bookingType || !distance) {
            alert('⚠️ Please select vehicle type, booking type, and enter distance');
            return false;
        }
        
        if (!fareAmount || fareAmount === '0') {
            alert('⚠️ Please calculate the fare first by clicking \"Calculate Fare\" button');
            return false;
        }
        
        if (!customerName || customerName.length < 3) {
            alert('⚠️ Please enter your full name (minimum 3 characters)');
            return false;
        }
        
        if (!customerEmail || !validateEmail(customerEmail)) {
            alert('⚠️ Please enter a valid email address');
            return false;
        }
        
        if (!customerPhone || !validatePhone(customerPhone)) {
            alert('⚠️ Please enter a valid 10-digit mobile number');
            return false;
        }
        
        if (!terms) {
            alert('⚠️ Please accept the Terms & Conditions to proceed');
            return false;
        }
        
        return true;
    }
    
    // ===== FORM SUBMISSION =====
    function initFormSubmission() {
        if (!elements.bookingForm) return;
        
        elements.bookingForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Validate form
            if (!validateBookingForm()) {
                return;
            }
            
            const submitText = document.getElementById('submit-text');
            const submitLoader = document.getElementById('submit-loader');
            const submitBtn = document.querySelector('.submit-booking');
            
            // Show loader
            hideElement(submitText);
            showElement(submitLoader);
            submitBtn.disabled = true;
            
            // Collect form data
            const formData = {
                pickup_location: document.getElementById('pickup_location').value.trim(),
                dropoff_location: document.getElementById('dropoff_location').value.trim(),
                pickup_date: document.getElementById('pickup_date').value,
                pickup_time: document.getElementById('pickup_time').value,
                vehicle_type: document.getElementById('vehicle_type').value,
                booking_type: document.getElementById('booking_type').value,
                distance: document.getElementById('distance').value,
                fare: elements.fareAmount.textContent.replace(/,/g, ''),
                customer_name: document.getElementById('customer_name').value.trim(),
                customer_email: document.getElementById('customer_email').value.trim(),
                customer_phone: document.getElementById('customer_phone').value.trim(),
                special_requests: document.getElementById('special_requests').value.trim()
            };
            
            // Generate booking ID
            const bookingId = 'KD' + new Date().toISOString().slice(0,10).replace(/-/g, '') + 
                              Math.floor(Math.random() * 9000 + 1000);
            
            // Simulate API call (in production, send to backend)
            setTimeout(function() {
                // Log booking data (in production, send to server)
                console.log('Booking Data:', formData);
                console.log('Booking ID:', bookingId);
                
                // Show success modal
                showSuccessModal(bookingId, formData);
                
                // Reset form
                elements.bookingForm.reset();
                hideElement(elements.fareDisplay);
                
                // Send confirmation (in production, backend handles this)
                sendConfirmationSMS(formData, bookingId);
                sendConfirmationEmail(formData, bookingId);
                
                // Hide loader
                hideElement(submitLoader);
                showElement(submitText);
                submitBtn.disabled = false;
            }, 2000);
        });
    }
    
    // ===== SUCCESS MODAL =====
    function showSuccessModal(bookingId, formData) {
        document.getElementById('modal-booking-id').textContent = bookingId;
        document.getElementById('modal-message').innerHTML = 
            `Your cab booking from <strong>${formData.pickup_location}</strong> to ` +
            `<strong>${formData.dropoff_location}</strong> has been confirmed!`;
        
        showElement(elements.successModal);
    }
    
    function initModal() {
        if (elements.closeModal) {
            elements.closeModal.addEventListener('click', function() {
                hideElement(elements.successModal);
            });
        }
        
        if (elements.modalCloseBtn) {
            elements.modalCloseBtn.addEventListener('click', function() {
                hideElement(elements.successModal);
            });
        }
        
        // Close on outside click
        if (elements.successModal) {
            elements.successModal.addEventListener('click', function(e) {
                if (e.target === elements.successModal) {
                    hideElement(elements.successModal);
                }
            });
        }
    }
    
    // ===== PHONE NUMBER FORMATTING =====
    function initPhoneFormatting() {
        const phoneInput = document.getElementById('customer_phone');
        if (!phoneInput) return;
        
        phoneInput.addEventListener('input', function() {
            let value = this.value.replace(/[^0-9]/g, '');
            if (value.length > 10) {
                value = value.slice(0, 10);
            }
            this.value = value;
        });
    }
    
    // ===== DATE RESTRICTION =====
    function initDateRestriction() {
        const dateInput = document.getElementById('pickup_date');
        if (!dateInput) return;
        
        // Set minimum date to today
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
        
        // Set default date to tomorrow
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        dateInput.value = tomorrow.toISOString().split('T')[0];
    }
    
    // ===== CONFIRMATION FUNCTIONS =====
    function sendConfirmationSMS(formData, bookingId) {
        // In production, this would call your SMS API
        const message = `Kumaon Drive: Booking Confirmed! ID: ${bookingId} | ` +
                       `${formData.pickup_location} to ${formData.dropoff_location} | ` +
                       `Date: ${formData.pickup_date} ${formData.pickup_time} | ` +
                       `Fare: ₹${formData.fare} | Call: ${CONFIG.phone}`;
        
        console.log('SMS to:', formData.customer_phone);
        console.log('Message:', message);
        
        // TODO: Integrate with SMS gateway (MSG91, Twilio, etc.)
    }
    
    function sendConfirmationEmail(formData, bookingId) {
        // In production, this would call your email API
        console.log('Email to:', formData.customer_email);
        console.log('Booking ID:', bookingId);
        console.log('Booking Details:', formData);
        
        // TODO: Integrate with email service (SendGrid, Mailgun, etc.)
    }
    
    // ===== LOCATION SUGGESTIONS =====
    function initLocationSuggestions() {
        const pickupInput = document.getElementById('pickup_location');
        const dropoffInput = document.getElementById('dropoff_location');
        
        [pickupInput, dropoffInput].forEach(input => {
            if (!input) return;
            
            input.addEventListener('input', function() {
                const value = this.value.toLowerCase();
                if (value.length < 2) return;
                
                const matches = popularLocations.filter(loc => 
                    loc.toLowerCase().includes(value)
                );
                
                // Show suggestions (basic implementation)
                // In production, integrate with Google Places API
                console.log('Location matches:', matches);
            });
        });
    }
    
    // ===== WHATSAPP INTEGRATION =====
    function initWhatsAppIntegration() {
        const whatsappBtn = document.querySelector('.whatsapp-float');
        if (!whatsappBtn) return;
        
        whatsappBtn.addEventListener('click', function(e) {
            // Log click for analytics
            console.log('WhatsApp button clicked');
        });
    }
    
    // ===== ANALYTICS =====
    function trackEvent(eventName, eventData) {
        // Integrate with Google Analytics or other analytics service
        console.log('Event:', eventName, eventData);
        
        // Example: Google Analytics 4
        // if (typeof gtag !== 'undefined') {
        //     gtag('event', eventName, eventData);
        // }
    }
    
    // ===== INITIALIZATION =====
    function init() {
        console.log('🚗 Kumaon Drive Website Initialized');
        
        // Initialize all features
        initSmoothScrolling();
        initMobileMenu();
        initScrollToTop();
        initStickyHeader();
        initFareCalculator();
        initRouteAutoFill();
        initVehicleSelection();
        initFormSubmission();
        initModal();
        initPhoneFormatting();
        initDateRestriction();
        initLocationSuggestions();
        initWhatsAppIntegration();
        
        // Track page view
        trackEvent('page_view', {
            page_title: document.title,
            page_location: window.location.href
        });
        
        console.log('✅ All features loaded successfully');
    }
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
})();

// ===== SERVICE WORKER (Optional - for PWA) =====
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // navigator.serviceWorker.register('/sw.js')
        //     .then(reg => console.log('Service Worker registered'))
        //     .catch(err => console.log('Service Worker registration failed'));
    });
}
"""

with open(f"{html_base}/js/script.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("✓ Created complete script.js with all interactive features")
print(f"  - Booking automation logic")
print(f"  - Fare calculation engine")
print(f"  - Form validation")
print(f"  - Auto-fill from routes")
print(f"  - Mobile menu handling")
print(f"  - Smooth scrolling")
print(f"  - Success modal system")
print(f"  - SMS/Email confirmation hooks")
