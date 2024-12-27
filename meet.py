#  File: Meet.py

#  Description: Determine earlist meet time interval for two people

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

def earliestPossibleMeeting(person1, person2, duration):
	available_time = []
	new_person1 = range_of_duration(person1, duration)
	new_person2 = range_of_duration(person2, duration)

	for time in new_person2:
		for num in time:
			for i in new_person1:
				if num in i:
					available_time.append(num)
	if available_time != []:
		available_time = [available_time[0], available_time[0] + duration]
		return available_time
	return available_time

def person_free_days(person, duration):
	new_person = []

	for time in person:
		if time[1] - time[0] >= duration:
			new_person.append(time)

	return new_person

def range_of_duration(person, duration):
	person_times = person_free_days(person, duration)
	range_duration = []

	for time in person_times:
		new_list = time
		count = time[0] + 1
		while count < time[1]:
			new_list.append(count)
			count += 1
		new_list.sort()
		range_duration.append(new_list)
	
	return range_duration



def main():
    #test_cases()

	# read the input data and create a list of lists for each person
	f = sys.stdin
	# read in the duration
	dur = int(f.readline().strip())
	# person 1's number of avalible slots
	num1 = int(f.readline().strip())
	p1 = []
	for x in range(num1):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p1.append(tmp)

	# person 2's number of avalible slots
	num2 = int(f.readline().strip())
	p2 = []
	for x in range(num2):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p2.append(tmp)

	print(earliestPossibleMeeting(p1,p2,dur))

if __name__ == "__main__":
  main()
