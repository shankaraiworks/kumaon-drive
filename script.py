
# Now create a complete standalone HTML version (non-WordPress) for immediate deployment
import os

# Create new directory structure for HTML version
html_base = "kumaon-drive-html"
os.makedirs(html_base, exist_ok=True)

html_dirs = [
    f"{html_base}/css",
    f"{html_base}/js",
    f"{html_base}/images",
    f"{html_base}/assets"
]

for directory in html_dirs:
    os.makedirs(directory, exist_ok=True)

print("✓ Created HTML website directory structure")

# Create the main HTML file with complete website
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Kumaon Drive - Premium taxi and cab service in Kumaon region, Uttarakhand. Book cabs to Nainital, Ranikhet, Jim Corbett and more. Instant booking with SMS confirmation.">
    <meta name="keywords" content="Kumaon taxi, Nainital cab, Uttarakhand taxi service, hill station cab booking, Ranikhet taxi, Jim Corbett cab">
    <meta name="author" content="Kumaon Drive">
    <meta name="robots" content="index, follow">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="Kumaon Drive - Premium Taxi Service in Uttarakhand">
    <meta property="og:description" content="Book comfortable and safe taxi rides across beautiful Kumaon region. 24/7 service available.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://kumaondrive.com">
    
    <title>Kumaon Drive - Premium Taxi & Cab Service in Kumaon, Uttarakhand | Book Now</title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="images/favicon.png">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="css/style.css">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>

    <!-- Header -->
    <header class="site-header" id="header">
        <div class="container">
            <div class="header-container">
                <div class="site-logo">
                    <a href="#home">
                        <img src="images/kumaon-drive-logo.png" alt="Kumaon Drive Logo" width="200" height="70">
                    </a>
                </div>
                
                <nav class="main-navigation" id="main-nav">
                    <button class="mobile-menu-toggle" id="mobile-toggle" aria-label="Toggle Menu">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                    <ul id="nav-menu">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#booking">Book Now</a></li>
                        <li><a href="#fleet">Our Fleet</a></li>
                        <li><a href="#routes">Popular Routes</a></li>
                        <li><a href="#testimonials">Reviews</a></li>
                        <li><a href="#contact">Contact</a></li>
                        <li><a href="tel:+919876543210" class="cta-button">📞 Call Now</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero-section">
        <div class="hero-overlay"></div>
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title animate-fade-in">Explore Kumaon with Comfort & Safety</h1>
                <p class="hero-subtitle animate-fade-in-delay">Premium Taxi Service | Nainital • Ranikhet • Jim Corbett • Mukteshwar • Bhimtal</p>
                <div class="hero-buttons animate-fade-in-delay-2">
                    <a href="#booking" class="btn-primary">Book Your Ride Now</a>
                    <a href="tel:+919876543210" class="btn-secondary">Call: +91-98765-43210</a>
                </div>
                <div class="hero-features">
                    <div class="feature-item">
                        <span class="feature-icon">✓</span>
                        <span>24/7 Available</span>
                    </div>
                    <div class="feature-item">
                        <span class="feature-icon">✓</span>
                        <span>Instant Confirmation</span>
                    </div>
                    <div class="feature-item">
                        <span class="feature-icon">✓</span>
                        <span>Professional Drivers</span>
                    </div>
                    <div class="feature-item">
                        <span class="feature-icon">✓</span>
                        <span>Clean Vehicles</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Booking Section -->
    <section id="booking" class="booking-section">
        <div class="container">
            <div class="booking-form-container">
                <h2 class="section-heading">Book Your Cab - Instant Confirmation</h2>
                <p class="section-subheading">Fill in the details below and get instant fare calculation & SMS confirmation</p>
                
                <form id="booking-form" class="booking-form">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="pickup_location">Pickup Location *</label>
                            <input type="text" id="pickup_location" name="pickup_location" required placeholder="e.g., Kathgodam Railway Station" autocomplete="off">
                            <div class="suggestions" id="pickup-suggestions"></div>
                        </div>
                        <div class="form-group">
                            <label for="dropoff_location">Drop-off Location *</label>
                            <input type="text" id="dropoff_location" name="dropoff_location" required placeholder="e.g., Nainital Mall Road" autocomplete="off">
                            <div class="suggestions" id="dropoff-suggestions"></div>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="pickup_date">Pickup Date *</label>
                            <input type="date" id="pickup_date" name="pickup_date" required>
                        </div>
                        <div class="form-group">
                            <label for="pickup_time">Pickup Time *</label>
                            <input type="time" id="pickup_time" name="pickup_time" required value="09:00">
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="vehicle_type">Vehicle Type *</label>
                            <select id="vehicle_type" name="vehicle_type" required>
                                <option value="">Select Vehicle</option>
                                <option value="hatchback">🚗 Hatchback (Swift, Wagon R) - ₹9/km</option>
                                <option value="sedan">🚙 Sedan (Etios, Dzire) - ₹11/km</option>
                                <option value="suv">🚐 SUV (Ertiga, XUV) - ₹13/km</option>
                                <option value="innova">🚌 Premium SUV (Innova Crysta) - ₹18/km</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="booking_type">Booking Type *</label>
                            <select id="booking_type" name="booking_type" required>
                                <option value="one_way">One Way</option>
                                <option value="round_trip">Round Trip (10% Discount)</option>
                                <option value="full_day">Full Day (8 hrs/80 km)</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="distance">Estimated Distance (km) *</label>
                            <input type="number" id="distance" name="distance" required placeholder="Enter distance" min="1" max="1000" step="1">
                            <small class="help-text">Approximate distance between pickup and drop-off</small>
                        </div>
                        <div class="form-group">
                            <label>&nbsp;</label>
                            <button type="button" class="btn-calculate" id="calculate-fare">
                                <span id="calc-text">🧮 Calculate Fare</span>
                                <span id="calc-loader" class="loader" style="display: none;"></span>
                            </button>
                        </div>
                    </div>
                    
                    <div id="fare-display" class="fare-display" style="display: none;">
                        <div class="fare-content">
                            <h3>Estimated Total Fare</h3>
                            <div class="fare-amount">₹<span id="fare-amount">0</span></div>
                            <div class="fare-breakdown">
                                <div class="breakdown-item">
                                    <span>Base Fare:</span>
                                    <span id="base-fare">₹0</span>
                                </div>
                                <div class="breakdown-item" id="driver-allowance-row" style="display: none;">
                                    <span>Driver Allowance (Outstation):</span>
                                    <span>₹500</span>
                                </div>
                                <div class="breakdown-item" id="toll-charges-row" style="display: none;">
                                    <span>Estimated Toll Charges:</span>
                                    <span>₹200</span>
                                </div>
                            </div>
                            <p class="fare-note">*Final fare may vary based on actual route and waiting time</p>
                        </div>
                    </div>
                    
                    <div class="form-divider"></div>
                    <h3 class="form-section-title">Customer Details</h3>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="customer_name">Your Full Name *</label>
                            <input type="text" id="customer_name" name="customer_name" required placeholder="Enter your full name">
                        </div>
                        <div class="form-group">
                            <label for="customer_email">Email Address *</label>
                            <input type="email" id="customer_email" name="customer_email" required placeholder="your@email.com">
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="customer_phone">Phone Number (WhatsApp) *</label>
                            <input type="tel" id="customer_phone" name="customer_phone" required placeholder="10-digit mobile number" pattern="[0-9]{10}" maxlength="10">
                            <small class="help-text">You'll receive booking confirmation on this number</small>
                        </div>
                        <div class="form-group">
                            <label for="special_requests">Special Requests (Optional)</label>
                            <textarea id="special_requests" name="special_requests" rows="1" placeholder="Child seat, extra luggage space, etc."></textarea>
                        </div>
                    </div>
                    
                    <div class="form-terms">
                        <label class="checkbox-label">
                            <input type="checkbox" id="terms" name="terms" required>
                            <span>I agree to the <a href="#" target="_blank">Terms & Conditions</a> and <a href="#" target="_blank">Privacy Policy</a></span>
                        </label>
                    </div>
                    
                    <button type="submit" class="submit-booking">
                        <span id="submit-text">✓ Confirm Booking & Get Instant SMS</span>
                        <span id="submit-loader" class="loader" style="display: none;"></span>
                    </button>
                    
                    <div class="payment-info">
                        <p>💳 Payment Options: UPI, Cards, Net Banking, Cash</p>
                        <p>📱 Instant booking confirmation via SMS & Email</p>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <!-- Fleet Section -->
    <section id="fleet" class="fleet-section">
        <div class="container">
            <h2 class="section-title">Our Premium Fleet</h2>
            <p class="section-subtitle">Choose from our well-maintained vehicles for your comfortable journey</p>
            
            <div class="fleet-grid">
                <div class="vehicle-card">
                    <div class="vehicle-image">
                        <div class="vehicle-icon">🚗</div>
                    </div>
                    <div class="vehicle-info">
                        <h3>Hatchback</h3>
                        <p class="vehicle-models">Swift, Wagon R, Baleno</p>
                        <ul class="vehicle-features">
                            <li><span class="check-icon">✓</span> 4 Passengers</li>
                            <li><span class="check-icon">✓</span> 2 Large Bags</li>
                            <li><span class="check-icon">✓</span> AC Available</li>
                            <li><span class="check-icon">✓</span> Perfect for City Rides</li>
                            <li><span class="check-icon">✓</span> Fuel Efficient</li>
                        </ul>
                        <div class="vehicle-pricing">
                            <div class="price-item">
                                <div class="vehicle-price">₹9<small>/km</small></div>
                                <small class="price-label">Per Kilometer</small>
                            </div>
                            <div class="price-divider">or</div>
                            <div class="price-item">
                                <div class="vehicle-price">₹1,400<small>/day</small></div>
                                <small class="price-label">Full Day (8hrs/80km)</small>
                            </div>
                        </div>
                        <button class="btn-select-vehicle" data-vehicle="hatchback">Select This Vehicle</button>
                    </div>
                </div>
                
                <div class="vehicle-card featured">
                    <div class="featured-badge">Popular</div>
                    <div class="vehicle-image">
                        <div class="vehicle-icon">🚙</div>
                    </div>
                    <div class="vehicle-info">
                        <h3>Sedan</h3>
                        <p class="vehicle-models">Etios, Dzire, Honda City</p>
                        <ul class="vehicle-features">
                            <li><span class="check-icon">✓</span> 4 Passengers</li>
                            <li><span class="check-icon">✓</span> 3 Large Bags</li>
                            <li><span class="check-icon">✓</span> Premium Comfort</li>
                            <li><span class="check-icon">✓</span> Ideal for Long Trips</li>
                            <li><span class="check-icon">✓</span> Spacious Interiors</li>
                        </ul>
                        <div class="vehicle-pricing">
                            <div class="price-item">
                                <div class="vehicle-price">₹11<small>/km</small></div>
                                <small class="price-label">Per Kilometer</small>
                            </div>
                            <div class="price-divider">or</div>
                            <div class="price-item">
                                <div class="vehicle-price">₹1,500<small>/day</small></div>
                                <small class="price-label">Full Day (8hrs/80km)</small>
                            </div>
                        </div>
                        <button class="btn-select-vehicle" data-vehicle="sedan">Select This Vehicle</button>
                    </div>
                </div>
                
                <div class="vehicle-card">
                    <div class="vehicle-image">
                        <div class="vehicle-icon">🚐</div>
                    </div>
                    <div class="vehicle-info">
                        <h3>SUV</h3>
                        <p class="vehicle-models">Ertiga, XUV300, Scorpio</p>
                        <ul class="vehicle-features">
                            <li><span class="check-icon">✓</span> 6-7 Passengers</li>
                            <li><span class="check-icon">✓</span> 4 Large Bags</li>
                            <li><span class="check-icon">✓</span> Mountain Terrain Ready</li>
                            <li><span class="check-icon">✓</span> Perfect for Families</li>
                            <li><span class="check-icon">✓</span> Extra Luggage Space</li>
                        </ul>
                        <div class="vehicle-pricing">
                            <div class="price-item">
                                <div class="vehicle-price">₹13<small>/km</small></div>
                                <small class="price-label">Per Kilometer</small>
                            </div>
                            <div class="price-divider">or</div>
                            <div class="price-item">
                                <div class="vehicle-price">₹2,000<small>/day</small></div>
                                <small class="price-label">Full Day (8hrs/80km)</small>
                            </div>
                        </div>
                        <button class="btn-select-vehicle" data-vehicle="suv">Select This Vehicle</button>
                    </div>
                </div>
                
                <div class="vehicle-card">
                    <div class="vehicle-image">
                        <div class="vehicle-icon">🚌</div>
                    </div>
                    <div class="vehicle-info">
                        <h3>Premium SUV</h3>
                        <p class="vehicle-models">Toyota Innova Crysta</p>
                        <ul class="vehicle-features">
                            <li><span class="check-icon">✓</span> 6-7 Passengers</li>
                            <li><span class="check-icon">✓</span> 5 Large Bags</li>
                            <li><span class="check-icon">✓</span> Luxury Interiors</li>
                            <li><span class="check-icon">✓</span> Best for Group Tours</li>
                            <li><span class="check-icon">✓</span> Superior Comfort</li>
                        </ul>
                        <div class="vehicle-pricing">
                            <div class="price-item">
                                <div class="vehicle-price">₹18<small>/km</small></div>
                                <small class="price-label">Per Kilometer</small>
                            </div>
                            <div class="price-divider">or</div>
                            <div class="price-item">
                                <div class="vehicle-price">₹5,500<small>/day</small></div>
                                <small class="price-label">Full Day (8hrs/80km)</small>
                            </div>
                        </div>
                        <button class="btn-select-vehicle" data-vehicle="innova">Select This Vehicle</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Routes Section -->
    <section id="routes" class="routes-section">
        <div class="container">
            <h2 class="section-title">Popular Routes in Kumaon</h2>
            <p class="section-subtitle">Click any route to auto-fill booking form</p>
            
            <div class="routes-grid">
                <div class="route-card" data-from="Kathgodam Railway Station" data-to="Nainital Mall Road" data-distance="35">
                    <div class="route-number">01</div>
                    <h3>Kathgodam → Nainital</h3>
                    <p class="route-description">Scenic route to the beautiful lake city nestled in the Himalayas</p>
                    <div class="route-details">
                        <div class="route-info">
                            <span class="info-icon">📍</span>
                            <span>35 km • 1.5 hours</span>
                        </div>
                        <div class="route-fare">
                            <span class="fare-label">From</span>
                            <span class="fare-value">₹385</span>
                        </div>
                    </div>
                    <button class="btn-book-route">Book This Route</button>
                </div>
                
                <div class="route-card" data-from="Delhi" data-to="Nainital" data-distance="320">
                    <div class="route-number">02</div>
                    <h3>Delhi → Nainital</h3>
                    <p class="route-description">Comfortable journey from capital to hills with rest stops</p>
                    <div class="route-details">
                        <div class="route-info">
                            <span class="info-icon">📍</span>
                            <span>320 km • 7 hours</span>
                        </div>
                        <div class="route-fare">
                            <span class="fare-label">From</span>
                            <span class="fare-value">₹4,220</span>
                        </div>
                    </div>
                    <button class="btn-book-route">Book This Route</button>
                </div>
                
                <div class="route-card" data-from="Nainital" data-to="Ranikhet" data-distance="60">
                    <div class="route-number">03</div>
                    <h3>Nainital → Ranikhet</h3>
                    <p class="route-description">Beautiful mountain drive through dense pine forests</p>
                    <div class="route-details">
                        <div class="route-info">
                            <span class="info-icon">📍</span>
                            <span>60 km • 2 hours</span>
                        </div>
                        <div class="route-fare">
                            <span class="fare-label">From</span>
                            <span class="fare-value">₹660</span>
                        </div>
                    </div>
                    <button class="btn-book-route">Book This Route</button>
                </div>
                
                <div class="route-card" data-from="Nainital" data-to="Jim Corbett National Park" data-distance="65">
                    <div class="route-number">04</div>
                    <h3>Nainital → Jim Corbett</h3>
                    <p class="route-description">Wildlife adventure awaits in India's oldest national park</p>
                    <div class="route-details">
                        <div class="route-info">
                            <span class="info-icon">📍</span>
                            <span>65 km • 2.5 hours</span>
                        </div>
                        <div class="route-fare">
                            <span class="fare-label">From</span>
                            <span class="fare-value">₹915</span>
                        </div>
                    </div>
                    <button class="btn-book-route">Book This Route</button>
                </div>
                
                <div class="route-card" data-from="Kathgodam" data-to="Mukteshwar" data-distance="50">
                    <div class="route-number">05</div>
                    <h3>Kathgodam → Mukteshwar</h3>
                    <p class="route-description">Peaceful hilltop destination with breathtaking Himalayan views</p>
                    <div class="route-details">
                        <div class="route-info">
                            <span class="info-icon">📍</span>
                            <span>50 km • 2 hours</span>
                        </div>
                        <div class="route-fare">
                            <span class="fare-label">From</span>
                            <span class="fare-value">₹550</span>
                        </div>
                    </div>
                    <button class="btn-book-route">Book This Route</button>
                </div>
                
                <div class="route-card" data-from="Nainital" data-to="Bhimtal" data-distance="22">
                    <div class="route-number">06</div>
                    <h3>Nainital → Bhimtal</h3>
                    <p class="route-description">Tranquil lake town perfect for peaceful getaways</p>
                    <div class="route-details">
                        <div class="route-info">
                            <span class="info-icon">📍</span>
                            <span>22 km • 1 hour</span>
                        </div>
                        <div class="route-fare">
                            <span class="fare-label">From</span>
                            <span class="fare-value">₹242</span>
                        </div>
                    </div>
                    <button class="btn-book-route">Book This Route</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us Section -->
    <section class="why-choose-section">
        <div class="container">
            <h2 class="section-title">Why Choose Kumaon Drive?</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon-large">🎯</div>
                    <h3>Instant Booking</h3>
                    <p>Quick online booking with instant SMS & email confirmation. No waiting, no hassle!</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon-large">💰</div>
                    <h3>Transparent Pricing</h3>
                    <p>No hidden charges. What you see is what you pay. Clear fare breakdown provided upfront.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon-large">👨‍✈️</div>
                    <h3>Professional Drivers</h3>
                    <p>Experienced, verified, and courteous drivers who know Kumaon routes like the back of their hand.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon-large">🚗</div>
                    <h3>Well-Maintained Fleet</h3>
                    <p>Clean, sanitized, and regularly serviced vehicles for your comfort and safety.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon-large">🕐</div>
                    <h3>24/7 Availability</h3>
                    <p>Round-the-clock service for early morning flights or late-night arrivals.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon-large">❌</div>
                    <h3>Free Cancellation</h3>
                    <p>Cancel up to 24 hours before pickup with full refund. Flexible and customer-friendly.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials" class="testimonials-section">
        <div class="container">
            <h2 class="section-title">What Our Customers Say</h2>
            <p class="section-subtitle">Real reviews from travelers who chose Kumaon Drive</p>
            
            <div class="testimonials-grid">
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <div class="rating">
                        <span>⭐⭐⭐⭐⭐</span>
                        <span class="rating-text">5.0</span>
                    </div>
                    <p class="testimonial-text">"Excellent service! The driver was punctual and very professional. The car was clean and comfortable. Highly recommend for Nainital trips. Will definitely book again for our next visit!"</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">RK</div>
                        <div class="author-info">
                            <strong>Rajesh Kumar</strong>
                            <span>Delhi • Booked Sedan</span>
                        </div>
                    </div>
                </div>
                
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <div class="rating">
                        <span>⭐⭐⭐⭐⭐</span>
                        <span class="rating-text">5.0</span>
                    </div>
                    <p class="testimonial-text">"Booked for our family trip to Ranikhet. Amazing experience! Fair pricing and the driver knew all the best routes and scenic spots. The kids loved the journey. Thank you Kumaon Drive!"</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">PS</div>
                        <div class="author-info">
                            <strong>Priya Sharma</strong>
                            <span>Mumbai • Booked SUV</span>
                        </div>
                    </div>
                </div>
                
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <div class="rating">
                        <span>⭐⭐⭐⭐⭐</span>
                        <span class="rating-text">5.0</span>
                    </div>
                    <p class="testimonial-text">"Very reliable service. Used them for Jim Corbett safari trip. The booking process was smooth and instant confirmation via SMS was great! Driver was knowledgeable about wildlife routes."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">AP</div>
                        <div class="author-info">
                            <strong>Amit Patel</strong>
                            <span>Bangalore • Booked Innova</span>
                        </div>
                    </div>
                </div>
                
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <div class="rating">
                        <span>⭐⭐⭐⭐⭐</span>
                        <span class="rating-text">5.0</span>
                    </div>
                    <p class="testimonial-text">"Best taxi service in Kumaon region! Driver arrived on time at Kathgodam station. Very comfortable ride to Nainital. The vehicle was spotless and well-maintained. Highly professional service."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">SK</div>
                        <div class="author-info">
                            <strong>Sneha Kapoor</strong>
                            <span>Chandigarh • Booked Sedan</span>
                        </div>
                    </div>
                </div>
                
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <div class="rating">
                        <span>⭐⭐⭐⭐⭐</span>
                        <span class="rating-text">5.0</span>
                    </div>
                    <p class="testimonial-text">"Used for Delhi to Nainital long trip. Driver was courteous and took regular breaks. Transparent pricing with no hidden charges. The online booking was super easy. Will recommend to everyone!"</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">VG</div>
                        <div class="author-info">
                            <strong>Vikram Gupta</strong>
                            <span>Noida • Booked SUV</span>
                        </div>
                    </div>
                </div>
                
                <div class="testimonial-card">
                    <div class="quote-icon">"</div>
                    <div class="rating">
                        <span>⭐⭐⭐⭐⭐</span>
                        <span class="rating-text">5.0</span>
                    </div>
                    <p class="testimonial-text">"Fantastic service for our Mukteshwar weekend getaway. Driver was friendly and gave us great tips about local attractions. The hatchback was perfect for two people. Value for money!"</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">MJ</div>
                        <div class="author-info">
                            <strong>Meera Joshi</strong>
                            <span>Dehradun • Booked Hatchback</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact-section">
        <div class="container">
            <h2 class="section-title">Get In Touch</h2>
            <p class="section-subtitle">We're here to help 24/7. Reach out anytime!</p>
            
            <div class="contact-grid">
                <div class="contact-card">
                    <div class="contact-icon-large">📞</div>
                    <h3>Phone</h3>
                    <a href="tel:+919876543210" class="contact-link">+91-98765-43210</a>
                    <p class="contact-description">24/7 Booking Support</p>
                    <a href="tel:+919876543210" class="btn-contact">Call Now</a>
                </div>
                
                <div class="contact-card">
                    <div class="contact-icon-large">💬</div>
                    <h3>WhatsApp</h3>
                    <a href="https://wa.me/919876543210?text=Hi, I want to book a cab with Kumaon Drive" class="contact-link">+91-98765-43210</a>
                    <p class="contact-description">Instant Booking & Queries</p>
                    <a href="https://wa.me/919876543210?text=Hi, I want to book a cab with Kumaon Drive" class="btn-contact" target="_blank">Chat on WhatsApp</a>
                </div>
                
                <div class="contact-card">
                    <div class="contact-icon-large">📧</div>
                    <h3>Email</h3>
                    <a href="mailto:bookings@kumaondrive.com" class="contact-link">bookings@kumaondrive.com</a>
                    <p class="contact-description">For Business Inquiries</p>
                    <a href="mailto:bookings@kumaondrive.com" class="btn-contact">Send Email</a>
                </div>
                
                <div class="contact-card">
                    <div class="contact-icon-large">📍</div>
                    <h3>Location</h3>
                    <p class="contact-link">Nainital, Uttarakhand</p>
                    <p class="contact-description">Serving entire Kumaon region</p>
                    <a href="https://goo.gl/maps/example" class="btn-contact" target="_blank">View on Map</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="site-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>About Kumaon Drive</h3>
                    <p>Your trusted travel partner in the beautiful Kumaon region of Uttarakhand. We provide safe, comfortable, and affordable taxi services for all your travel needs across Nainital, Ranikhet, Jim Corbett, and beyond.</p>
                    <div class="social-links">
                        <a href="#" aria-label="Facebook">📘</a>
                        <a href="#" aria-label="Instagram">📷</a>
                        <a href="#" aria-label="Twitter">🐦</a>
                        <a href="#" aria-label="YouTube">📺</a>
                    </div>
                </div>
                
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <ul class="footer-links">
                        <li><a href="#booking">Book a Cab</a></li>
                        <li><a href="#fleet">Our Vehicles</a></li>
                        <li><a href="#routes">Popular Destinations</a></li>
                        <li><a href="#testimonials">Customer Reviews</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Blog</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>Popular Routes</h3>
                    <ul class="footer-links">
                        <li><a href="#">Kathgodam to Nainital</a></li>
                        <li><a href="#">Delhi to Nainital</a></li>
                        <li><a href="#">Nainital to Ranikhet</a></li>
                        <li><a href="#">Nainital to Jim Corbett</a></li>
                        <li><a href="#">Nainital to Mukteshwar</a></li>
                        <li><a href="#">Nainital to Bhimtal</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>Important Links</h3>
                    <ul class="footer-links">
                        <li><a href="#">Privacy Policy</a></li>
                        <li><a href="#">Terms & Conditions</a></li>
                        <li><a href="#">Cancellation Policy</a></li>
                        <li><a href="#">Refund Policy</a></li>
                        <li><a href="#">FAQ</a></li>
                        <li><a href="#">Contact Support</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 Kumaon Drive. All rights reserved. | Designed for the Beautiful Kumaon Region of Uttarakhand</p>
                <p class="footer-tagline">🏔️ Explore Mountains • Experience Comfort • Create Memories 🚗</p>
            </div>
        </div>
    </footer>

    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/919876543210?text=Hi, I want to book a cab with Kumaon Drive" class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp">
        <svg viewBox="0 0 32 32" width="32" height="32">
            <path fill="white" d="M16 0c-8.837 0-16 7.163-16 16 0 2.825 0.737 5.607 2.137 8.048l-2.137 7.952 7.933-2.127c2.42 1.37 5.173 2.127 8.067 2.127 8.837 0 16-7.163 16-16s-7.163-16-16-16zM16 29.467c-2.482 0-4.908-0.646-7.07-1.87l-0.507-0.292-4.713 1.262 1.262-4.669-0.292-0.508c-1.207-2.100-1.847-4.507-1.847-6.923 0-7.435 6.050-13.485 13.485-13.485s13.485 6.050 13.485 13.485c0 7.435-6.050 13.485-13.485 13.485zM21.960 18.537c-0.307-0.153-1.813-0.893-2.093-0.996s-0.485-0.153-0.69 0.153c-0.204 0.307-0.792 0.996-0.971 1.201s-0.358 0.230-0.665 0.077c-0.307-0.153-1.296-0.478-2.467-1.524-0.912-0.813-1.528-1.817-1.707-2.124s-0.018-0.472 0.135-0.626c0.138-0.137 0.307-0.358 0.461-0.537s0.204-0.307 0.307-0.512 0.051-0.384-0.026-0.537c-0.077-0.153-0.69-1.663-0.946-2.278-0.25-0.598-0.503-0.517-0.69-0.526-0.179-0.009-0.384-0.011-0.589-0.011s-0.537 0.077-0.818 0.384c-0.281 0.307-1.073 1.048-1.073 2.556s1.099 2.964 1.252 3.169c0.153 0.204 2.159 3.299 5.231 4.625 0.731 0.315 1.302 0.504 1.747 0.645 0.734 0.234 1.402 0.201 1.929 0.122 0.588-0.088 1.813-0.741 2.068-1.456s0.255-1.329 0.179-1.456c-0.077-0.128-0.281-0.204-0.588-0.358z"/>
        </svg>
    </a>

    <!-- Scroll to Top Button -->
    <button id="scroll-to-top" class="scroll-to-top" aria-label="Scroll to top" style="display: none;">
        <span>↑</span>
    </button>

    <!-- Success Modal -->
    <div id="success-modal" class="modal" style="display: none;">
        <div class="modal-content">
            <div class="modal-header">
                <span class="close-modal" id="close-modal">&times;</span>
            </div>
            <div class="modal-body">
                <div class="success-icon">✓</div>
                <h2>Booking Confirmed!</h2>
                <p id="modal-message">Your booking has been confirmed successfully.</p>
                <p><strong>Booking ID:</strong> <span id="modal-booking-id"></span></p>
                <p class="modal-note">You will receive a confirmation SMS and email shortly with all the details.</p>
                <button class="btn-primary" id="modal-close-btn">Close</button>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="js/script.js"></script>
</body>
</html>
"""

with open(f"{html_base}/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✓ Created complete index.html with all sections")
print(f"  - Hero section with animated features")
print(f"  - Advanced booking form with validation")
print(f"  - Vehicle fleet showcase")
print(f"  - Popular routes with auto-fill")
print(f"  - Customer testimonials")
print(f"  - Contact section")
print(f"  - Complete footer")
