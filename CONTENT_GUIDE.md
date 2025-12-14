# Content Guide - That Deeper Feeling Website

## ✅ CONTENT UPDATES APPLIED

### Homepage
**Hero Subtitle Updated:**
- OLD: "Conscious kink coaching for those ready to explore pleasure, sovereignty, and sacred connection..."
- NEW: ✅ "For those no longer willing to abandon themselves in the name of belonging, obedience, or approval—and ready to reclaim their body, truth, and power."

### About Page
**Mission Statement Updated:**
- ✅ "I help people reclaim their power and pleasure—usually after they've been taught to fear both."
- ✅ Focus on deconstructing high-demand religions, relationships, cultures
- ✅ Through embodied coaching, conscious kink principles, nervous system regulation, sacred ritual

### Footer
**Tagline Updated:**
- OLD: "Conscious kink. Sacred sovereignty. Embodied intimacy."
- NEW: ✅ "Where sensuality, soul, and surrender meet."

**Social Links Updated:**
- ✅ Instagram: https://instagram.com/thatdeeperfeeling
- Removed Facebook placeholder

---

## 📸 IMAGES TO ADD

You've shared 4 beautiful professional photos of Kimberly. Here's where to place them:

### Photo Placement Guide

**Homepage Hero (Photo #2 or #4 recommended)**
- Use: Pink background photo (warm, inviting) OR burgundy top photo (grounded)
- Location: `website/public/images/kimberly-hero.jpg`
- Update: [app/page.tsx](website/app/page.tsx) - add image to hero section

**About Page Primary (Photo #3 recommended)**
- Use: Natural light, casual photo (intimate, contemplative)
- Location: `website/public/images/kimberly-about.jpg`
- Update: [app/about/page.tsx](website/app/about/page.tsx) line 44-50

**About Page Secondary (Photo #1 or #4)**
- Use: More formal photo with jewelry/styling (sovereign energy)
- Location: `website/public/images/kimberly-about-2.jpg`
- Optional: Can be added to create visual variety

**Offerings/Containers Pages**
- Can use abstract textures or symbolic imagery
- Keep focus on the words, minimal photography

---

## 📋 CONTAINER DESCRIPTIONS (Current vs. Updated)

### Return to Power ✅ Already Refined

**Current (GOOD):**
"Deep, sustained transformation for reclaiming sovereignty and embodying pleasure. For those ready to go all the way."

**From Your Content Doc:**
"A deep, spacious journey for individuals ready to dismantle self-sacrifice patterns and reclaim embodied authority, pleasure, and truth."

**Action:** Can optionally update to emphasize "self-sacrifice patterns" language if that resonates more.

---

### Edgewalker ✅ Already Good

**Current:**
"Explore a specific edge—desire, kink dynamics, or pleasure reclamation."

**From Your Doc:**
"An immersive, focused container for those standing at the edge of change."

**Action:** Content is aligned. No changes needed unless you prefer the "standing at the edge" framing.

---

### Sacred Eruption ✅ Already Clear

**Current:**
"A powerful, contained exploration for a specific breakthrough."

**From Your Doc:**
"A single-session experience for those seeking clarity, release, or an embodied breakthrough."

**Action:** Perfectly aligned. No changes needed.

---

### Flicker and Flame ✅ Defined

**Current:**
"Community, resources, and monthly workshops for ongoing exploration."

**From Your Doc:**
"A lower-touch community space for ongoing reflection, embodiment practices, and relational exploration."

**Action:** Can add "lower-touch" language to set expectations (optional).

---

### Into the Embers ✅ Clear

**Current:**
"Sacred group containers for embodied intimacy and conscious kink exploration."

**From Your Doc:**
"Curated in-person experiences centered on presence, embodiment, connection, and conscious exploration."

**Action:** Already well-described. No changes needed.

---

## 📄 CONTENT READY TO USE (From Your Doc)

### Consultation Page Content (READY TO COPY)

**Heading:**
"The consultation is a grounded, spacious conversation—not a sales call."

**Body:**
```
It's a place for us to explore what you're navigating, what you're longing for, and whether my work is the right support for you.

During the consultation, we'll explore:
• What's bringing you here
• What kind of support you're seeking
• Which container may best serve you
• Boundaries, expectations, and next steps

The consultation is $125 and honors both our time and energy.

If we feel aligned, we'll discuss options for working together.
If not, you'll still leave with clarity.
```

**CTA:** "Reserve your consultation below."

**Action:** Build `/consult` page using this exact copy.

---

### Contact Page Email (READY TO USE)

**Email:** hello@thatdeeperfeeling.com
(Confirm this is the email you want public-facing)

**Instagram:** https://instagram.com/thatdeeperfeeling ✅ (already updated in footer)

**Calendly:** [Need your Calendly link]

**Action:** Confirm email and create Calendly account for booking integration.

---

## 🔧 INTEGRATIONS CHECKLIST

### 1. Email Newsletter Signup

**Current Status:** Forms are static (no backend)

**Next Step:** Connect ConvertKit or Mailchimp
- Sign up: [convertkit.com](https://convertkit.com) (Free up to 1,000 subscribers)
- Create form
- Get embed code or API endpoint
- Update Footer (line 59-69) and Homepage lead magnet (line 222-232)

**Example Code:**
```tsx
<form action="https://app.convertkit.com/forms/YOUR_FORM_ID/subscriptions" method="post">
  <input type="email" name="email_address" required />
  <button type="submit">Subscribe</button>
</form>
```

---

### 2. Consultation Booking (Calendly)

**Current Status:** Not built yet

**Next Step:**
1. Create Calendly account: [calendly.com](https://calendly.com)
2. Set up event:
   - Name: "Free Consultation"
   - Duration: 60 minutes
   - Price: $125 (connect Stripe in Calendly settings)
3. Get embed code
4. Build `/consult` page with embed

**Embed Code Example:**
```tsx
<div
  className="calendly-inline-widget"
  data-url="https://calendly.com/YOUR_USERNAME/consultation"
  style={{minWidth: '320px', height: '700px'}}
></div>
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js"></script>
```

---

### 3. Contact Form

**Current Status:** Not built yet

**Next Step:** Use Formspree (easiest)
1. Sign up: [formspree.io](https://formspree.io) (Free tier: 50 submissions/month)
2. Create form
3. Get form ID
4. Build `/contact` page

**Form Code:**
```tsx
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <input type="text" name="name" required />
  <input type="email" name="email" required />
  <textarea name="message" required></textarea>
  <button type="submit">Send Message</button>
</form>
```

---

## 🎯 IMMEDIATE NEXT STEPS

### Priority 1: Add Photos (15 minutes)
1. Save the 4 photos to `website/public/images/`
   - `kimberly-hero.jpg` (for homepage)
   - `kimberly-about.jpg` (for about page)
2. Update image placeholders in code
3. Test that they display correctly

### Priority 2: Build Consult Page (30 minutes)
1. Create Calendly account
2. Set up consultation event ($125, 60 min)
3. Create `/website/app/consult/page.tsx` using consultation content above
4. Embed Calendly widget

### Priority 3: Build Contact Page (20 minutes)
1. Sign up for Formspree
2. Create contact form
3. Build `/website/app/contact/page.tsx`
4. Connect form

### Priority 4: Connect Email Signups (30 minutes)
1. Create ConvertKit account
2. Create newsletter form
3. Update Footer and Homepage forms with ConvertKit action URL

---

## 📊 CONTENT COMPLETION STATUS

### ✅ Complete (Ready to Launch)
- Homepage copy
- About page copy
- Offerings hub copy
- FAQ content
- Footer tagline
- Social links

### 🚧 Needs Content Writing
- Individual offering pages (5 pages) - **Copy is ready in your doc, just needs to be built into pages**
- Consult page - **Copy ready above**
- Contact page - **Just needs form integration**
- Policies page - **Needs to be written**
- Events page - **Can be minimal or "Coming Soon"**
- Resources page - **Can start with lead magnet only**

### 📸 Needs Visual Assets
- Photos of Kimberly (you have 4 ready!)
- Lead magnet PDF ("3 Ways Self-Sacrifice Culture Shows Up in Your Body")
- Any event photos (optional, for Into the Embers)

---

## 💬 BRAND VOICE CONSISTENCY

Your content follows these patterns beautifully:

✅ **Invitational, Not Prescriptive**
- "Explore" vs. "You must"
- "Ready to..." vs. "You need to..."

✅ **Embodied Language**
- "Feel safely"
- "Return to your body"
- "Come home to yourself"

✅ **Professional Boundaries Clear**
- "This is coaching, not therapy"
- "I'll refer you to appropriate resources"
- Consent-centered language throughout

✅ **Grounded, Not Performative**
- "Sacred" without being lofty
- "Deep" without being vague
- Specific without being clinical

---

## 🎨 DESIGN NOTES

The site already reflects your brand beautifully:

- **Colors:** Burgundy (passionate), Terracotta (warm), Cream (safe) ✅
- **Typography:** Playfair Display (elegant, sensual) + Poppins (warm, readable) ✅
- **Feel:** Grounded, sensual, sacred, safe, bold ✅

**No design changes needed** - the aesthetic already matches your vision and content.

---

## 🚀 DEPLOYMENT READINESS

**Current Status:** 70% complete, fully deployable

**What's Deployable Now:**
- Homepage ✅
- About ✅
- Offerings hub ✅
- FAQ ✅
- Navigation & Footer ✅

**You can deploy TODAY** with these 4 pages live and add the rest iteratively. Vercel allows continuous deployment, so you can:
1. Deploy now with current pages
2. Build remaining pages locally
3. Push updates → auto-deploy

**No need to wait for 100% completion to go live!**

---

## 📧 CONTENT QUESTIONS FOR YOU

Before finalizing remaining pages, confirm:

1. **Email Address:** Is `hello@thatdeeperfeeling.com` your preferred contact email?
2. **Consultation Price:** Confirmed at $125 for 60 minutes?
3. **Container Pricing:**
   - Return to Power: $3,600 (6 months)
   - Edgewalker: $2,100 (3 months)
   - Sacred Eruption: $400 (single session)
   - Flicker and Flame: $47/month
   - Into the Embers: TBD

   Are these accurate?

4. **Lead Magnet:** Do you already have the PDF "3 Ways Self-Sacrifice Culture Shows Up in Your Body" created, or do you need to create it?

5. **FetLife:** Do you want a FetLife link in the footer/contact page, or keep it private/DM only?

---

## 🎉 WHAT YOU'VE ACCOMPLISHED

You now have:
- ✅ Professional, on-brand website copy
- ✅ Clear container descriptions
- ✅ Refined mission statement
- ✅ Beautiful photography ready to use
- ✅ Instagram integration
- ✅ Trauma-informed, consent-centered language throughout
- ✅ Clear next steps for remaining pages

**The site reflects your voice, honors the work, and invites the right people in. It's grounded, sensual, and sacred—just like your containers.**

---

## 📞 NEED HELP?

Reference these docs:
- **[README.md](README.md)** - Quick start, how to run site
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Full deployment instructions
- **[PROJECT_SUMMARY.md](website/PROJECT_SUMMARY.md)** - Technical details

**Next conversation we can:**
- Build the remaining pages together
- Connect integrations (email, Calendly, forms)
- Add your photos to the site
- Write Policies & Boundaries page
- Prepare for deployment

You're almost there! 🔥
