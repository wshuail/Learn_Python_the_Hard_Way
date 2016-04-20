#! /usr/bin/env python
# -*- coding: utf-8 -*-

from string import Template

def main():
    students = []
    students.append({'name': 'Tom', 'age': 24, 'height': 173})
    students.append({'name': 'Lisa', 'age': 21, 'height': 165})
    template = Template('$name is $age years old, and is $height tall.')
    for student in students:
        print (template.substitute(student))

if __name__ == '__main__':
    main()
