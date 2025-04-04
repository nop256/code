def combo_string(a, b):

    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a

    return short + long + short
