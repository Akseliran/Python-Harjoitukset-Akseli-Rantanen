import baseValues

# make larger numbers easier to read
def format_ants(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.2f}M"
    if n >= 10_000:
        return f"{n / 1_000:.1f}k"
    return f"{n:,}"

# progress bar
def progress_bar(ants, width=20):
    fillvalue = ants / baseValues.target
    filled = int(fillvalue * width)
    return f"[{'█' * filled}{'-' * (width - filled)}] {fillvalue:.0%}"

# show games status
def show_status(day, ants, today_boost):
    print(f"\nDay {day}/{baseValues.days} ({baseValues.days - day} left after today)")
    print(f"Ants: {format_ants(ants)} / {format_ants(baseValues.target)}")
    print(f"Goal: {progress_bar(ants)}")
    print(f"Growth tonight: x{baseValues.baseGrowth + today_boost:.2f}")
