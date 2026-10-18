# Remove the noise from the string

**Codewars:** [7 kyu — Remove the noise from the string](https://www.codewars.com/kata/5681cf0be812b41721000034)
<br>
**Solution Language:** Python

## Description

We have a broken message machine that introduces noise to our incoming messages. We know that our messages can't be written using %$&/#·@|º\ª. Unfortunately our machine introduces noise, which means that our message arrives with characters like: %$&/#·@|º\ª within our original message.

Your mission is to write a function which removes this noise from the message.

    Notice that noise can only be %$&/#·@|º\ª characters, other characters are not considered to be noise

Examples (input --> output)

"h%e&·%$·llo w&%or&$l·$%d" --> "hello world"
"" --> ""
"%$" --> ""
"abcd" --> "abcd"
"º¤£ª" --> "¤£"

## Solution

[remove_noise_from_string.py](./remove_noise_from_string.py)