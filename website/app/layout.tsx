import type { Metadata } from "next";
import "./globals.css";
import Navigation from "@/components/layout/Navigation";
import Footer from "@/components/layout/Footer";
import PageTransition from "@/components/ui/PageTransition";

export const metadata: Metadata = {
  title: "That Deeper Feeling | Conscious Intimacy Coaching by Kimberly Bryant",
  description: "Transform your relationship with intimacy, power, and pleasure through conscious kink coaching. Individual containers, couples exploration, and sacred group experiences with trauma-informed, consent-centered guidance.",
  keywords: ["intimacy coaching", "conscious kink", "somatic coaching", "trauma-informed", "relationship coaching", "BDSM coaching", "sex-positive coaching"],
  authors: [{ name: "Kimberly Bryant" }],
  openGraph: {
    title: "That Deeper Feeling | Conscious Intimacy Coaching",
    description: "Transform your relationship with intimacy, power, and pleasure through conscious kink coaching.",
    url: "https://www.thatdeeperfeeling.com",
    siteName: "That Deeper Feeling",
    locale: "en_US",
    type: "website",
    images: [
      {
        url: "https://www.thatdeeperfeeling.com/images/kimberly-hero.jpg",
        width: 1200,
        height: 630,
        alt: "Kimberly Bryant — That Deeper Feeling",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "That Deeper Feeling | Conscious Intimacy Coaching",
    description: "Transform your relationship with intimacy, power, and pleasure through conscious kink coaching.",
    images: ["https://www.thatdeeperfeeling.com/images/kimberly-hero.jpg"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Poppins:wght@300;400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>
        <Navigation />
        <main>
          <PageTransition>{children}</PageTransition>
        </main>
        <Footer />
      </body>
    </html>
  );
}
