
# Create README and deployment guide
readme_content = """# Kumaon Drive - Production Website

## 🚗 Complete Taxi Booking Website for Kumaon Region, Uttarakhand

A fully functional, production-ready website with automated booking system, instant fare calculation, and real-time SMS/email confirmations.

---

## 📋 Features

### Core Functionality
- ✅ **Instant Online Booking** - Real-time fare calculation with automatic confirmation
- ✅ **Multiple Vehicle Options** - Hatchback, Sedan, SUV, Premium SUV (Innova)
- ✅ **Smart Fare Calculator** - Distance-based pricing with automatic toll and allowance calculation
- ✅ **Indian Currency (₹ INR)** - All pricing in Rupees with proper formatting
- ✅ **Popular Routes** - Pre-configured routes with one-click auto-fill
- ✅ **SMS & Email Confirmations** - Instant booking notifications (requires gateway setup)
- ✅ **WhatsApp Integration** - Floating button for quick inquiries
- ✅ **Mobile Responsive** - Perfect on all devices

### User Experience
- 🎨 Green branding matching Kumaon Drive logo
- 📱 Mobile-first responsive design
- ⚡ Fast loading and smooth animations
- 🔒 Form validation and error handling
- 💬 WhatsApp quick contact button
- 📞 Click-to-call functionality

### Business Features
- 💰 Transparent pricing breakdown
- 🚙 Vehicle fleet showcase
- ⭐ Customer testimonials
- 📍 Popular Kumaon destinations
- 🎯 SEO optimized structure
- 📊 Google Analytics ready

---

## 📁 File Structure

```
kumaon-drive-html/
├── index.html              # Main website file
├── css/
│   └── style.css          # All styling (responsive)
├── js/
│   └── script.js          # Interactive features & booking logic
├── images/
│   └── kumaon-drive-logo.png  # Your logo (add this file)
└── README.md              # This file
```

---

## 🚀 Quick Start

### Option 1: Static HTML Hosting (Fastest)

1. **Upload Files**
   - Upload all files to any web hosting (Hostinger, Bluehost, etc.)
   - Or use free hosting: Netlify, Vercel, GitHub Pages

2. **Add Your Logo**
   - Save your logo as `images/kumaon-drive-logo.png`
   - Recommended size: 200x70 pixels (transparent PNG)

3. **Update Contact Information**
   - Open `index.html` and `js/script.js`
   - Replace `+919876543210` with your actual phone number (appears ~10 times)
   - Replace `bookings@kumaondrive.com` with your email

4. **Test Locally**
   - Open `index.html` in your browser
   - Test all features before deploying

### Option 2: Deploy to Netlify (Free, Recommended)

1. Create account at https://netlify.com
2. Drag and drop the `kumaon-drive-html` folder
3. Get instant live URL: `your-site.netlify.app`
4. Optional: Connect custom domain

### Option 3: Deploy to GitHub Pages (Free)

1. Create GitHub repository
2. Upload files to repo
3. Enable GitHub Pages in settings
4. Access at `username.github.io/repo-name`

---

## ⚙️ Configuration

### 1. Contact Information Updates

**In index.html**, replace all instances of:
- `+919876543210` → Your phone number
- `bookings@kumaondrive.com` → Your email address

**In js/script.js**, line 8-12:
```javascript
const CONFIG = {
    phone: '+91XXXXXXXXXX',  // Your phone
    email: 'your@email.com',  // Your email
    // ... rest remains same
};
```

### 2. Vehicle Rates (if needed)

**In js/script.js**, line 13-24:
```javascript
rates: {
    hatchback: 9,   // ₹ per km
    sedan: 11,
    suv: 13,
    innova: 18
},
fullDayRates: {
    hatchback: 1400,  // ₹ full day
    sedan: 1500,
    suv: 2000,
    innova: 5500
}
```

### 3. WhatsApp Setup

Update WhatsApp links (appears 3 times in index.html):
```html
https://wa.me/919876543210  →  https://wa.me/91XXXXXXXXXX
```

---

## 📧 Setting Up Email & SMS (Production)

### Email Confirmation Setup

**Option A: EmailJS (Free, Easy)**
1. Sign up at https://www.emailjs.com
2. Create email template
3. Add EmailJS SDK to index.html:
```html
<script src="https://cdn.emailjs.com/dist/email.min.js"></script>
```
4. Update `sendConfirmationEmail()` function in script.js

**Option B: Backend API**
- Use PHP mail() function
- Or integrate with SendGrid, Mailgun, AWS SES

### SMS Confirmation Setup

**Option A: MSG91 (India, ₹0.15/SMS)**
1. Register at https://msg91.com
2. Get API key and sender ID
3. Update `sendConfirmationSMS()` in script.js:
```javascript
fetch('https://api.msg91.com/api/v5/flow/', {
    method: 'POST',
    headers: { 'authkey': 'YOUR_API_KEY' },
    body: JSON.stringify({
        sender: 'KUMDRV',
        mobiles: formData.customer_phone,
        message: message
    })
});
```

**Option B: Twilio**
- Global service
- Easy integration
- ~$0.02/SMS in India

---

## 💳 Payment Gateway Integration

### Razorpay Setup (Recommended for India)

1. **Register**: https://razorpay.com
2. **Get Credentials**: API Key & Secret
3. **Add Razorpay Checkout**:

In index.html before `</body>`:
```html
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
```

In script.js after form validation:
```javascript
const options = {
    key: 'rzp_live_XXXXXXXXXXXX',
    amount: formData.fare * 100,  // Amount in paise
    currency: 'INR',
    name: 'Kumaon Drive',
    description: 'Taxi Booking',
    handler: function(response) {
        // Payment successful - submit booking
        console.log('Payment ID:', response.razorpay_payment_id);
    }
};
const rzp = new Razorpay(options);
rzp.open();
```

---

## 🗺️ Google Maps Integration (Optional)

1. Get API key from Google Cloud Console
2. Enable Maps JavaScript API & Places API
3. Add before `</head>` in index.html:
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places"></script>
```

4. Add autocomplete in script.js:
```javascript
const pickup = new google.maps.places.Autocomplete(
    document.getElementById('pickup_location')
);
```

---

## 🎨 Customization

### Change Brand Colors

In css/style.css, update lines 22-27:
```css
:root {
    --primary-green: #228B22;   /* Your brand color */
    --dark-green: #1B5E1F;
    --light-green: #90EE90;
    --accent-green: #32CD32;
}
```

### Add More Routes

In index.html, duplicate any `.route-card` div and update:
- `data-from="Start Location"`
- `data-to="End Location"`
- `data-distance="XX"` (in km)
- Route description

### Modify Testimonials

In index.html, find `.testimonial-card` sections and update:
- Customer names
- Review text
- Star ratings
- Cities

---

## 📊 Analytics Setup

### Google Analytics 4

1. Create GA4 property at https://analytics.google.com
2. Add tracking code before `</head>` in index.html:
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 🔧 Backend Setup (Optional)

For production-grade booking management, create a simple backend:

### PHP Backend Example

Create `api/booking.php`:
```php
<?php
header('Content-Type: application/json');

$data = json_decode(file_get_contents('php://input'), true);

// Validate data
// Save to database
// Send email
// Send SMS
// Return booking ID

echo json_encode(['success' => true, 'booking_id' => $bookingId]);
?>
```

Update script.js form submission:
```javascript
fetch('/api/booking.php', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData)
})
.then(response => response.json())
.then(data => showSuccessModal(data.booking_id, formData));
```

---

## 🌐 Domain Setup

### Connect Custom Domain

**For Netlify:**
1. Go to Domain settings
2. Add custom domain: `kumaondrive.com`
3. Update DNS records at your registrar

**For Hostinger/cPanel:**
1. Point domain to hosting
2. Upload files to public_html
3. SSL auto-configured

---

## ✅ Pre-Launch Checklist

- [ ] Logo uploaded to images folder
- [ ] All phone numbers updated (search +919876543210)
- [ ] All email addresses updated
- [ ] WhatsApp number configured
- [ ] Test fare calculator with different distances
- [ ] Test form submission and validation
- [ ] Check mobile responsiveness
- [ ] Setup email confirmation (EmailJS or backend)
- [ ] Setup SMS confirmation (MSG91 or Twilio)
- [ ] Payment gateway configured (Razorpay)
- [ ] Google Analytics added
- [ ] Test on multiple browsers
- [ ] SSL certificate active (https://)
- [ ] Google My Business listing created
- [ ] Social media links added

---

## 🚨 Troubleshooting

### Issue: Form doesn't submit
- Check browser console for errors
- Ensure all required fields filled
- Verify "Calculate Fare" clicked first

### Issue: Fare calculation shows 0
- Verify distance, vehicle type selected
- Check browser console for JavaScript errors
- Ensure script.js loaded properly

### Issue: SMS not sending
- Verify SMS gateway credentials
- Check API endpoint and format
- Test with small credits first

### Issue: Mobile menu not working
- Clear browser cache
- Check if script.js loaded
- Verify mobile-toggle element exists

---

## 📈 Marketing Tips

1. **Google My Business** - Create listing with photos and booking link
2. **Facebook Page** - Share booking link, customer reviews
3. **Instagram** - Post Kumaon travel photos with booking CTA
4. **WhatsApp Business** - Auto-replies with booking link
5. **Local SEO** - Target "Nainital taxi", "Kumaon cab service"
6. **Google Ads** - Run campaigns for tourist season
7. **Partnerships** - Hotels, homestays, travel agents

---

## 🔐 Security Best Practices

- Use HTTPS (SSL certificate)
- Sanitize all form inputs
- Implement rate limiting on form submission
- Use environment variables for API keys
- Regular backups of booking data
- GDPR-compliant privacy policy

---

## 📞 Support

For technical issues or customization help:
- Email: [your-support-email]
- Phone: [your-number]

---

## 📄 License

This website is created for Kumaon Drive taxi service.
All rights reserved © 2025 Kumaon Drive

---

## 🎉 Congratulations!

Your complete taxi booking website is ready to go live!

**Next Steps:**
1. Deploy to web hosting
2. Update contact information
3. Setup payment gateway
4. Test thoroughly
5. Go live and start receiving bookings!

🚗 Happy booking and safe travels in beautiful Kumaon! 🏔️
"""

with open(f"{html_base}/README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✓ Created comprehensive README.md")
print("✓ Includes deployment instructions")
print("✓ Email/SMS setup guide")
print("✓ Payment gateway integration")
print("✓ Customization guide")
print("✓ Pre-launch checklist")
