#!/usr/bin/env python

# How many people are planning to attend and how many are not sure yet (and if anyone took the survey but just wants tickety info)
# Breakdown of cast/crew/orchestra/just for fun responses
# Shows that are not yet represented at all

from datetime import date
import sys

import numpy as np
import pandas as pd

version = "2.0.0"

with open('responses.csv', 'r') as infile:
    with open('responses_preprocessed.csv' ,'w') as outfile:
        for line in infile.readlines():
            outfile.write(line.replace('Hello, ', 'Hello '))

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
    'orchestra_in',
    'instruments_since',
    'instruments_since_bring',
    'instruments_since_nobring',
    'instruments_try',
    'fun_in',
    'gopher',
    'addl_expertise',
    ]
df = pd.read_csv('responses_preprocessed.csv', quotechar='"', names=col_names, skiprows=[0])
df = df.replace(np.nan, '')

stdout_orig = sys.stdout

def indent(input, num=1, char=' '): return num * 4 * char + input

def version_str(): return(f"Revision {version} ({date.today().strftime('%d %b %Y')})")

##### Attendance
def fmt_person(df):
    output = indent(f"{df['firstname']} {df['lastname_now']} ({df['lastname_school']})", 0)
    output += "\n"
    if df['cast_in'] != '':
        output += indent(f"Cast: {df['cast_in']}", 3)
    if df['orchestra_in'] != '':
        output += indent(f"Orchestra: {df['orchestra_in']}", 3)
    if df['crew_in'] != '':
        output += indent(f"Crew: {df['crew_in']}", 3)
    return output

def print_people(people, interest):
    if int(len(people)) > 0:
        print(indent(f"Interested in {interest} ({len(people)} total):"))
        for i, person in people.iterrows():
            print(indent(fmt_person(person), 2))



with open('out/registrants-by-attendance.txt', 'w') as fh:
    sys.stdout = fh
    print("Registrants by attendance:")
    print(version_str())
    print()
    for attendance in [
            "Absolutely!  I'll be there if it happens!",
            "I need to know more - I'll decide later.",
    ]:
        people = df[df['ready'] == attendance]
        print(f"{attendance} ({len(people)} total)")

        interested_people = people[people['interest'] == 'Lead']
        interested_people = interested_people[interested_people['lead'] == 'Yes']
        print_people(interested_people, 'Cast')

        interested_people = people[people['interest'] == 'Cast']
        interested_people = interested_people[interested_people['lead'] == 'Would accept one if necessary']
        print_people(interested_people, 'Lead if necessary')

        interested_people = people[people['interest'] == 'Cast']
        print_people(interested_people, 'Cast')

        for interest in ["Crew", "Orchestra", "Just showing up for the fun!"]:
            interested_people = people[people['interest'] == interest]
            print_people(interested_people, interest)

        print()

    attendance = 'No, but send me the information to buy a streaming ticket!'
    interested_people = df[df['ready'] == attendance]
    print(f"{attendance} ({len(people)} total)")
    for i, person in interested_people.iterrows():
        print(indent(fmt_person(person)))



##### Shows
with open('out/unrepresented-shows.txt', 'w') as fh:
    shows_responded = []
    sys.stdout = fh
    for idx, row in df[['cast_in', 'crew_in', 'orchestra_in']].iterrows():
        for subrow in row:
            for show in subrow.split(', '):
                shows_responded.append(show)
    shows_responded = set(shows_responded)

    print(f"Unrepresented shows:")
    print(version_str())
    for s in set(
            set(
                [
                    "Fiddler on the Roof",
                    "Hello Dolly 1989",
                    "Anything Goes 1990",
                    "Guys and Dolls",
                    "Li'l Abner",
                    "Peter Pan 1993",
                    "Annie Get Your Gun",
                    "Jesus Christ Superstar 1995",
                    "The Music Man",
                    "Man of La Mancha",
                    "Pirates of Penzance",
                    "The King and I",
                    "On the 20th Century",
                    "Evita",
                    "Hello Dolly 2003",
                    "Anything Goes 2004",
                    "Seussical",
                    "Pippin",
                    "Les Miserables",
                    "Beauty and the Beast",
                    "The Wizard of Oz",
                    "Annie",
                    "The Phantom of the Opera",
                    "Curtains",
                    "Young Frankenstein",
                    "Sweeney Todd",
                    "Peter Pan 2016",
                    "Spamalot",
                    "The Drowsy Chaperone",
                    "Mamma Mia",
                    "Jesus Christ Superstar 2020",
                    "Jesus Christ Superstar 2021"
                ]
            ) - shows_responded):
        print(indent(s))


##### Questions
with open('out/questions.txt', 'w') as fh:
    sys.stdout = fh
    print(f"Questions:")
    print(version_str())
    print()
    for l in df[
            ~df.questions.isin(
                [
                    '', 'None', 'N/a', 'None at this time', 'None really',
                ])]['questions']:
        print(f"{l}\n")
    

    
