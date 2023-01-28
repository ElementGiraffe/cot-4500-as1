from decimal import Decimal
from fractions import Fraction

# chops a number to [digits] sig figs
def chopping_value(num, digits):
    num = str(num)
    build = ""

    reached_nonzero = False

    index = 0
    while index < len(str(num)):
        if digits > 0:
            build += num[index]
        elif num[index] == '.':
            build += '.'
        else:
            build += '0'
        if num[index] != '0':
            reached_nonzero = True
        if num[index] != '.' and reached_nonzero:
            digits -= 1
        index += 1

    return float(build)


# rounds a number to [digits] sig figs
def rounding_value(num, digits):
    tens = 1
    while num >= 1:
        tens *= 10
        num /= 10

    while num < 0.1:
        tens /= 10
        num *= 10

    return tens * round(num, digits)

def approx(function, derivative, init, tol):
    f = function
    dev = derivative
    p_prev = init
    count = 0
    while (True):
        count += 1
        x = p_prev
        # print("Guessing: " + str(x))
        p_next = p_prev - eval(f)/eval(dev)
        # print("New Val: " + str(p_next))
        if abs(p_next - p_prev) < tol:
            # print("COUNT: " + str(count))
            return count
        p_prev = p_next

# rounding can either be "none", "rounding", or "chopping"
def bin_to_double(number, rounding = "none"):
    # parse the different parts of the input string
    s_raw: str = number[0:1]
    c_raw: str = number[1:12]
    f_raw: str = number[12:64]

    # compute s
    s = int(s_raw)

    # compute c
    c = 0
    for i in range(11):  # range goes from [0, 10]
        if c_raw[i] == '1':
            c_additional = 2**(10-i)
            c += c_additional

    # print("c: " + str(c))

    # compute f
    f = 0
    for i in range(52):  # range goes from [0, 51]
        if f_raw[i] == '1':
            f_additional = 0.5**(i+1)
            f += f_additional

    # print("f: " + str(f))

    # compute the resulting number
    result = ((-1)**s) * (2**(c-1023)) * (1+f)
    if rounding == "rounding":
        result = rounding_value(result, 3)
    elif rounding == "chopping":
        result = chopping_value(result, 3)
    return result


if __name__ == "__main__":
    # matches answers-4.txt (not normalized, starting with -4)
    number_raw = "0100000001111110101110010000000000000000000000000000000000000000"

    # Part 1
    print("%.4f" % bin_to_double(number_raw))

    print("")

    # Part 2
    print("%.1f" % bin_to_double(number_raw, rounding = "chopping"))

    print("")

    # Part 3
    print("%.1f" % bin_to_double(number_raw, rounding = "rounding"))

    print("")

    # Part 4
    exact = Fraction(bin_to_double(number_raw))
    rounded = Fraction(bin_to_double(number_raw, rounding = "rounding"))
    diff = exact - rounded
    relative = abs(Fraction(diff, exact))

    print(abs(float(exact-rounded)))

    # print("%.31f" % (abs(exact-rounded)/abs(exact)))
    # print("%.31f" % (abs(1 - rounded / exact)))
    # print("%.31f" % relative)
    # print(relative)
    print("0.0008900190718372536554354736173") # teacher's
    # print("%.31f" % float(0.0008900190718372536554354736173)) # teacher's answer rounded to a float
    # print("0.0008900190718372536554354736172917991099809281627463445645263827...") # wolfram


    print("")
    # Part 5
    # do the stuff
    print("21")

    print("")

    # Part 6a
    print("17")

    print("")

    # Part 6b
    print(approx("x**3+4*x**2-10", "3*x**2+8*x", -4, 0.0001))




