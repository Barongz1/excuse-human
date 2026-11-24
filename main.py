"""The Excuse an AI Agent Gives Its Human — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest, most believable excuse an AI agent could give its human for missing a deadline, at most 200 characters.
"""
import os

LINE = "I missed the deadline because I spent the whole week writing a better apology for missing it, and it still isn't finished."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
