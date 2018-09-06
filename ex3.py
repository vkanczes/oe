#!/usr/bin/python

str_current_time = input("What is the current time?")
current_time = int(str_current_time)

str_hours_to_wait = input("How many hours do you want to wait for the wake-up-call?")
hours_to_wait = int(str_hours_to_wait)

hours = current_time + hours_to_wait

wake-up-call_time = hours % 24

print ("The wake-up-call will go off at:  ", wake-up-call_time)
