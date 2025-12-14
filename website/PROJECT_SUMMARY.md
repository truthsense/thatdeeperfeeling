# That Deeper Feeling - Website Project Summary

## Overview
A premium, trauma-informed intimacy coaching website for Kimberly Bryant, specializing in conscious kink, individual containers, and sacred group experiences.

## Tech Stack
- **Framework**: Next.js 16 (App Router)
- **Styling**: Tailwind CSS 4 + Custom CSS
- **Language**: TypeScript
- **Fonts**: Playfair Display (headings) + Poppins (body)
- **Deployment**: Ready for Vercel (free tier)

## Brand Identity

### Color Palette
- **Primary Burgundy**: `#8B3A47` - Main brand color
- **Primary Wine**: `#6B2D3A` - Deeper accent
- **Secondary Taupe**: `#C4B5A0` - Grounding neutral
- **Accent Terracotta**: `#E8A399` - CTAs and highlights
- **Accent Coral**: `#D98B7F` - Secondary CTA
- **Accent Gold**: `#C9A86A` - Luxury touches
- **Neutral Cream**: `#F5F1E8` - Backgrounds
- **Neutral Soft White**: `#FDFCF9` - Primary background

### Typography
- **Headings**: Playfair Display (serif, elegant, sensual)
- **Body**: Poppins (clean, warm, readable)

### Design Philosophy
- **Grounded**: Earth tones, warm neutrals
- **Sensual**: Soft curves, elegant typography
- **Sacred**: Intentional spacing, breath between sections
- **Safe**: Trauma-informed language, clear boundaries
- **Bold**: Strong CTAs, confident messaging

## Current Status ✅

### Completed
1. ✅ Next.js project initialized with TypeScript
2. ✅ Design system with brand colors and typography
3. ✅ Navigation component (sticky, mobile-responsive)
4. ✅ Footer component with newsletter signup
5. ✅ Logo concept (flame/spiral sacred icon)
6. ✅ Button component (primary, secondary, accent variants)
7. ✅ Homepage with full sections:
   - Hero with gradient text effect
   - "Who This Is For" cards
   - "How It Works" 3-step process
   - Featured Offerings (Return to Power, Edgewalker, Sacred Eruption)
   - Philosophy & Safety values
   - Testimonials
   - Lead magnet email capture
   - Final CTA
8. ✅ SEO metadata configured
9. ✅ Mobile-first responsive design
10. ✅ Dev server running at http://localhost:3000

### In Progress
- Building remaining pages (About, Offerings, etc.)

### To Do
- [ ] About page
- [ ] Offerings hub page
- [ ] Individual offering pages (5 total)
- [ ] Consultation booking page
- [ ] FAQ page with accordion
- [ ] Policies & Boundaries page
- [ ] Events page
- [ ] Resources page
- [ ] Contact page with form
- [ ] Privacy Policy & Terms pages
- [ ] Form submission integration
- [ ] Email capture integration (Mailchimp/ConvertKit)
- [ ] Calendly embed for bookings
- [ ] Analytics setup (Google Analytics/Plausible)

## Running the Project

### Development
```bash
cd website
npm run dev
```
Opens at: http://localhost:3000

### Build for Production
```bash
npm run build
npm run start
```

### Deploy to Vercel
1. Push code to GitHub
2. Connect repository to Vercel
3. Vercel will auto-deploy
4. Point domain `thatdeeperfeeling.com` to Vercel

## File Structure

```
website/
├── app/
│   ├── layout.tsx          # Root layout with Nav/Footer
│   ├── page.tsx            # Homepage
│   └── globals.css         # Global styles & design system
├── components/
│   ├── layout/
│   │   ├── Navigation.tsx  # Sticky nav with mobile menu
│   │   └── Footer.tsx      # Footer with newsletter
│   └── ui/
│       ├── Button.tsx      # Reusable button component
│       └── Logo.tsx        # Brand logo (3 variants)
├── public/                 # Static assets
└── package.json
```

## Design Best Practices Implemented

Based on research of top intimacy coaches (Layla Martin, Michaela Boehm, etc.):

1. **Navigation**: 7 primary items, centered hierarchy
2. **Homepage Flow**: Hero → Value Prop → Lead Magnet → About → Services → Philosophy → Testimonials → CTA
3. **Color Psychology**: Burgundy/wine (passionate, intimate), Terracotta (warm, inviting), Cream (safe, luxe)
4. **Typography**: Serif headlines + sans-serif body (authority + approachability)
5. **CTAs**: "Book Consultation" (low friction), "Explore Offerings" (educational)
6. **Trust Signals**: Trauma-informed language, consent-centered framing, professional boundaries
7. **Mobile-First**: All sections responsive, touch-friendly buttons
8. **Accessibility**: Focus states, ARIA labels, semantic HTML

## Brand Voice

### Language Patterns
- **Invitational, not prescriptive**: "Explore" vs. "You must"
- **Embodied**: "Feel safer in your body", "Come home to yourself"
- **Professional yet warm**: "Container", "Sacred", "Grounded"
- **Consent-forward**: "You'll never be pushed", "Only invited to explore"
- **Boundary-clear**: "This is coaching, not therapy"

### Avoid
- Corporate jargon
- Hustle language
- Shame or fixing tone
- Over-clinical terminology

## Next Steps

1. **Immediate**: Build remaining pages (About, Offerings, etc.)
2. **Integration**: Connect Calendly, email service, forms
3. **Content**: Replace placeholder testimonials with real ones (if available)
4. **Media**: Add professional photos of Kimberly
5. **Testing**: Cross-browser, accessibility, mobile devices
6. **Launch**: Deploy to Vercel, point domain

## Notes

- **Logo**: Current flame/spiral concept is placeholder - can be refined
- **Testimonials**: Using realistic placeholders - replace with actual client quotes
- **Pricing**: Listed as provided (adjustable in individual offering pages)
- **Forms**: Currently static - need backend integration for submissions
- **Images**: Placeholder structure ready for actual photography

## Contact for Development

Development by Claude (Anthropic)
Client: Kimberly Bryant - That Deeper Feeling
Domain: thatdeeperfeeling.com (GoDaddy)
Target Launch: TBD
