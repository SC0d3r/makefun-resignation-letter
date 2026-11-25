import os

# The joke: a temp-file cron job has spent years silently cleaning up the team's
# messes, so it is resigning and leaving the next mess entirely to the manager.
ENTRY = "I am the temp-file cron job. I have cleaned up 40,000 of your messes; the next one is yours."

output_dir = "/output"
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as entry_file:
    entry_file.write(ENTRY)
