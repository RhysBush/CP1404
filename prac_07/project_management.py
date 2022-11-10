"""
Estimated time: 1 hour
Actual time: ~2.2 hours
"""
from project import Project
import datetime
from operator import attrgetter

MENU = "(L)oad Projects\n" \
       "(S)ave Projects\n" \
       "(D)isplay Projects\n" \
       "(F)ilter Projects by Date\n" \
       "(A)dd New Project\n" \
       "(U)pdate Project"
FILENAME = "projects.txt"


def main():
    """Loads projects file and displays menu."""
    print(MENU)
    projects = load_projects(FILENAME)
    choice = input('>>> ').upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Enter filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            display_date_filtered_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input('>>> ').upper()


def load_projects(filename):
    """Load projects from entered filename."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        projects.append(Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4])))
    return projects


def add_project(projects):
    """Get project details from user and append to list of projects."""
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = input("Priority: ")
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    projects.append(Project(name, date, priority, cost_estimate, percent_complete))


def update_project(projects):
    """Get choice  from user for which project to update and get values that require updating."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project Choice: "))
    print(projects[choice])
    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        new_percentage = int(new_percentage)
        projects[choice].completion_percentage = new_percentage
    new_priority = input("New Priority: ")
    if new_priority != "":
        new_priority = int(new_priority)
        projects[choice].priority = new_priority


def display_projects(projects):
    """Display incomplete and complete projects separately."""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_completed()]
    incomplete_projects.sort(key=attrgetter('priority'))
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    completed_projects = [project for project in projects if project.is_completed()]
    completed_projects.sort(key=attrgetter('priority'))
    for project in completed_projects:
        print(f"  {project}")


def display_date_filtered_projects(projects):
    """Get date from user and display projects by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date_threshold = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= date_threshold]
    filtered_projects.sort(key=attrgetter('start_date'))
    for project in filtered_projects:
        print(project)


def save_projects(filename, projects):
    """Save projects to file."""
    out_file = open(filename, 'w')
    for project in projects:
        print(
            f"{project.name}\t{project.start_date}\t{project.priority}\t"
            f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    out_file.close()


main()
