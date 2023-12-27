import datetime


# Function to generate the class schedule
def generate_class_schedule(slots, classes):

    class_schedule = {}

    for day, day_slots in slots.items():

        class_schedule[day] = []

        for slot, time in sorted(day_slots.items(), key=lambda x: x[1]):
            for course, course_slots in classes.items():
                if slot in course_slots:

                    class_schedule[day].append({"course": course, "time": time.strip()})

    return class_schedule


# Function to check for slot clashes
def check_slot_clashes(schedule):

    clashes = {}

    for day, classes in schedule.items():

        for i in range(len(classes) - 1):

            time_i = datetime.datetime.strptime(classes[i]["time"].split(" - ")[0].strip(), "%H:%M")  # Strip spaces
            end_time_i = datetime.datetime.strptime(classes[i]["time"].split(" - ")[1].strip(), "%H:%M")  # Strip spaces

            for j in range(i + 1, len(classes)):

                time_j = datetime.datetime.strptime(classes[j]["time"].split(" - ")[0].strip(), "%H:%M")  # Strip spaces
                end_time_j = datetime.datetime.strptime(classes[j]["time"].split(" - ")[1].strip(), "%H:%M")  # Strip spaces

                if end_time_i > time_j :

                    clashes.setdefault(day, []).append((classes[i]["course"], classes[j]["course"], classes[i]["time"]))

    return clashes
