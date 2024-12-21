"use client";

import { Github } from "lucide-react";
import { Button } from "@/components/ui/button";

interface HeroSectionProps {
  onGetStarted: () => void;
}

export function HeroSection({ onGetStarted }: HeroSectionProps) {
  return (
    <div className="relative pb-16 pt-24 text-center">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-4xl">
          <h1 className="text-4xl font-bold tracking-tight sm:text-6xl">
            Discover Your Perfect Soundtrack
          </h1>
          <p className="mt-6 text-lg leading-8 text-muted-foreground">
            Tell us your mood, activity, or vibe, and let our AI-powered recommender find the perfect songs for your moment.
          </p>
          <div className="mt-10 flex items-center justify-center gap-x-6">
            <Button size="lg" onClick={onGetStarted}>
              Get Started
            </Button>
            <Button size="lg" variant="outline" asChild>
              <a
                href="https://github.com/ameensalim1/the-greatest-team"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center"
              >
                <Github className="mr-2 h-5 w-5" />
                View on GitHub
              </a>
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}