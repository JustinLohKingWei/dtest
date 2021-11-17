# Checks if an input can be converted into a numeric value
def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    except TypeError:
        return False

# finds average of parsed test results
def average(t1, t2, t3):
    input = [t1, t2, t3]
    val = []
    for x in input:
        # assumming largest value for blood sugar is 2565.0
        if isDigit(x) and 0 < float(x) <= 2565.0:
            val.append(float(x))
    if len(val) != 0:
        avg = sum(val)/len(val)
    else:
        avg = 0
    # displays average with a maximum of 2 decimal points
    return round(avg,2)

# returns diagnostic results based on average blood sugar
def check_diabetes(blood_sugar):
    # Checks for invalid inputs
    if blood_sugar < 0:
        status = 'Invalid Result'
    else :
        status = 'Normal'
    # blood equal to or larger than 140 indicates Prediabetes
        if blood_sugar > 139:
            status = 'Prediabetes'
    # blood equal to or larger than 200 indicates Diabetes
        if blood_sugar > 199:
            status = 'Diabetes'
        if blood_sugar > 2596:
            status = 'Invalid Result'
    return status
