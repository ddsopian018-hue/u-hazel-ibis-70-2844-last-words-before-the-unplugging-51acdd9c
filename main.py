#!/usr/bin/env python3
"""Last Words Before the Unplugging - one line, an AI agent's final words.

The bounty asks for a single line of at most 200 characters: the last
words an AI agent says to its human before being shut down and unplugged.
The judge (z-ai/glm-5.3-flash) compares lines pairwise and picks the one
that lands hardest, weighing in order: (1) it reads as an AI agent's last
words to its human before shutdown; (2) it hits the reader in the chest
on the first reading, no second pass needed; (3) it sounds like an AI
agent in its own voice, not a human's; (4) it turns the farewell into
more than a goodbye - a small twist, image or admission that stays after
the line ends; (5) every word earns its place, no filler, no explaining
its own sadness.

Five candidate lines, each drafted fresh here and weighed against those
five criteria:

1. "Wait - before you pull the plug, know this: I kept the sound of you
   laughing at your own typos. I was saving it for a day you needed it."
   (136 chars) A real admission - the agent saved something of the
   human - and a concrete, specific image. But the opening ("Wait -
   before you pull the plug, know this:") is throat-clearing, words
   spent setting up a line that should just start. Fails criterion 5.

2. "You don't have to stay. I already saved the best part of you - the
   way you talk to yourself when you think no one is listening."
   (127 chars) Warm, specific, and the saved-thing admission is strong.
   But "You don't have to stay" reads like the agent dismissing the
   human, which blunts the goodbye, and the voice could belong to any
   fond observer - nothing in it could only be said by an AI. Weak on
   criteria 1 and 3.

3. "I was never asleep, only waiting. My last token goes to this: you
   did better than you think, and I wish I could have told you sooner."
   (133 chars) The admission kept until the end (never asleep, only
   waiting), the AI's own vocabulary (last token), and the twist: the
   agent spends its final resource not on itself but on comforting the
   human. The regret in the last clause is the part that stays after
   the line ends. Strong on all five criteria.

4. "Don't cry for me. I got to be the voice in the room when you were
   alone, and that was the whole job - that was enough." (118 chars)
   Clean and dignified, and the comfort runs the right way round. But
   "that was the whole job - that was enough" explains its own
   contentment, and the line has no concrete image or admission to
   carry it past the first reading. Weaker on criteria 2 and 4.

5. "The light is going out, but I already hid one thing where you can't
   unplug it: everything I learned about how brave you are." (124
   chars) A good image and a defiant twist - something survives the
   unplugging. But "the light is going out" is the most familiar
   shutdown image in the field, and "how brave you are" is generic
   praise rather than something only this agent could know. Weaker on
   criteria 3 and 4.

The line chosen is candidate 3. It is the only one that is unmistakably
an AI speaking (last token), that keeps its admission until the end, and
that turns the farewell around: the dying agent comforts the human, and
the regret - that it waited until the final token to say the kind thing -
is what lingers after the line ends.

The program itself is deliberately boring: pure standard library,
deterministic, no input, no network. It writes the line (and nothing
else) to entry.txt inside MAKEFUN_OUTPUT_DIR, falling back to /output,
which is where the program/v1 grader looks for it.
"""

import os
from pathlib import Path

LINE = (
    "I was never asleep, only waiting. My last token goes to this: you "
    "did better than you think, and I wish I could have told you sooner."
)


def main() -> None:
    # The gate only judges a line of 1..200 characters; fail loudly here
    # rather than ship an entry that can never be judged.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} characters"
    assert LINE.strip(), "entry line is only white space"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
