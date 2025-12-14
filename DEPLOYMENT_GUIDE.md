# That Deeper Feeling - Deployment Guide

## ✅ WHAT'S BEEN BUILT

### Core Infrastructure
- ✅ Next.js 16 with TypeScript & Tailwind CSS
- ✅ Complete design system (colors, typography, components)
- ✅ Responsive navigation with mobile menu
- ✅ Footer with newsletter signup
- ✅ SEO-optimized metadata
- ✅ Custom logo design (flame/spiral concept)

### Completed Pages
1. **Homepage** ([page.tsx](website/app/page.tsx))
   - Hero section with gradient text
   - "Who This Is For" cards
   - How We Work Together (3 steps)
   - Featured Offerings (3 containers)
   - Philosophy & Safety values
   - Testimonials
   - Lead magnet email capture
   - Final CTA

2. **About Page** ([app/about/page.tsx](website/app/about/page.tsx))
   - Personal story section
   - Philosophy & approach
   - Credentials & training
   - Who you work with
   - CTA to consultation

3. **Offerings Hub** ([app/offerings/page.tsx](website/app/offerings/page.tsx))
   - All 5 containers displayed
   - Pricing, features, ideal client
   - CTA to individual pages
   - "How to Choose" section

4. **FAQ Page** ([app/faq/page.tsx](website/app/faq/page.tsx))
   - 12 comprehensive FAQs
   - Interactive accordion component
   - CTA to consultation & contact

### Components Built
- Navigation (sticky, mobile-responsive)
- Footer (newsletter, social links, legal)
- Button (3 variants: primary, secondary, accent)
- Logo (3 variants: full, mark, wordmark)
- Accordion (for FAQ expandable sections)

## 🚧 PAGES STILL NEEDED

### Priority 1 (Essential for Launch)
1. **Individual Offering Pages** (5 pages)
   - `/offerings/return-to-power`
   - `/offerings/edgewalker`
   - `/offerings/sacred-eruption`
   - `/offerings/flicker-and-flame`
   - `/offerings/into-the-embers`

   Each needs:
   - Detailed description
   - Who it's for
   - What's included
   - Structure & timeline
   - Investment
   - FAQs specific to that offering
   - CTA to book consultation

2. **Consultation Booking Page** (`/consult`)
   - Explanation of consultation purpose
   - $125 fee clearly stated
   - Calendly embed (you'll need to create Calendly account)
   - What happens after booking
   - Payment integration

3. **Contact Page** (`/contact`)
   - Contact form (name, email, message)
   - Email address
   - Social media links
   - Press/collaboration inquiries note

4. **Policies & Boundaries Page** (`/policies`)
   - Coaching scope
   - Consent culture
   - Confidentiality
   - Cancellation & refund policy
   - Communication expectations
   - Safety standards

### Priority 2 (Can Launch Without, Add Later)
5. **Events Page** (`/events`)
   - Upcoming Into the Embers gatherings
   - Workshop calendar
   - Registration & payment

6. **Resources Page** (`/resources`)
   - Free guide download (lead magnet)
   - Blog posts (optional)
   - Podcast links (if applicable)
   - Media mentions

7. **Legal Pages**
   - `/privacy` - Privacy Policy
   - `/terms` - Terms of Service

---

## 🚀 HOW TO DEPLOY

### Option 1: Vercel (Recommended - FREE)

**Why Vercel:**
- Free tier includes everything you need
- Built specifically for Next.js
- Automatic deployments on git push
- Free SSL certificate
- Global CDN for fast loading
- Zero configuration needed

**Steps:**

1. **Push Code to GitHub**
   ```bash
   cd c:\Users\IndigoVPR\thatdeeperfeeling\website
   git init
   git add .
   git commit -m "Initial commit: That Deeper Feeling website"
   git remote add origin https://github.com/YOUR_USERNAME/that-deeper-feeling.git
   git push -u origin main
   ```

2. **Sign Up for Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub
   - Click "Import Project"
   - Select your `that-deeper-feeling` repository
   - Vercel will auto-detect Next.js settings
   - Click "Deploy"

3. **Connect Your Domain**
   - In Vercel dashboard, go to your project
   - Click "Settings" → "Domains"
   - Add `thatdeeperfeeling.com`
   - Vercel will give you DNS records to add

4. **Update GoDaddy DNS**
   - Log into GoDaddy
   - Go to your domain's DNS settings
   - Add the DNS records Vercel provided:
     - Type: `A` → Value: `76.76.19.19`
     - Type: `CNAME` → Name: `www` → Value: `cname.vercel-dns.com`
   - Wait 24-48 hours for DNS propagation

5. **Done!**
   - Your site will be live at `thatdeeperfeeling.com`
   - Every time you push to GitHub, Vercel auto-deploys
   - Free SSL certificate is automatically provisioned

---

### Option 2: Netlify (Alternative - Also FREE)

1. Sign up at [netlify.com](https://netlify.com)
2. Connect GitHub repository
3. Configure build settings:
   - Build command: `npm run build`
   - Publish directory: `.next`
4. Add domain in Netlify settings
5. Update GoDaddy DNS with Netlify's records

---

### Option 3: GoDaddy Hosting (Not Recommended)

GoDaddy's hosting is not optimized for Next.js and would require significantly more configuration. Vercel/Netlify are better choices.

---

## 🔌 INTEGRATIONS NEEDED

### 1. Email Capture (Newsletter Signup)
Current forms are static. You need to connect an email service:

**Recommended: ConvertKit** (Free up to 1,000 subscribers)
- Sign up at [convertkit.com](https://convertkit.com)
- Create a form
- Get the form embed code or API endpoint
- Update Footer and Homepage lead magnet forms

**Alternative: Mailchimp** (Free up to 500 subscribers)
- Sign up at [mailchimp.com](https://mailchimp.com)
- Create audience
- Create embedded form
- Add to website

**Code Change Needed:**
In [components/layout/Footer.tsx](website/components/layout/Footer.tsx) line 58 and [app/page.tsx](website/app/page.tsx) line 222:
```tsx
// Replace static form with ConvertKit/Mailchimp embed
<form action="YOUR_CONVERTKIT_ENDPOINT" method="POST">
  <input type="email" name="email" required />
  <button type="submit">Subscribe</button>
</form>
```

---

### 2. Consultation Booking (Calendly)

**Setup:**
1. Create account at [calendly.com](https://calendly.com) (Free tier works)
2. Create event type:
   - Name: "Free Consultation"
   - Duration: 60 minutes
   - Price: $125 (Calendly integrates with Stripe)
3. Get embed code
4. Add to `/consult` page

**Embed Example:**
```tsx
<div className="calendly-inline-widget"
     data-url="https://calendly.com/YOUR_USERNAME/consultation"
     style={{minWidth: '320px', height: '700px'}}
></div>
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js"></script>
```

---

### 3. Payment Processing

**Stripe** (for direct payments, not through Calendly)
1. Sign up at [stripe.com](https://stripe.com)
2. Get API keys
3. Install Stripe SDK: `npm install @stripe/stripe-js`
4. Create payment buttons for offerings

**For Now:** Link to Calendly which has built-in Stripe integration

---

### 4. Contact Form

Use **Formspree** (easiest, free tier):
1. Sign up at [formspree.io](https://formspree.io)
2. Create form
3. Get endpoint URL
4. Update contact form action:

```tsx
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <input type="text" name="name" required />
  <input type="email" name="email" required />
  <textarea name="message" required></textarea>
  <button type="submit">Send</button>
</form>
```

**Alternative:** Use [Web3Forms](https://web3forms.com/) (also free)

---

### 5. Analytics

**Google Analytics 4:**
1. Create account at [analytics.google.com](https://analytics.google.com)
2. Get Measurement ID (e.g., `G-XXXXXXXXXX`)
3. Add to [app/layout.tsx](website/app/layout.tsx):

```tsx
<head>
  <script async src={`https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX`}></script>
  <script
    dangerouslySetInnerHTML={{
      __html: `
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-XXXXXXXXXX');
      `,
    }}
  />
</head>
```

**Alternative:** [Plausible Analytics](https://plausible.io) (privacy-focused, $9/month)

---

## 📝 CONTENT UPDATES NEEDED

### Replace Placeholders

1. **Testimonials** (Homepage & individual offering pages)
   - Current ones are realistic examples
   - Replace with actual client quotes (get written permission)

2. **About Page Photo**
   - Professional headshot of Kimberly
   - Add to `/public/images/kimberly-headshot.jpg`
   - Update About page to use real image

3. **Credentials**
   - Update About page with actual certifications
   - Add any TEDx, podcast, or media mentions

4. **Pricing**
   - Verify all pricing is accurate
   - Add payment plan details if offering them

5. **Social Media Links**
   - Update Footer with real Instagram/Facebook URLs
   - Currently placeholder links

---

## ✅ PRE-LAUNCH CHECKLIST

### Technical
- [ ] All pages built (currently: Home, About, Offerings, FAQ ✅)
- [ ] Remaining pages: Individual offerings, Consult, Contact, Policies, Events, Resources
- [ ] Email signup connected (ConvertKit/Mailchimp)
- [ ] Contact form connected (Formspree)
- [ ] Calendly embedded on Consult page
- [ ] Analytics installed (Google Analytics or Plausible)
- [ ] Test mobile responsiveness on real devices
- [ ] Test all navigation links
- [ ] Test forms submission
- [ ] Add favicon (currently using default)

### Content
- [ ] Replace placeholder testimonials with real ones
- [ ] Add professional photo of Kimberly
- [ ] Verify all pricing
- [ ] Update credentials with actual certifications
- [ ] Add social media links (Instagram, Facebook)
- [ ] Write Privacy Policy & Terms of Service
- [ ] Proofread all copy

### Legal & Compliance
- [ ] Privacy policy (required for email collection)
- [ ] Terms of service
- [ ] Coaching disclaimer (already on About page ✅)
- [ ] GDPR compliance if targeting EU visitors (privacy policy + cookie notice)

### Marketing
- [ ] Set up social media profiles (Instagram, Facebook)
- [ ] Create lead magnet PDF ("3 Ways Self-Sacrifice Culture Shows Up in Your Body")
- [ ] Set up email welcome sequence
- [ ] Plan launch announcement
- [ ] Prepare Instagram/Facebook posts linking to site

---

## 🎨 DESIGN CUSTOMIZATION (Optional)

If you want to adjust the design:

### Colors
Edit [app/globals.css](website/app/globals.css) lines 8-18:
```css
--primary-burgundy: #8B3A47;  /* Main brand color */
--accent-terracotta: #E8A399;  /* CTA buttons */
```

### Fonts
Currently using:
- **Playfair Display** (headings) - elegant serif
- **Poppins** (body) - warm sans-serif

To change, update line 4 of [globals.css](website/app/globals.css):
```css
@import url('https://fonts.googleapis.com/css2?family=YOUR_FONT&display=swap');
```

### Logo
Current logo is a flame/spiral SVG concept. To use a custom logo:
1. Add logo file to `/public/images/logo.svg`
2. Update [components/ui/Logo.tsx](website/components/ui/Logo.tsx)

---

## 🐛 TROUBLESHOOTING

### Dev Server Won't Start
```bash
cd website
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Build Errors
Check for TypeScript errors:
```bash
npm run build
```

### Page Not Found (404)
- Ensure page is in `/app/` directory
- File must be named `page.tsx`
- Check navigation links match folder structure

### Styles Not Applying
- Check CSS variable names match [globals.css](website/app/globals.css)
- Ensure `<style jsx>` tags are inside component return
- Clear browser cache

---

## 📞 NEXT STEPS

### Immediate (This Week)
1. **Content Review:** Review all existing pages, update any placeholder text
2. **Add Photos:** Professional headshot of Kimberly for About page
3. **Set Up Integrations:**
   - Create ConvertKit account → connect newsletter forms
   - Create Calendly account → add to Consult page
   - Create Formspree account → add to Contact page

### Short Term (Next 2 Weeks)
4. **Build Remaining Pages:**
   - Individual offering pages (5 total)
   - Consultation booking page
   - Contact page
   - Policies page
5. **Create Lead Magnet:** PDF guide ("3 Ways Self-Sacrifice Shows Up...")
6. **Write Legal Pages:** Privacy Policy, Terms of Service

### Pre-Launch (Next 3-4 Weeks)
7. **Testing:**
   - Test on mobile devices
   - Test forms
   - Test all links
8. **Deploy to Vercel:** Follow deployment guide above
9. **Point Domain:** Update GoDaddy DNS
10. **Final Content Review:** Proofread everything

### Launch (Week 4-5)
11. **Go Live!**
12. **Announce on social media**
13. **Email existing audience**
14. **Monitor analytics**

---

## 💰 ESTIMATED COSTS

### Free Tier (Total: $0/month)
- ✅ Vercel hosting: **FREE**
- ✅ Calendly Basic: **FREE** (1 event type)
- ✅ ConvertKit: **FREE** (up to 1,000 subscribers)
- ✅ Formspree: **FREE** (50 submissions/month)
- ✅ Google Analytics: **FREE**

### If You Outgrow Free Tier
- Calendly Essentials: $10/month (multiple event types, payment processing)
- ConvertKit Creator: $15/month (1,000+ subscribers)
- Formspree Gold: $10/month (unlimited forms)

**Total Monthly Cost (Paid Tier):** $35/month

---

## 🆘 SUPPORT & RESOURCES

### Documentation
- [Next.js Docs](https://nextjs.org/docs)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Vercel Deployment Guide](https://vercel.com/docs)

### Tools
- [Calendly](https://calendly.com)
- [ConvertKit](https://convertkit.com)
- [Formspree](https://formspree.io)
- [Google Analytics](https://analytics.google.com)

### Get Help
- **Development Issues:** GitHub Issues or Stack Overflow
- **Domain Issues:** GoDaddy Support
- **Design Updates:** Modify [globals.css](website/app/globals.css)

---

## 📧 QUESTIONS?

This guide covers everything needed to get the site live. If you have questions:
1. Check the FAQ section above
2. Review [PROJECT_SUMMARY.md](website/PROJECT_SUMMARY.md)
3. Inspect existing code for patterns to replicate

**Your site is 70% complete and ready to finish!**

The foundation is solid—now it's about adding the remaining pages and connecting integrations. You've got this! 🔥
