import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Script generated with AI assistance

def fetch_youtube_transcript(video_id, file_name):
    try:
        print(f"Fetching transcript for video ID: {video_id}...")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        text_formatted = formatter.format_transcript(transcript)

        output_path = f"research/youtube-transcripts/{file_name}.txt"
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text_formatted)

        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    videos_to_scrape = [
        {"id": "q1a2b3c4d5e", "name": "gael-breton-ai-helpful-content-test"},
        {"id": "z9y8x7w6v5u", "name": "matt-diggity-ai-seo-blueprint"}
    ]

    os.makedirs("research/youtube-transcripts", exist_ok=True)

    for video in videos_to_scrape:
        fetch_youtube_transcript(video["id"], video["name"])