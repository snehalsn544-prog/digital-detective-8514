# Mission 5 — Numbers and Data

**Goal:** understand decimal, binary and hexadecimal numbers, bits and bytes, character encoding, and test the number converter in this folder.

## 1. Number systems

A number system uses a base (radix). Each position represents a power of that base.

| System | Base | Digits used | Example |
|---|---:|---|---|
| Decimal | 10 | 0–9 | 25 |
| Binary | 2 | 0–1 | 11001 |
| Hexadecimal | 16 | 0–9 and A–F | 19 |

In hexadecimal, A=10, B=11, C=12, D=13, E=14 and F=15.

## 2. Convert binary to decimal

Binary `1101` means:

```text
1×2³ + 1×2² + 0×2¹ + 1×2⁰
= 8 + 4 + 0 + 1
= 13
```

So `1101₂ = 13₁₀`.

## 3. Convert decimal to binary

Repeatedly divide by 2 and record each remainder. Read the remainders from bottom to top.

Example for 13:

```text
13 ÷ 2 = 6 remainder 1
 6 ÷ 2 = 3 remainder 0
 3 ÷ 2 = 1 remainder 1
 1 ÷ 2 = 0 remainder 1

Read upward: 1101
```

Therefore, `13₁₀ = 1101₂`.

## 4. Hexadecimal example

`2F₁₆ = 2×16 + 15 = 47₁₀`.

Hexadecimal is compact: one hexadecimal digit represents four binary bits. For example, `F₁₆ = 1111₂`.

## 5. Bits and bytes

- A **bit** is one binary digit: 0 or 1.
- A **byte** is 8 bits.
- A byte can represent 256 different patterns (from `00000000` through `11111111`).
- Storage units such as KB, MB and GB describe larger quantities of data. In many contexts, 1 byte = 8 bits; decimal and binary storage-unit conventions can differ.

## 6. Character encoding

Computers store text as numbers. A character encoding defines how text characters are represented as bytes.
- ASCII represents a limited set of English letters, digits and symbols.
- UTF-8 is a widely used Unicode encoding that can represent characters from many writing systems.
- The same text must be decoded using a compatible encoding to display correctly.

## 7. Run the number converter

From the repository root:

```bash
python3 mission-05-numbers-data/number_converter.py
```

If your system uses `python`, that may work instead. Follow the prompts shown by the script. Try several small non-negative integers and compare the results with your hand calculations.

Suggested test values:
- Decimal 0
- Decimal 13 (binary should be `1101`, hexadecimal `D`)
- Decimal 47 (binary should be `101111`, hexadecimal `2F`)
- Decimal 255 (binary should be `11111111`, hexadecimal `FF`)

## 8. Practice questions

1. Convert `1010₂` to decimal.
2. Convert decimal 18 to binary.
3. Convert `A₁₆` to decimal.
4. How many bits are in 3 bytes?
5. Why does a computer need a character encoding?

**Check answers:** 1) 10, 2) 10010, 3) 10, 4) 24 bits. For question 5, explain that encoding maps characters to stored byte sequences and enables consistent decoding.

## Experiment log

| Input (decimal) | Binary result | Hex result | Did it match my hand calculation? |
|---:|---|---|---|
| 13 |  |  |  |
| 47 |  |  |  |
| 255 |  |  |  |

## Reflection

- Which conversion method was easiest for me?
- What mistake did I make, if any, and how did I correct it?
- Explain the difference between a bit and a byte in my own words.

## Completion checklist

- [ ] Explained the three number systems.
- [ ] Completed at least two hand conversions.
- [ ] Explained bits, bytes and character encoding.
- [ ] Ran the converter and recorded real results.
- [ ] Completed the reflection.

**Submission note:** Do not mark the converter as tested until you have run it on your computer.
