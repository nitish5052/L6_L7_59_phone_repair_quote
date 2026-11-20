# Lab 7 — Fuzzing for Input Validation Bugs

**C NITISH** · **PES1UG25CS809**

The phone repair parser accepts an IMEI, a parts order, and a phone brand and model. Hypothesis checks each parser with generated valid inputs, malformed text, and non-text values.

## Run the application and tests

Run from `LAB7/` with Python 3.8 or newer.

```text
python -m pip install pytest hypothesis
python phone_repair_quote_parser.py
python -m pytest test_phone_repair_quote_parser.py -v
```

| Function | Accepted input | Invalid result |
|---|---|---|
| `mask_imei` | 15 ASCII digits, optionally formatted with whitespace and hyphens. Masks the first 11 digits. | Empty string |
| `parse_parts_order` | Semicolon-separated `PART xQTY` items with positive ASCII integer quantities. The final quantity wins for repeated part names. | Empty dictionary for the entire order |
| `parse_model` | A brand followed by whitespace and a nonempty model name. Title-cases the brand and retains the model text. | Pair of empty strings |

## Deliverables

- `phone_repair_quote_parser.py` contains the hardened parser and interactive application.
- `test_phone_repair_quote_parser.py` contains nine Hypothesis properties covering all three functions.
- [PES1UG25CS809_C_NITISH_LAB7.pdf](PES1UG25CS809_C_NITISH_LAB7.pdf) contains the findings and screenshots SS1–SS4. All nine properties failed on the starter and passed after the fixes.
