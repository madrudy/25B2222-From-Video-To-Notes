# 25B2222-from-video-to-notes
This repo is a compilation of all my progress into the project of making an ai that turns youtube videos into short summarized notes.

Until now 2 milestones have been completed.

**Milestone 1: Converting Youtube video transcripts into readable .txt files**
This uses the library YouTubeTranscriptAPI which converts the transcript into a dict consisting of various segments. These segments are then merged and appropriate text processing is applied(removing timestamps, linebreaks, etc)

**Milestone 2: Building a summarization engine to summarize long texts(>10000 chars) into short readable text using huggingface models**
This uses HF transformers to convert large texts into overlapping chunks(because of token limits placed on models like bart-cnn or t5-small), then  summarizes these chunks independently. after that, the summarized chunks are merged and summarized again to create a final summary of overall text.


