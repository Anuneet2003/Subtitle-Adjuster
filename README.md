# Subtitle Adjuster

`Subtitle Adjuster` is a Python script that modifies subtitle timing in `.srt` files by adding or subtracting a specified time difference.

## Features
- Adjust subtitle timestamps by a custom time difference.
- Prevents negative timestamps by clamping to `00:00:00,000`.

## Input Example (input.srt)
- Here's an example of what your input file might look like:
```
1
00:00:02,500 --> 00:00:03,000
Hello, world!

2
00:00:05,000 --> 00:00:07,000
This is an example subtitle file.
```

## Output Example (output.srt)
- After applying a diff of 2 seconds, the output will look like:
```
1
00:00:00,500 --> 00:00:01,000
Hello, world!

2
00:00:03,000 --> 00:00:05,000
This is an example subtitle file.
If the diff results in negative timestamps, they will be clamped to 00:00:00,000. For example, if the diff was 5 seconds instead:
```

## Requirements
- Python 3.6 or later

## Installation
Clone this repository using the following command:
```bash
git clone https://github.com/your-username/subtitle-adjuster.git
