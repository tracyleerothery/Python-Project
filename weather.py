import csv
import statistics

from datetime import date, datetime


# print(data)

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    dt = datetime.fromisoformat(iso_string)
    return dt.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    temp_in_c = (float(temp_in_farenheit) - 32) * 5/9

    return round(temp_in_c, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.

            """
    newlist = [float(num) for num in weather_data]

    return statistics.mean(newlist)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    weather_data = []

    # opened and given file a name, varible name
    with open(csv_file, encoding="utf-8") as csv_file:
        # reader lets you put in csv file into somthing you can read
        reader = csv.reader(csv_file)
        next(reader)

        for line in reader:
            if line:
                # # alternative method
                # date_str, min_t, max_t = line
                # min_t = int(min_t)
                # max_t = int(max_t)

                # weather_data.append([date_str,  min_t, max_t])
                weather_data.append([line[0], int(line[1]), int(line[2])])

    return weather_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    newlist = [float(num) for num in weather_data]

    if newlist:

        min_values = [i for i, x in enumerate(newlist) if x == min(newlist)]
        return min(newlist), min_values[-1]

    return ()


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    newlist = [float(num) for num in weather_data]

    if newlist:

        max_values = [i for i, x in enumerate(newlist) if x == max(newlist)]
        return max(newlist), max_values[-1]

    return ()


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: is list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

#     # 5 Day Overview
#     # The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#     # The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#     # The average low this week is 12.2°C.
#     # The average high this week is 17.8°C.
#     #

    """Outputs a daily summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    day_overview = len(weather_data)

    list_of_days = [convert_date(x[0]) for x in weather_data]
    list_of_min_temp = [convert_f_to_c(x[1]) for x in weather_data]
    list_of_max_temp = [convert_f_to_c(x[2]) for x in weather_data]

    min_temp, min_index = find_min(list_of_min_temp)
    max_temp, max_index = find_max(list_of_max_temp)
    average_low = sum(list_of_min_temp) / len(list_of_min_temp)
    average_low = round(average_low, 1)

    average_high = sum(list_of_max_temp) / len(list_of_max_temp)
    average_high = round(average_high, 1)

    # finding postion of min temp in list
    min_date = list_of_min_temp.index(min_temp)
    date_min = list_of_days[min_date]  # finds the actual date for the MIN temp

    max_date = list_of_max_temp.index(max_temp)
    date_max = list_of_days[max_date]

    return f"""{day_overview} Day Overview
  The lowest temperature will be {min_temp}°C, and will occur on {date_min}.
  The highest temperature will be {max_temp}°C, and will occur on {date_max}.
  The average low this week is {average_low}°C.
  The average high this week is {average_high}°C.
"""


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    summary = []

    for data in weather_data:
        date = convert_date(data[0])
        min_temp = convert_f_to_c(data[1])
        max_temp = convert_f_to_c(data[2])
        summary.append(
            # f"""----  {date} ----\n  Minimum Temperature: {min_temp}°C\n  Maximum Temperature: {max_temp}°C\n""")
            f"""---- {date} ----
  Minimum Temperature: {min_temp}°C
  Maximum Temperature: {max_temp}°C
""")

        x = "\n".join(summary)

    return(x+"\n")
