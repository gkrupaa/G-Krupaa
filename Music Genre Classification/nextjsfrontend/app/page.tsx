"use client";

import { useState } from "react";
import axios from "axios";
import { SearchForm } from "@/components/recommender/SearchForm";
import { SongList } from "@/components/recommender/SongList";
import { useToast } from "@/components/ui/use-toast";
import { HeroSection } from "@/components/recommender/HeroSection";
import { MoodSelector } from "@/components/recommender/MoodSelector";

interface Song {
  artist_name: string;
  track_name: string;
}

export default function Home() {
  const [songs, setSongs] = useState<Song[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const { toast } = useToast();

  const handleSubmit = async (query: string) => {
    setIsLoading(true);
    try {
      // Use the backend URL from environment variables
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/recommend-by-genre`,
        { query }
      );
      setSongs(response.data.recommendations);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to get recommendations. Please try again.",
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  const scrollToSearch = () => {
    const searchElement = document.getElementById("search-section");
    searchElement?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div>
      <HeroSection onGetStarted={scrollToSearch} />
      <div id="search-section" className="container mx-auto max-w-4xl py-8 px-4">
        <div className="flex flex-col items-center space-y-8">
          <MoodSelector onMoodSelect={handleSubmit} />
          <div className="flex flex-col items-center space-y-8 w-full">
            <SearchForm onSubmit={handleSubmit} isLoading={isLoading} />
            <SongList songs={songs} />
          </div>
        </div>
      </div>
    </div>
  );
}