# That Deeper Feeling - Website Project

**Conscious Intimacy Coaching by Kimberly Bryant**

🌐 **Domain:** [thatdeeperfeeling.com](https://thatdeeperfeeling.com)
🎨 **Design:** Grounded, Sensual, Sacred
⚡ **Tech:** Next.js 16 + TypeScript + Tailwind CSS

---

## 🚀 Quick Start

### Development Server
```bash
cd website
npm install          # First time only
npm run dev         # Start development server
```

Visit: **http://localhost:3000**

### Production Build
```bash
npm run build       # Build for production
npm run start       # Run production build locally
```

---

## 📊 Project Status

### ✅ Completed (70%)
- [x] Design system & brand identity
- [x] Navigation & Footer
- [x] Homepage (hero, offerings, testimonials, lead magnet)
- [x] About page
- [x] Offerings hub page
- [x] FAQ page with accordion

### 🚧 In Progress (30%)
- [ ] Individual offering pages (5 total)
- [ ] Consultation booking page
- [ ] Contact page
- [ ] Policies & Boundaries page
- [ ] Events page
- [ ] Resources page
- [ ] Email/form integrations

---

## 📁 File Structure

```
thatdeeperfeeling/
├── website/                    # Main Next.js application
│   ├── app/                    # Pages & routes
│   │   ├── page.tsx           # ✅ Homepage
│   │   ├── about/page.tsx     # ✅ About page
│   │   ├── offerings/page.tsx # ✅ Offerings hub
│   │   ├── faq/page.tsx       # ✅ FAQ page
│   │   ├── consult/           # 🚧 Booking page
│   │   ├── contact/           # 🚧 Contact form
│   │   ├── policies/          # 🚧 Policies page
│   │   ├── events/            # 🚧 Events calendar
│   │   └── resources/         # 🚧 Resources page
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Navigation.tsx # ✅ Sticky nav
│   │   │   └── Footer.tsx     # ✅ Footer
│   │   └── ui/
│   │       ├── Button.tsx     # ✅ Reusable button
│   │       ├── Logo.tsx       # ✅ Brand logo
│   │       └── Accordion.tsx  # ✅ FAQ accordion
│   ├── public/                # Static assets
│   └── globals.css            # ✅ Design system
├── DEPLOYMENT_GUIDE.md        # 📘 How to deploy
├── PROJECT_SUMMARY.md         # 📘 Technical details
└── README.md                  # 📘 You are here
```

---

## 🎨 Brand Identity

### Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| **Primary Burgundy** | `#8B3A47` | Main brand, headings |
| **Primary Wine** | `#6B2D3A` | Deeper accents |
| **Accent Terracotta** | `#E8A399` | CTAs, highlights |
| **Neutral Cream** | `#F5F1E8` | Backgrounds |
| **Neutral Soft White** | `#FDFCF9` | Primary background |

### Typography
- **Headings:** Playfair Display (serif, elegant)
- **Body:** Poppins (sans-serif, warm, readable)

### Design Principles
✨ Grounded • Sensual • Sacred • Safe • Bold

---

## 🔧 Integrations Needed

### Email Capture
- **Service:** [ConvertKit](https://convertkit.com) or Mailchimp
- **Location:** Footer newsletter, Homepage lead magnet
- **Status:** 🔴 Not connected (forms are static)

### Consultation Booking
- **Service:** [Calendly](https://calendly.com)
- **Page:** `/consult`
- **Status:** 🔴 Not built yet

### Contact Form
- **Service:** [Formspree](https://formspree.io) or Web3Forms
- **Page:** `/contact`
- **Status:** 🔴 Not built yet

### Analytics
- **Service:** Google Analytics 4 or Plausible
- **Status:** 🔴 Not installed

---

## 📋 Next Steps

### Phase 1: Complete Core Pages (Priority)
1. **Build Individual Offering Pages**
   - `/offerings/return-to-power`
   - `/offerings/edgewalker`
   - `/offerings/sacred-eruption`
   - `/offerings/flicker-and-flame`
   - `/offerings/into-the-embers`

2. **Build Consultation Page** (`/consult`)
   - Add Calendly embed
   - Explain consultation process
   - Show $125 fee

3. **Build Contact Page** (`/contact`)
   - Contact form
   - Email & social links

4. **Build Policies Page** (`/policies`)
   - Coaching scope
   - Consent & boundaries
   - Refund policy
   - Confidentiality

### Phase 2: Integrations
5. Connect ConvertKit/Mailchimp for email signup
6. Add Calendly booking to Consult page
7. Connect Formspree for contact form
8. Install Google Analytics

### Phase 3: Content & Polish
9. Replace placeholder testimonials
10. Add professional photos
11. Create lead magnet PDF
12. Write Privacy Policy & Terms

### Phase 4: Deploy
13. Push to GitHub
14. Deploy to Vercel (free)
15. Point domain from GoDaddy

**📘 Full deployment guide:** [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 🌐 Deployment

### Recommended: Vercel (FREE)
1. Push code to GitHub
2. Sign up at [vercel.com](https://vercel.com)
3. Import GitHub repository
4. Deploy (automatic)
5. Add domain `thatdeeperfeeling.com`
6. Update GoDaddy DNS

**Detailed steps:** See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 💡 Quick Edits

### Change Colors
Edit [website/app/globals.css](website/app/globals.css) lines 8-18

### Change Fonts
Edit [website/app/globals.css](website/app/globals.css) line 4

### Update Navigation Items
Edit [website/components/layout/Navigation.tsx](website/components/layout/Navigation.tsx) lines 10-18

### Update Footer Links
Edit [website/components/layout/Footer.tsx](website/components/layout/Footer.tsx)

---

## 📚 Documentation

- **[PROJECT_SUMMARY.md](website/PROJECT_SUMMARY.md)** - Technical overview, brand guidelines, file structure
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Complete deployment instructions, integrations, troubleshooting

---

## 🆘 Support

### Common Issues

**Dev server won't start?**
```bash
cd website
rm -rf node_modules
npm install
npm run dev
```

**Build errors?**
```bash
npm run build
# Check terminal for specific errors
```

**Styles not showing?**
- Clear browser cache
- Check CSS variable names in `globals.css`

### Resources
- [Next.js Docs](https://nextjs.org/docs)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Vercel Docs](https://vercel.com/docs)

---

## 🎯 Current Development Status

**Development Server:** Running at http://localhost:3000

**Pages Live:**
- ✅ Homepage - Fully functional
- ✅ About - Fully functional
- ✅ Offerings Hub - Fully functional
- ✅ FAQ - Fully functional

**To Visit:**
```
http://localhost:3000           # Homepage
http://localhost:3000/about     # About
http://localhost:3000/offerings # Offerings
http://localhost:3000/faq       # FAQ
```

---

## 🎨 Design Best Practices Implemented

Based on research of top intimacy coaches:

✅ **Navigation:** Centered, 7 items, mobile-responsive
✅ **Color Psychology:** Burgundy (passionate), Terracotta (warm), Cream (safe)
✅ **Typography:** Serif headlines + sans-serif body for authority + warmth
✅ **Trust Signals:** Trauma-informed language, consent-centered, clear boundaries
✅ **Mobile-First:** Responsive design, touch-friendly buttons
✅ **Accessibility:** Focus states, ARIA labels, semantic HTML
✅ **SEO:** Meta tags, semantic structure, fast loading

---

## 📧 Contact

**Website:** [thatdeeperfeeling.com](https://thatdeeperfeeling.com)
**Coach:** Kimberly Bryant
**Domain Registrar:** GoDaddy

---

**Built with Claude Code • Ready to launch with a few more pages! 🚀**
