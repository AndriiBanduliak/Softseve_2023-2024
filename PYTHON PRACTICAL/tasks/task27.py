import math
import logging


logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w")


def findingTangent(sin_alpha, cos_alpha):
    logging.info(f"A value has been entered sin(alpha) = {sin_alpha}")
    logging.info(f"A value has been entered cos(alpha) = {cos_alpha}")
    try:
        tan_αlpha = sin_alpha / cos_alpha
        message = f"The value of the tangent of the angle alpha is found = {
            tan_αlpha}"
        logging.debug(message)
    except ZeroDivisionError:
        message = "The cosine of the angle alpha = 0. The tangent is not defined."
        logging.warning(message)
    except:
        message = "The tangent of the angle alpha is not defined."
        logging.critical(message)


findingTangent(0.5, math.sqrt(3) / 2)
findingTangent(0.5, 'w')
findingTangent(0.5, 0)
