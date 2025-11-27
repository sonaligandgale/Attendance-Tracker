import sys

if len(sys.argv) != 3:
    print("Usage: python attendance_tracker.py <classes_held> <classes_attended>")
    sys.exit()

held = int(sys.argv[1])
attended = int(sys.argv[2])

percentage = (attended / held) * 100

print("Attendance Percentage:", percentage, "%")
