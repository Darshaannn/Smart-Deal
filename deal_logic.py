
def get_deal(predicted_price, asking_price, tolerance):

    difference= asking_price-predicted_price

    difference_percent = (difference/predicted_price)*100

    # tolearance = 2 
    # -5 -4 -3 -2 -1 0 1 2 3 4 5
    
    if difference_percent < -(2*tolerance):
        verdict="Excellent Deal"

    elif difference_percent < -(tolerance):
        verdict="Good Deal"

    if difference_percent <= (tolerance):
        verdict="Fair Deal"

    if difference_percent < (2*tolerance):
        verdict="Overpriced Deal"

    else:
        verdict = "Very Overpriced Deal"

    return difference, difference_percent, verdict