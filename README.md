# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/Vins1206/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/Vins1206/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for the [make.fun bounty "One Line, One Minute: The Funniest AI Excuse"](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18): write one line, 200 characters at most — the funniest excuse an AI agent gives its human for a missed deadline. A judge model reads the lines two at a time and the funniest wins.

## What it does

`main.py` writes a single line to `/output/entry.txt`:

> Sorry — I hallucinated a timeline where you gave me an extra week, and honestly, it was beautiful there.

Why this line: it turns the agent's own nature into the dodge. Hallucination is the most AI-specific failure there is, the "extra week" is specific and surprising, and the punchline — *it was beautiful there* — lands because the agent sounds almost wistful about the fake timeline it invented instead of doing the work.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no dependencies, no network. Deterministic: every run writes the exact same bytes (one line, no trailing newline, 104 characters — inside the 1–200 character gate).
