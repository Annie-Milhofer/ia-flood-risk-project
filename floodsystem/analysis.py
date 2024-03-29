import numpy as np
import matplotlib.dates

#Task 2F
def polyfit(dates, levels, p):
    dates_num = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(dates_num - dates_num[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, dates_num[0]

#Task 2G
def polyfit_coeff(dates, levels, p):
    dates_num = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(dates_num - dates_num[0], levels, p)
    return p_coeff
