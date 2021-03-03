#!/usr/bin/env python

# How many people are planning to attend and how many are not sure yet (and if anyone took the survey but just wants tickety info)
# Breakdown of cast/crew/orchestra/just for fun responses
# Shows that are not yet represented at all

import sys

import numpy as np
import pandas as pd

col_names = [
    'timestamp',
    'paid',
    'firstname',
    'lastname_school',
    'lastname_now',
    'pronouns',
    'email',
    'questions',
    'ready',
    'traveling',
    'graduated',
    'interest',
    'cast_in',
    'voicepart',
    'lead',
    'performing_experience',
    'crew_in',
    'crew_specialty',
    'crew_experiences',
    'pit_in',
    'instruments_since',
    'instruments_since_bring',
    'instruments_since_nobring',
    'instruments_try',
    'fun_in',
    'gopher',
    'addl_expertise',
    ]
df = pd.read_csv('responses.csv', names=col_names, skiprows=[0])
df = df.replace(np.nan, '')


def section(): print(40*'=')

stdout_orig = sys.stdout

##### Attendance
def fmt_for_attendance(df):
    output = 8*" " + f"{df['firstname']} {df['lastname_now']} ({df['lastname_school']})")
    return output

with open('out/registrants-by-attendance.txt', 'w') as fh:
    sys.stdout = stdout_orig #fh
    print("Registrants by attendance:")
    print()
    for attendance in [
            "Absolutely!  I'll be there if it happens!",
            "I need to know more - I'll decide later.",
    ]:
        people = df[df['ready'] == attendance]
        print(f"{attendance} ({len(people)} total)")

        interested_people = people[people['interest'] == 'Cast']
        interested_people = interested_people[interested_people['lead'] == 'Yes']
        if int(len(interested_people)) > 0:
            print(f"    Interested in Lead ({len(interested_people)} total):")
            for i, person in interested_people.iterrows():
                print(fmt_for_attendance(person))

        interested_people = people[people['interest'] == 'Cast']
        interested_people = interested_people[interested_people['lead'] == 'Would accept one if necessary']
        if int(len(interested_people)) > 0:
            print(f"    Interested in Lead if necessary ({len(interested_people)} total):")
            for i, person in interested_people.iterrows():
                print(fmt_for_attendance(person))                

        interested_people = people[people['interest'] == 'Cast']
        if len(interested_people) > 0:
            print(f"    Interested in Cast ({len(interested_people)} total):")
            for i, person in interested_people.iterrows():
                print(fmt_for_attendance(person))

        for interest in ["Crew", "Orchestra", "Just showing up for the fun!"]:
            interested_people = people[people['interest'] == interest]
            if len(interested_people) > 0:
                print(f"    Interested in {interest} ({len(interested_people)} total):")
                for i, person in interested_people.iterrows():
                    print(fmt_for_attendance(person))
        print()

    attendance = 'No, but send me the information to buy a streaming ticket!'
    people = df[df['ready'] == attendance]
    print(f"{attendance} ({len(people)} total)")
    for i, person in people.iterrows():
        print(fmt_for_attendance(person))


# ##### Interest
# def fmt_for_interest(df):
#     return("slkdfj")

# with open('out/registrants-by-interest.txt', 'w') as fh:
#     sys.stdout = stdout_orig # fh
#     print("Registrants by interest:")

#     for attendance in [
#             "Absolutely!  I'll be there if it happens!",
#             "I need to know more - I'll decide later.",
#             "No, but send me the information to buy a streaming ticket!"
#     ]:
#         print(f"    {attendance}:")
        
#         people = df[df['ready'] == attendance]
#         for interest in [
#             "Cast",
#             "Crew",
#             "Orchestra",
#             "Just showing up for the fun!"
#         ]:
#             interests = people[people['interest'] == interest]
#             for i, person in interests.iterrows():
#                 print(fmt_for_interest(person))
#         print()
