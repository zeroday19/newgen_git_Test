# from app.calculator import Calculator
# fixture


def test_add(calc, dataset):
    output = calc.add(dataset["x"], dataset["y"])
    assert output == dataset["a"]


def test_subtract(calc, dataset):

    output = calc.substract(dataset["x"], dataset["y"])
    assert output == dataset["s"]


def test_multiply(calc, dataset):
    output = calc.mulitply(dataset["x"], dataset["y"])
    assert output == dataset["m"]


def test_div(calc, dataset):

    output = calc.division(dataset["x"], dataset["y"])
    assert output == dataset["d"]
