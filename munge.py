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
    return(f"    {df['firstname']} {df['lastname_now']} ({df['lastname_school']}): {df['interest']}")

with open('out/registrants-by-attendance.txt', 'w') as fh:
    sys.stdout = fh
    print("Registrants by attendance:")
    print()
    for ans in [
            "Absolutely!  I'll be there if it happens!",
            "I need to know more - I'll decide later.",
            "No, but send me the information to buy a streaming ticket!"
    ]:
        people = df[df['ready'] == ans]
        print(f"{ans} ({len(people)} registrant(s))")
        for i, person in people.iterrows():
            print(fmt_for_attendance(person))
        print()



#import pudb ; pudb.set_trace()

