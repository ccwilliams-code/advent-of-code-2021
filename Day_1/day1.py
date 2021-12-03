# Author: Charlie Williams
"""Day 1 of Advent of Code: Sonar Sweep"""
from pprint import pprint

increases = 0
data = []

# Read the data
with open("input.txt") as f:
    for each in f.readlines():
        data.append(int(each.strip()))

pprint(f"DATA={data}")

x = 1
while x < len(data):
    print(f"{data[x]} >? {data[x - 1]}")
    if data[x] > data[x - 1]:
        increases += 1
    x += 1

print(increases)
