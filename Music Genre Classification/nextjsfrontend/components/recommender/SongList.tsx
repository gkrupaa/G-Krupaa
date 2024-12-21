import { Card } from "@/components/ui/card";
import { Music2Icon } from "lucide-react";

interface Song {
  artist_name: string;
  track_name: string;
}

interface SongListProps {
  songs: Song[];
}

export function SongList({ songs }: SongListProps) {
  if (!songs) return null;

  return (
    <Card className="w-full max-w-2xl p-6">
      <h2 className="mb-4 text-2xl font-bold">Recommended Songs</h2>
      <div className="space-y-4">
        {songs.map((song, index) => (
          <div
            key={index}
            className="flex items-center space-x-4 rounded-lg border p-4 transition-colors hover:bg-muted/50"
          >
            <Music2Icon className="h-8 w-8 flex-shrink-0 text-primary" />
            <div>
              <h3 className="font-semibold">{song.track_name}</h3>
              <p className="text-sm text-muted-foreground">{song.artist_name}</p>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
}