
def calc(expr):
    valid_operations = ('+', "-", "*", "/")
    result = ""
    try:
        assert len(expr) == 3, "Wrong expression or number of parameters."
        op = expr[0]
        assert op in valid_operations, f"'{op}' is not valid operation. Try one of this: {valid_operations}"

        numb1 = int(expr[1])
        numb2 = int(expr[2])
        if op == "+":
            result = numb1 + numb2
        elif op == "-":
            result = numb1 - numb2
        elif op == "*":
            result = numb1 * numb2
        elif op == "/":
            result = numb1 / numb2
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Another exception: {e}")

    return result


while True:
    # expr = input("Enter expression in polish notation or \"Q\" to exit:\n" ).strip()
    # expr = "- 3  %"
    expr = "/ 3  0"
    # expr = "- 3  6 6"
    if expr in ["q", "Q"]:
        break
    print(calc(expr.split()))
    break

