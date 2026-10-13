
import libs.common.number

note = "module libs.common.number contains mathematic functions"

import libs.common.number as num

note = "module libs.calculate contains mathematic function"

def calc_hypotenuse(a, b):
    return num.sqrt(num.pow(a) + num.pow(b))
