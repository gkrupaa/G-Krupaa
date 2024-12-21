"use client";

import { Github, MusicIcon } from "lucide-react";
import { ThemeToggle } from "@/components/theme/ThemeToggle";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export function Header() {
  const scrollToSearch = () => {
    const searchElement = document.getElementById("search-section");
    searchElement?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-14 items-center">
        <div className="mr-4 flex pl-4 sm:pl-6">  {/* Added pl-4 sm:pl-6 */}
          <Link href="/" className="mr-6 flex items-center space-x-2">
            <MusicIcon className="h-6 w-6" />
            <span className="hidden font-bold sm:inline-block">
              Song Recommender
            </span>
          </Link>
        </div>
        <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
          <nav className="flex items-center space-x-2">
            <Button variant="ghost" asChild>
              <a href="https://github.com/ameensalim1/the-greatest-team" target="_blank" rel="noopener noreferrer">
                <Github className="mr-2 h-4 w-4" />
                GitHub
              </a>
            </Button>
            <ThemeToggle />
          </nav>
        </div>
      </div>
    </header>
  );
}