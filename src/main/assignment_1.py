# chops a number to [digits] sig figs
def chopping_value(num, digits):
    num = str(num)
    build = ""

    reached_nonzero = False

    index = 0
    while index < len(str(num)):
        if digits > 0:
            build += num[index]
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
            if rounding == "none":
                c += c_additional
            elif rounding == "rounding":
                c += rounding_value(c_additional, 3)
            elif rounding == "chopping":
                c += chopping_value(c_additional, 3)

    # print("c: " + str(c))

    # compute f
    f = 0
    for i in range(52):  # range goes from [0, 51]
        if f_raw[i] == '1':
            f_additional = 0.5**(i+1)
            if rounding == "none":
                f += f_additional
            elif rounding == "rounding":
                f += rounding_value(f_additional, 3)
            elif rounding == "chopping":
                f += chopping_value(f_additional, 3)

    # print("f: " + str(f))

    # compute the resulting number
    result = ((-1)**s) * (2**(c-1023)) * (1+f)
    if rounding == "rounding":
        result = rounding_value(result, 3)
    elif rounding == "chopping":
        result = chopping_value(result, 3)
    return result


if __name__ == "__main__":

    number_raw = "0100000001111110101110010000000000000000000000000000000000000000"

    # Part 1
    print("%.5f" % bin_to_double(number_raw))

    print("")

    # Part 2
    print("%.3g" % bin_to_double(number_raw, rounding = "chopping"))

    print("")

    # Part 3
    print("%.3g" % bin_to_double(number_raw, rounding = "rounding"))


