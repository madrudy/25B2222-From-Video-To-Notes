from youtube_transcript_api import YouTubeTranscriptApi
import json


url = input("Enter the YouTube video URL: ")

if url.startswith("https://youtu.be/"):
    video_ID = url.split("/")[-1]
elif url.startswith("https://www.youtube.com/watch?v="):
    video_ID = url.split("v=")[-1].split("&")[0]
else:
    print("Invalid YouTube URL format.")
    exit()

ytt_api = YouTubeTranscriptApi()

transcript_list = ytt_api.list(video_ID)

segments = None

for transcript in transcript_list:
    if transcript.language_code == 'en':
        segments = transcript.fetch()
        break
if segments is None:
    print("No English transcript available.")
else:
    #merge segments into raw text
    raw_text = ""
    for segment in segments:
        raw_text += segment.text + " "
raw_text = raw_text.strip().replace("\n", " ") #remove line breaks
while "  " in raw_text: #remove double spaces
    raw_text = raw_text.replace("  ", " ")
for punct in [".", ",", "!", "?", ";", ":"]: #remove spaces before punctuations
    raw_text = raw_text.replace(" " + punct, punct + " ")
print(raw_text)

with open("transcript.txt", "w", encoding = "utf-8") as f:
    f.write(raw_text)
json_segments = []
for segment in segments:
    json_segments.append({
        "text":segment.text,
        "start":segment.start,
        "duration":segment.duration
    })
data = {
    "video_id":video_ID,
    "language":"en",
    "transcript":raw_text,
    "segments":json_segments
}
with open("transcript.json", "w", encoding = "utf-8") as f:
    json.dump(data, f, indent = 4, ensure_ascii = False)
print("Transcript saved to transcript.txt and transcript.json")
