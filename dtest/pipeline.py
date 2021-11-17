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
    status = 'Normal'
    if blood_sugar > 140:
        status = 'Prediabetes'
    if blood_sugar > 200:
        status = 'Diabetes'
    return status
