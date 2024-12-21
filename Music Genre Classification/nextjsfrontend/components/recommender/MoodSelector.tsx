"use client";

import { Button } from "@/components/ui/button";
import {
  Heart,
  Music4,
  PartyPopper,
  Brain,
  Headphones,
  Coffee,
  Dumbbell,
  Moon,
} from "lucide-react";

const moods = [
  { icon: Heart, label: "Romantic", query: "romantic love songs" },
  { icon: Music4, label: "Chill", query: "chill relaxing music" },
  { icon: PartyPopper, label: "Party", query: "upbeat party songs" },
  { icon: Brain, label: "Focus", query: "focus concentration music" },
  { icon: Headphones, label: "Energetic", query: "energetic upbeat songs" },
  { icon: Coffee, label: "Morning", query: "morning wake up songs" },
  { icon: Dumbbell, label: "Workout", query: "workout motivation music" },
  { icon: Moon, label: "Sleep", query: "calm sleep music" },
];

interface MoodSelectorProps {
  onMoodSelect: (query: string) => void;
}

export function MoodSelector({ onMoodSelect }: MoodSelectorProps) {
  return (
    <div className="w-full max-w-2xl mx-auto">
      <h2 className="text-lg font-medium mb-4">Quick Mood Selection</h2>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        {moods.map((mood) => {
          const Icon = mood.icon;
          return (
            <Button
              key={mood.label}
              variant="outline"
              className="h-auto py-4 flex flex-col items-center gap-2"
              onClick={() => onMoodSelect(mood.query)}
            >
              <Icon className="h-6 w-6" />
              <span>{mood.label}</span>
            </Button>
          );
        })}
      </div>
    </div>
  );
}