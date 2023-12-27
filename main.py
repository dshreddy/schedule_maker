from classes import *
from funcs import *
from schedule import *

# Generate and print the class schedule
class_schedule = generate_class_schedule(slots, my_courses)

print("\n---> Schedule:\n")
for day, classes in class_schedule.items():
    print(f"\t--- {day} ---")

    for class_info in sorted(classes, key=lambda x: x["time"]):
        print(f"\t\t {class_info['time']} : {class_info['course']}")

    print()

# Print slot clashes, if any
slot_clashes = check_slot_clashes(class_schedule)

if slot_clashes:
    print("\n---> Slot Clashes:\n")

    for day, clashes in slot_clashes.items():
        print(f"\t--- {day} ---")

        for clash in clashes:
            print(f"\t\t {clash[0]} & {clash[1]} clashes at {clash[2]}")
        print()
