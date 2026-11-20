import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value

#Example test cases:
def test_budget_screen():
    assert repair_quote("screen", "budget", False, False) == 4600

def test_in_stock_quick():
    assert repair_days("battery", True, 2) == 1

#Write the rest of the test cases so that the code is 90- 100% covered.


@pytest.mark.parametrize(
    "part, tier, warranty, express, expected",
    [
        pytest.param("screen", "flagship", False, False, 8600, id="Q02"),
        pytest.param("battery", "budget", False, False, 1800, id="Q03"),
        pytest.param("battery", "flagship", False, False, 3300, id="Q04"),
        pytest.param("camera", "budget", False, False, 2800, id="Q05"),
        pytest.param("charging_port", "budget", False, False, 1100, id="Q06"),
        pytest.param("screen", "budget", True, False, 4600, id="Q07"),
        pytest.param("screen", "flagship", True, True, 9100, id="Q08"),
        pytest.param("battery", "flagship", True, False, 300, id="Q09"),
        pytest.param("camera", "budget", True, True, 800, id="Q10"),
        pytest.param("charging_port", "budget", False, True, 1600, id="Q11"),
    ],
)
def test_quote_amount(part, tier, warranty, express, expected):
    assert repair_quote(part, tier, warranty, express) == expected


@pytest.mark.parametrize(
    "part, tier, warranty, express, expected",
    [
        pytest.param("speaker", "budget", False, False, "unknown part", id="Q12"),
        pytest.param("screen", "premium", False, False, "unknown brand tier", id="Q13"),
    ],
)
def test_quote_rejects_invalid_input(part, tier, warranty, express, expected):
    with pytest.raises(ValueError) as error:
        repair_quote(part, tier, warranty, express)
    assert str(error.value) == expected


@pytest.mark.parametrize(
    "part, in_stock, technicians, expected",
    [
        pytest.param("screen", True, 0, 3, id="D02"),
        pytest.param("screen", False, 1, 6, id="D03"),
        pytest.param("camera", False, 0, 8, id="D04"),
        pytest.param("battery", False, 0, 5, id="D05"),
        pytest.param("charging_port", False, 2, 3, id="D06"),
    ],
)
def test_turnaround_days(part, in_stock, technicians, expected):
    assert repair_days(part, in_stock, technicians) == expected


@pytest.mark.parametrize(
    "price, age, cracked, expected",
    [
        pytest.param(10000, 0, False, 6000, id="T01"),
        pytest.param(10000, 12, False, 6000, id="T02"),
        pytest.param(10000, 13, False, 4000, id="T03"),
        pytest.param(10000, 24, False, 4000, id="T04"),
        pytest.param(10000, 25, False, 2000, id="T05"),
        pytest.param(10000, 48, False, 2000, id="T06"),
        pytest.param(10000, 49, False, 0, id="T07"),
        pytest.param(10005, 12, True, 3001, id="T08"),
    ],
)
def test_trade_in_amount(price, age, cracked, expected):
    assert trade_in_value(price, age, cracked) == expected


@pytest.mark.parametrize(
    "price, age, cracked, expected",
    [
        pytest.param(0, 12, False, "invalid input", id="T09"),
        pytest.param(-1, 12, False, "invalid input", id="T10"),
        pytest.param(10000, -1, False, "invalid input", id="T11"),
    ],
)
def test_trade_in_rejects_invalid_input(price, age, cracked, expected):
    with pytest.raises(ValueError) as error:
        trade_in_value(price, age, cracked)
    assert str(error.value) == expected
