import datetime
from zoneinfo import ZoneInfo
import calendar
import sys

def calstr(year, month):
    """
    Return a calendar string for the specified year and month.
    
    Args:
        year (int): The year (e.g., 2025)
        month (int): The month (1-12)
        
    Returns:
        str: Formatted calendar month as multiline string
    """
    cal = calendar.TextCalendar(calendar.MONDAY)
    return cal.formatmonth(year, month)

def print_calendar(year, month, before=1, after=1):
    """
    Print calendars for `before` months before + current month + `after` months after,
    all in one horizontal row.
    
    Args:
        year (int): Year of the reference month
        month (int): Month (1-12) of the reference month
        before (int): Number of months before to show
        after (int): Number of months after to show
    """
    cal_strs = []

    # Helper to decrement month/year properly
    def prev_month(y, m):
        m -= 1
        if m < 1:
            m = 12
            y -= 1
        return y, m

    # Helper to increment month/year properly
    def next_month(y, m):
        m += 1
        if m > 12:
            m = 1
            y += 1
        return y, m

    # Collect calendars for before months
    y, m = year, month
    for _ in range(before):
        y, m = prev_month(y, m)
        cal_strs.insert(0, calstr(y, m))  # Insert at front

    # Add current month calendar
    cal_strs.append(calstr(year, month))

    # Collect calendars for after months
    y, m = year, month
    for _ in range(after):
        y, m = next_month(y, m)
        cal_strs.append(calstr(y, m))

    for cal_start in range(0, before + 1 + after, 3):
        cals = [cal.splitlines() for cal in cal_strs[cal_start : cal_start + 3]]
        longest_line = max(max([len(line) for line in lines]) for lines in cals)
        for row_id in range(max([len(c) for c in cals])):
            lines = []
            for cal in cals:
                if(row_id < len(cal)):
                    lines.append(cal[row_id])
                else:
                    lines.append("")
            padded_lines = [line + " " * (longest_line - len(line) + 1) for line in lines]
            print(" ".join(padded_lines), file=sys.stderr)
        print(file=sys.stderr)



def get_current_times(timezones):
    """
    Get the current time in UTC and convert to other timezones.

    Args:
        timezones (list of str): List of timezone names, e.g. ['US/Eastern', 'Europe/London']

    Returns:
        dict: Mapping of timezone names to current datetime strings
    """
    # Get current UTC time as aware datetime
    utc_now = datetime.datetime.now(tz=ZoneInfo("UTC"))
    times = {'UTC': utc_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}

    for tz_name in timezones:
        tz = ZoneInfo(tz_name)
        times[tz_name] = utc_now.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    return times


def cal():
    tzs = ['US/Pacific', 'US/Eastern', 'Europe/London', 'Asia/Tokyo']
    current_times = get_current_times(tzs)
    max_tzs_length = max([len(tz) for tz in tzs])
    for zone, time_str in current_times.items():
        print(zone + " " * (max_tzs_length - len(zone) + 1) , time_str, file = sys.stderr)

    print(file = sys.stderr)

    today = datetime.date.today()
    print_calendar(today.year, today.month)


if __name__ == "__main__":
    cal()
