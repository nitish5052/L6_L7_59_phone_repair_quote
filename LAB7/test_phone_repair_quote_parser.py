import string

from hypothesis import given, strategies as st

from phone_repair_quote_parser import mask_imei, parse_model, parse_parts_order


non_text = st.one_of(
    st.none(), st.booleans(), st.integers(), st.binary(),
    st.lists(st.integers(), max_size=4), st.dictionaries(st.text(), st.integers(), max_size=4),
)
arbitrary_input = st.text() | non_text
imei_digits = st.text(alphabet=string.digits, min_size=15, max_size=15)
word = st.text(alphabet=string.ascii_letters, min_size=1, max_size=12)
part_names = st.sampled_from(["screen", "battery", "flex cable", "camera module"])


@given(arbitrary_input)
def test_mask_imei_no_crash(value):
    result = mask_imei(value)
    assert isinstance(result, str)
    if not isinstance(value, str):
        assert result == ""
    elif result:
        digits = "".join(value.split()).replace("-", "")
        assert len(digits) == 15
        assert all(digit in string.digits for digit in digits)
        assert result == "*" * 11 + digits[-4:]


@given(imei_digits, st.sampled_from(["", "-", " ", "\t"]))
def test_mask_imei_valid_formats(digits, separator):
    formatted = separator.join(digits)
    assert mask_imei(formatted) == "*" * 11 + digits[-4:]


@given(st.text(alphabet=string.digits, max_size=14))
def test_mask_imei_rejects_short_values(digits):
    assert mask_imei(digits) == ""


@given(arbitrary_input)
def test_parse_parts_order_no_crash(value):
    result = parse_parts_order(value)
    assert isinstance(result, dict)
    if not isinstance(value, str):
        assert result == {}
    assert all(part and part == part.strip() for part in result)
    assert all(type(quantity) is int and quantity > 0 for quantity in result.values())


@given(st.dictionaries(part_names, st.integers(min_value=1, max_value=100), min_size=1))
def test_parse_parts_order_round_trip(order):
    formatted = " ; ".join(f" {part} x {quantity} " for part, quantity in order.items())
    assert parse_parts_order(formatted) == order


@given(st.sampled_from(["", "battery", "battery x0", "battery x-1", "battery xone", "x2"]))
def test_parse_parts_order_rejects_malformed_item(item):
    assert parse_parts_order(f"screen x1; {item}") == {}


@given(arbitrary_input)
def test_parse_model_no_crash(value):
    result = parse_model(value)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(field, str) for field in result)
    fields = value.split(maxsplit=1) if isinstance(value, str) else []
    expected = (fields[0].title(), fields[1].strip()) if len(fields) == 2 else ("", "")
    assert result == expected


@given(word, st.lists(word, min_size=1, max_size=4), st.sampled_from([" ", "\t", "\u2003"]))
def test_parse_model_accepts_whitespace_separator(brand, words, separator):
    model = " ".join(words)
    assert parse_model(f"  {brand}{separator}{model}  ") == (brand.title(), model)


@given(word)
def test_parse_model_rejects_brand_only(brand):
    assert parse_model(brand) == ("", "")
