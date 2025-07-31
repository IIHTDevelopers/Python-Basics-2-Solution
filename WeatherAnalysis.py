def read_temperatures_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            temps = [float(line.strip()) for line in file if line.strip()]
        return temps
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def analyze_temperatures(temps):
    max_temp = max(temps)
    min_temp = min(temps)
    extreme_temps = [t for t in temps if t > 34 or t < 30]

    report = f"""
    Weather Analysis Report
    ------------------------
    Temperatures (°C): {temps}
    Highest Temperature: {max_temp}
    Lowest Temperature: {min_temp}
    Extreme Temperatures Detected: {sorted(extreme_temps) if extreme_temps else 'None'}
    """
    return report

def main():
    filename = "temperatures.txt"
    temps = read_temperatures_from_file(filename)
    if temps:
        report = analyze_temperatures(temps)
        print(report)

if __name__ == "__main__":
    main()
