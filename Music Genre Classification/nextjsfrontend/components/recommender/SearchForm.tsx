"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Card } from "@/components/ui/card";

interface SearchFormProps {
  onSubmit: (query: string) => void;
  isLoading: boolean;
}

export function SearchForm({ onSubmit, isLoading }: SearchFormProps) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      onSubmit(query);
    }
  };

  return (
    <Card className="w-full max-w-2xl p-6">
      <form onSubmit={handleSubmit} className="space-y-4">
        <Textarea
          placeholder="Describe the type of music you're looking for... (e.g., 'I want upbeat acoustic songs for working out')"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="min-h-[100px] resize-none"
        />
        <Button type="submit" className="w-full" disabled={isLoading}>
          {isLoading ? "Finding songs..." : "Get Recommendations"}
        </Button>
      </form>
    </Card>
  );
}