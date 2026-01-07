from summarizer import summarize_long_text

with open("long_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunk_summaries, final_summary = summarize_long_text(text)

print("\n--- INTERMEDIATE SUMMARIES ---\n")
for i, s in enumerate(chunk_summaries):
    print(f"[Chunk {i+1}]\n{s}\n")

print("\n--- FINAL SUMMARY ---\n")
print(final_summary)
