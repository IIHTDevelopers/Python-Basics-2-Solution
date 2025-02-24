# Function to perform weather analysis
def weather_analysis(temperatures):
    max_temp = max(temperatures)
    min_temp = min(temperatures)

    # Identify extreme temperatures (above 34°C or below 30°C)
    extreme_temps = {temp for temp in temperatures if temp > 34 or temp < 30}

    report = f"""
    Weather Analysis Report
    ------------------------
    Temperatures (°C): {sorted(temperatures)}
    Highest Temperature: {max_temp}
    Lowest Temperature: {min_temp}
    Extreme Temperatures Detected: {sorted(extreme_temps) if extreme_temps else 'None'}
    """

    print(report)
    return report

# Function to save the weather report to a file
def save_report_to_file(report, filename):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(report + "\n")
    print(f" Report saved to '{filename}'")

# Sample temperature dataset (in Celsius) as a set
temperatures = {32.5, 34.0, 31.2, 29.8, 35.5}

# Perform weather analysis and save report
report = weather_analysis(temperatures)
save_report_to_file(report, "weather_report.txt")
