minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

if hours > 0:
    print(f"{hours} hr{'s' if hours > 1 else ''} {remaining_minutes} minutes")
else:
    print(f"{remaining_minutes} minutes")