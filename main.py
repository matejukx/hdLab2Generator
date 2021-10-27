import datetime
import time

from dateutil import relativedelta

from process import Process

if __name__ == '__main__':

    start_time = datetime.date.fromisoformat("2015-01-01")
    end_time = datetime.date.fromisoformat("2020-01-01")

    start = time.perf_counter()
    process = Process(start_time=start_time,
                      end_time=end_time,
                      number_of_students=10000,
                      number_of_instructors=300,
                      number_of_lecturers=3)
    print("Starting to initialize people")
    process.initialize_people()
    ppl_finish_string = f"Initialization finished.\nCreated {len(process.students)} " \
                        f"students - that means we should have around " \
                        f"{len(process.students) / int((end_time - start_time).days / 30)} students per month.\n" \
                        f"We've also created {len(process.instructors)} instructors.\n" \
                        f"In {time.perf_counter() - start} seconds."
    print(ppl_finish_string)

    start = time.perf_counter()
    print('Starting to initialize activities - half of the months')
    current_month = start_time
    # pierwsza czesc generowania T0-T1
    for _ in range(int((end_time - start_time).days / 30 / 2)):
        process.create_activities(date_of_inclusion=current_month, hours_per_drive=4)
        current_month += relativedelta.relativedelta(months=1)

    # tutaj zmiana danych nastepuje w T1

    # lecimy dalej z generowaniem T1-T2
    for _ in range(int((end_time - start_time).days / 30 / 2)):
        process.create_activities(date_of_inclusion=current_month, hours_per_drive=4)
        current_month += relativedelta.relativedelta(months=1)

    print(f'Created {len(process.lectures)} lectures.\n'
          f'Created {len(process.drives)} drives.'
          f'\nIt took {time.perf_counter() - start} seconds to create activities for all students')

    all_rows = len(process.students) + len(process.lectures) + len(process.instructors) + len(
        process.lectures) + len(process.drives) + len(process.courses)
    print(f'We created {all_rows} rows for our SQL database')

    # tutaj generowanie plików do importu SQL
