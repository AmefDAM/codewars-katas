# Smart log formatter

**Codewars:** [7 kyu — Smart log formatter](https://www.codewars.com/kata/52fba66badcd10859f00097e)
<br>
**Solution Language:** Python

## Description

You are given a list of log entries from a system. Each log entry has the following format: `"LEVEL message"`, where LEVEL is one of `INFO`, `WARNING`, `ERROR`.

Your task is to compress consecutive identical log entries by adding a repetition counter.
Rules:

    Only consecutive identical entries should be compressed.
    The comparison must be case-sensitive.
    The original log message must be preserved.
    A single occurrence should remain unchanged.
    Repeated entries should be replaced with the entry followed by " (xN)", where N is the number of repetitions.
    The order of the logs must remain unchanged.
    If the input list is empty, return an empty list.

Examples

#### Input
[
"ERROR Disk failure",
"ERROR Disk failure",
"ERROR Disk failure",
"INFO User login"
]

#### Output
[
"ERROR Disk failure (x3)",
"INFO User login"
]

Explanation: The three consecutive `"ERROR Disk failure"` entries are combined into one entry.

#### Input
[
"INFO Connected",
"WARNING Low battery",
"INFO Connected"
]

#### Output
[
"INFO Connected",
"WARNING Low battery",
"INFO Connected"
]

Explanation: Only consecutive identical logs are compressed. The two `INFO` entries are not next to each other, so they remain separate.

## Solution

[smart_log_formatter.py](./smart_log_formatter.py)