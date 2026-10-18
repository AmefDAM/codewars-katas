# Keyword cipher

**Codewars:** [6 kyu — Keyword cipher](https://www.codewars.com/kata/57241cafef90082e270012d8)
<br>
**Solution Language:** Python

## Description

Third day at your new cryptoanalyst job and you come across your toughest assignment yet. Your job is to implement a simple keyword cipher. A keyword cipher is a type of monoalphabetic substitution where two parameters are provided as such (string, keyword). The string is encrypted by taking the keyword, dropping any letters that appear more than once. The rest of the letters of the alphabet that aren't used are then appended to the end of the keyword.

For example, if your string was "hello" and your keyword was "wednesday", your encryption key would be "wednsaybcfghijklmopqrtuvxz".

To encrypt "hello" you'd substitute as follows:

              abcdefghijklmnopqrstuvwxyz
  hello ==>   |||||||||||||||||||||||||| ==> bshhk
              wednsaybcfghijklmopqrtuvxz

"hello" encrypts into "bshhk" with the keyword "wednesday".

    If there are uppercase letters in the string, convert them to lowercase before encrypting them.
    If there are non-alphabetic characters in the string, leave them as-is in the result.
    The keyword will entirely consist of lowercase letters.

## Solution

[keyword_cipher.py](./keyword_cipher.py)