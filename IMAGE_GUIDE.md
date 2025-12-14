# Image Integration Guide

## 📸 Your Professional Photos (From Attachments)

You've shared 4 beautiful photos of Kimberly. Here's exactly how to add them to the site:

---

## STEP 1: Save Images

Save each photo to the `website/public/images/` folder:

**Photo Recommendations:**

1. **kimberly-hero.jpg**
   - Use: Pink background photo (warm, confident, finger on lips)
   - Purpose: Homepage hero section
   - Feel: Inviting, playful, grounded

2. **kimberly-about-main.jpg**
   - Use: Natural light casual photo (soft, intimate)
   - Purpose: About page primary image
   - Feel: Approachable, human, warm

3. **kimberly-about-secondary.jpg**
   - Use: Burgundy off-shoulder top (grounded, sensual)
   - Purpose: About page secondary or alternate
   - Feel: Sovereign, present, embodied

4. **kimberly-offerings.jpg**
   - Use: Christmas lights background (joyful, present)
   - Purpose: Optional for offerings or testimonials
   - Feel: Celebratory, alive, connected

---

## STEP 2: Add to Website Folder

**Windows:**
1. Download/save the 4 photos from our chat
2. Navigate to: `C:\Users\IndigoVPR\thatdeeperfeeling\website\public\images\`
3. Rename them as suggested above
4. Save all 4 files there

**Folder structure should look like:**
```
website/
  public/
    images/
      kimberly-hero.jpg
      kimberly-about-main.jpg
      kimberly-about-secondary.jpg
      kimberly-offerings.jpg
```

---

## STEP 3: Update Homepage (Add Hero Image)

**File:** `website/app/page.tsx`

**Current code (line ~8-29):**
```tsx
<section className="hero">
  <div className="container">
    <div className="hero-content">
      <h1 className="hero-title">
        Reclaim Your Deepest
        <br />
        <span className="gradient-text">Intimacy & Power</span>
      </h1>
      <p className="hero-subtitle">
        For those no longer willing to abandon themselves...
      </p>
      <div className="hero-cta">
        <Button href="/consult" variant="primary">
          Book Your Consultation
        </Button>
        <Button href="/offerings" variant="secondary">
          Explore Offerings
        </Button>
      </div>
    </div>
  </div>
</section>
```

**Add image like this:**
```tsx
import Image from 'next/image';

<section className="hero">
  <div className="container">
    <div className="hero-layout">
      {/* Left: Text */}
      <div className="hero-content">
        <h1 className="hero-title">
          Reclaim Your Deepest
          <br />
          <span className="gradient-text">Intimacy & Power</span>
        </h1>
        <p className="hero-subtitle">
          For those no longer willing to abandon themselves in the name of belonging, obedience, or approval—and ready to reclaim their body, truth, and power.
        </p>
        <div className="hero-cta">
          <Button href="/consult" variant="primary">
            Book Your Consultation
          </Button>
          <Button href="/offerings" variant="secondary">
            Explore Offerings
          </Button>
        </div>
      </div>

      {/* Right: Image */}
      <div className="hero-image">
        <Image
          src="/images/kimberly-hero.jpg"
          alt="Kimberly Bryant - Intimacy Coach"
          width={500}
          height={600}
          priority
          className="hero-photo"
        />
      </div>
    </div>
  </div>
</section>
```

**Add this CSS to the `<style jsx>` section:**
```css
.hero-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

@media (min-width: 768px) {
  .hero-layout {
    grid-template-columns: 1fr 1fr;
  }
}

.hero-image {
  display: flex;
  justify-content: center;
}

.hero-photo {
  border-radius: 1rem;
  box-shadow: 0 20px 50px rgba(139, 58, 71, 0.3);
  object-fit: cover;
  width: 100%;
  height: auto;
  max-width: 500px;
}
```

---

## STEP 4: Update About Page (Add Photos)

**File:** `website/app/about/page.tsx`

**Current placeholder (line ~44-50):**
```tsx
<div className="story-image">
  <div className="image-placeholder">
    <p>Professional photo of Kimberly Bryant</p>
    <small>(Add your photo here)</small>
  </div>
</div>
```

**Replace with:**
```tsx
import Image from 'next/image';

<div className="story-images">
  <div className="story-image-primary">
    <Image
      src="/images/kimberly-about-main.jpg"
      alt="Kimberly Bryant"
      width={600}
      height={700}
      className="about-photo"
    />
  </div>
  <div className="story-image-secondary">
    <Image
      src="/images/kimberly-about-secondary.jpg"
      alt="Kimberly Bryant - Intimacy Coach"
      width={600}
      height={700}
      className="about-photo"
    />
  </div>
</div>
```

**Update CSS:**
```css
.story-images {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-top: 3rem;
}

@media (min-width: 768px) {
  .story-images {
    grid-template-columns: repeat(2, 1fr);
  }
}

.story-image-primary,
.story-image-secondary {
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(139, 58, 71, 0.2);
}

.about-photo {
  width: 100%;
  height: auto;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.about-photo:hover {
  transform: scale(1.05);
}
```

---

## STEP 5: Optimize Images (Optional but Recommended)

**Why:** Next.js automatically optimizes images, but you can pre-optimize for faster loading.

**Tools:**
- [TinyPNG](https://tinypng.com/) - Free compression
- [Squoosh](https://squoosh.app/) - Google's image optimizer

**Target:**
- File size: < 200KB per image
- Dimensions: 1000-1500px wide (Next.js will resize automatically)
- Format: JPG or WebP

---

## IMAGE SPECIFICATIONS

### Homepage Hero Image
- **Dimensions:** 800x1000px (portrait orientation works best)
- **File Size:** < 250KB
- **Format:** JPG
- **Alt Text:** "Kimberly Bryant - Intimacy Coach specializing in conscious kink and embodied reclamation"

### About Page Images
- **Dimensions:** 600x700px each
- **File Size:** < 200KB each
- **Format:** JPG
- **Alt Text:**
  - Primary: "Kimberly Bryant in a contemplative moment"
  - Secondary: "Kimberly Bryant - Trauma-informed intimacy coach"

---

## FALLBACK: If Images Don't Load

**Check:**
1. File path is correct: `/images/kimberly-hero.jpg` (no typo)
2. Files are in `public/images/` folder
3. File names match exactly (case-sensitive on some systems)
4. Dev server restarted after adding images:
   ```bash
   # Stop server (Ctrl+C)
   npm run dev
   ```

**Browser Console:**
- Right-click page → Inspect → Console
- Look for 404 errors on image paths
- Adjust file names if needed

---

## EXAMPLE: Complete Hero Section with Image

Here's the full hero section code ready to copy/paste:

```tsx
import Image from 'next/image';
import Button from '@/components/ui/Button';

export default function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-layout">
            <div className="hero-content">
              <h1 className="hero-title">
                Reclaim Your Deepest
                <br />
                <span className="gradient-text">Intimacy & Power</span>
              </h1>
              <p className="hero-subtitle">
                For those no longer willing to abandon themselves in the name of belonging, obedience, or approval—and ready to reclaim their body, truth, and power.
              </p>
              <div className="hero-cta">
                <Button href="/consult" variant="primary">
                  Book Your Consultation
                </Button>
                <Button href="/offerings" variant="secondary">
                  Explore Offerings
                </Button>
              </div>
            </div>

            <div className="hero-image">
              <Image
                src="/images/kimberly-hero.jpg"
                alt="Kimberly Bryant - Intimacy Coach"
                width={500}
                height={600}
                priority
                className="hero-photo"
              />
            </div>
          </div>
        </div>
      </section>

      <style jsx>{`
        .hero {
          min-height: 80vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background: linear-gradient(135deg, var(--neutral-cream) 0%, var(--secondary-warm-beige) 100%);
          padding: 4rem 1.5rem;
        }

        .hero-layout {
          display: grid;
          grid-template-columns: 1fr;
          gap: 3rem;
          align-items: center;
          max-width: 1200px;
          margin: 0 auto;
        }

        @media (min-width: 768px) {
          .hero-layout {
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
          }
        }

        .hero-content {
          max-width: 600px;
        }

        .hero-title {
          font-size: clamp(2.5rem, 6vw, 5rem);
          margin-bottom: 1.5rem;
          line-height: 1.1;
        }

        .gradient-text {
          background: linear-gradient(135deg, var(--primary-burgundy) 0%, var(--accent-terracotta) 100%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
        }

        .hero-subtitle {
          font-size: clamp(1.1rem, 2vw, 1.35rem);
          color: var(--neutral-warm-gray);
          margin-bottom: 2.5rem;
          line-height: 1.7;
        }

        .hero-cta {
          display: flex;
          gap: 1rem;
          flex-wrap: wrap;
        }

        .hero-image {
          display: flex;
          justify-content: center;
        }

        :global(.hero-photo) {
          border-radius: 1rem;
          box-shadow: 0 20px 50px rgba(139, 58, 71, 0.3);
          object-fit: cover;
          width: 100%;
          height: auto;
          max-width: 500px;
        }
      `}</style>
    </>
  );
}
```

---

## QUICK CHECKLIST

Before testing:
- [ ] All 4 photos saved to `public/images/`
- [ ] Files renamed correctly
- [ ] `Image` component imported from `next/image`
- [ ] Alt text added (accessibility)
- [ ] CSS updated for layout
- [ ] Dev server restarted

After adding:
- [ ] Images display on homepage
- [ ] Images display on about page
- [ ] Images look good on mobile (resize browser)
- [ ] No console errors in browser

---

## 🎉 RESULT

Once images are added, your site will have:
- ✅ Professional photography of Kimberly
- ✅ Warm, inviting visual presence
- ✅ Trust-building through human connection
- ✅ Optimized, fast-loading images
- ✅ Accessible alt text for screen readers

**The site will feel complete, professional, and ready to launch! 🔥**
