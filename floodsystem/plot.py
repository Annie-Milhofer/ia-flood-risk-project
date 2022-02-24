import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit

#Task 2E
def plot_water_levels(station, dates, levels):
    
    # Plot water level curve
    plt.plot(dates, levels, label = "Water level")

    # Plot typical high/low value range
    low, high = station.typical_range
    plt.axhline(y = low, color='r', linestyle='-', label = "Typical low range")
    plt.axhline(y = high, color='b', linestyle='-', label = "Typical high range")
    plt.legend(loc="upper left")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()
    plt.show()

#Task 2F
def plot_water_level_with_fit(station, dates, levels, p, *, show_high_low_range = False, dot_like_original_data = True):
    
    # Plot typical high/low value range
    if show_high_low_range:
        low, high = station.typical_range
        plt.axhline(y = low, color='r', linestyle='-', label = "Typical low range")
        plt.axhline(y = high, color='b', linestyle='-', label = "Typical high range")

    # Plot original data points
    if dot_like_original_data:
        plt.plot(dates, levels, '.', label = "Water level (original data)")
    else:
        plt.plot(dates, levels, label = "Water level (original data)")

    # Find polynomial fit
    poly, d0 = polyfit(dates, levels, p)

    # Plot polynomial fit
    dates_num = matplotlib.dates.date2num(dates)
    poly_fit_date_num = np.linspace(dates_num[0], dates_num[-1], 30)
    poly_fit_date = matplotlib.dates.num2date(poly_fit_date_num)
    plt.plot(poly_fit_date, poly(poly_fit_date_num - dates_num[0]), label = "Polynomial fit of order " + str(p))
   
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45);
    plt.title(station.name)

    # Display plot
    plt.legend(loc="lower left")
    plt.tight_layout()
    plt.show()