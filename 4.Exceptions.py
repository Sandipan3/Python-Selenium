def divide(a,b):
    if(b < 0):
        raise Exception("We are not accepting negative denominator")
    return a / b

def test(a,b):
    try:
        res = divide(a,b)
        print(f"{a}/{b} = {res}")
    except TypeError:
        print("Invalid Number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print(e)

# this is ok!
# test(10, 2)

# Cannot divide by zero
# test(10, 0)

test(10, -2)
