import datetime

from classes import *
from schedule import *


# Function to generate the class schedule
def generate_class_schedule(slots, classes):
    class_schedule = {}

    for day, day_slots in slots.items():
        class_schedule[day] = []

        for slot, time in day_slots.items():
            for course, course_slots in classes.items():
                if slot in course_slots:
                    class_schedule[day].append({"course": course, "time": time})

    return class_schedule


# Generate and print the class schedule
class_schedule = generate_class_schedule(slots, cse_classes)

for day, classes in class_schedule.items():
    print(f"--- {day} ---")

    for class_info in classes:
        print(f"\t\t {class_info['time']} : {class_info['course']}")

    print()
