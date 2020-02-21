valid_operations = ('+', "-", "*", "/")


def calc(expr):
    result = ""
    try:
        assert len(expr) == 3, "Wrong expression or number of parameters."
        op = expr[0]
        assert op in valid_operations, f"'{op}' is not valid operation. Try one of this: {valid_operations}"

        numb1 = int(expr[1])
        numb2 = int(expr[2])
        assert numb1 > 0 and numb2 > 0, "Operands should be positive numbers"

        if op == "+":
            result = numb1 + numb2
        elif op == "-":
            result = numb1 - numb2
        elif op == "*":
            result = numb1 * numb2
        elif op == "/":
            result = numb1 / numb2
    except ZeroDivisionError:
        print("ERROR. ZeroDivisionError")
    except AssertionError as e:
        print(f"ERROR. AssertionError: {e}")
    except ValueError as e:
        print(f"ERROR. ValueError: {e}")
    except Exception as e:
        print(f"ERROR. Another exception: {e}")

    return result


while True:
    expr = input("===Enter expression in polish notation or \"Q\" to exit:\n").strip()
    if expr in ["q", "Q"]:
        print("Goodbye")
        break
    res = calc(expr.split())
    if res:
        print(f"{expr} = {res}")


