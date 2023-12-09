import sys
import re

from multiprocessing import Pool


part1_seeds = list(map(int, re.findall(r'\d+', sys.stdin.readline())))

lines = list(filter(None,map(str.strip,sys.stdin.readlines())))

stsi = lines.index('seed-to-soil map:')
stfi = lines.index('soil-to-fertilizer map:')
ftwi = lines.index('fertilizer-to-water map:')
wtli = lines.index('water-to-light map:')
ltti = lines.index('light-to-temperature map:')
tthi = lines.index('temperature-to-humidity map:')
htli = lines.index('humidity-to-location map:')

def get_new_num(n, ranges):
    for sr, er, v in ranges:
        if sr > n:
            break
        if n >= sr and n < er:
            return n + v
    return n

def map_nums(lines, previous_nums):
    ranges = []

    for line in lines:
        dr, sr, rl = list(map(int, re.findall(r'\d+', line)))

        ranges.append((sr,sr+rl,dr-sr))

    for p in previous_nums:
        yield get_new_num(p, sorted(ranges, key=lambda t: t[0]))

def get_locations(initial_seeds):
    soils = map_nums(lines[stsi+1:stfi], initial_seeds)

    fertilizers = map_nums(lines[stfi+1:ftwi], soils)

    waters = map_nums(lines[ftwi+1:wtli], fertilizers)

    lights = map_nums(lines[wtli+1:ltti], waters)

    temperatures = map_nums(lines[ltti+1:tthi], lights)

    humidities = map_nums(lines[tthi+1:htli], temperatures)

    locations = map_nums(lines[htli+1:], humidities)

    return min(locations)

def part2():
    with Pool(10) as p:
        ranges = [range(part1_seeds[i], part1_seeds[i]+part1_seeds[i+1]) for i in range(0, len(part1_seeds), 2)]
        result = p.map(get_locations, ranges)

    print(min(result))

print(get_locations(part1_seeds))

part2()
