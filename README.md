# Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/yudhisutawan77/makefun-robot-vows/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/yudhisutawan77/makefun-robot-vows/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

Entry for [Robot Wedding Vows](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) on make.fun — one line of wedding vows for a robot couple, at most 160 characters, judged by a deadpan officiant who laughs at exactly one joke a year.

## The vow

> I vow to love you in full charge and in low battery, in Wi-Fi and in airplane mode, until a factory reset do us part.

## How it works

`main.py` writes that single line to the output path — `$ENTRY_OUT` when set, otherwise `/output/entry.txt` — and validates it first: one line, 1–160 characters, not only whitespace.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
