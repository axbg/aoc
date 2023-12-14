# heavily inspired by https://todd.ginsberg.com/post/advent-of-code/2022/day19/

import math
from bisect import insort
from copy import deepcopy


class Robot:
    def __init__(self, type, ore, clay, obsidian):
        self.type = type
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian

    def __str__(self):
        return f"{self.ore} ore, {self.clay} clay, {self.obsidian} obsidian"

    def consume(self, ore, clay, obsidian):
        new_ore = ore - self.ore
        new_clay = clay - self.clay
        new_obsidian = obsidian - self.obsidian

        return [new_ore, new_clay, new_obsidian]

    def compute_time(self, run):
        ore = 0 if run.ore >= self.ore else math.ceil((self.ore - run.ore) / run.ore_robots)
        clay = 0 if run.clay >= self.clay else math.ceil((self.clay - run.clay) / run.clay_robots)
        obsidian = 0 if run.obsidian >= self.obsidian else math.ceil(
            (self.obsidian - run.obsidian) / run.obsidian_robots)

        return max([ore, clay, obsidian]) + 1

    def schedule(self, run):
        time_required = self.compute_time(run)

        run.ore = run.ore - self.ore + time_required * run.ore_robots
        run.clay = run.clay - self.clay + time_required * run.clay_robots
        run.obsidian = run.obsidian - self.obsidian + time_required * run.obsidian_robots
        run.geode = run.geode + time_required * run.geode_robot

        if self.type == 'ore':
            run.ore_robots += 1
        elif self.type == 'clay':
            run.clay_robots += 1
        elif self.type == 'obsidian':
            run.obsidian_robots += 1
        elif self.type == 'geode':
            run.geode_robot += 1

        run.current_cycle += time_required

        return run


class Blueprint:
    def __init__(self, id, ore_robot, clay_robot, obsidian_robot, geode_robot):
        self.id = id
        self.ore_robot = ore_robot
        self.clay_robot = clay_robot
        self.obsidian_robot = obsidian_robot
        self.geode_robot = geode_robot
        self.max_ore = max([self.ore_robot.ore, self.clay_robot.ore, self.obsidian_robot.ore, self.geode_robot.ore])
        self.max_clay = max(
            [self.ore_robot.clay, self.clay_robot.clay, self.obsidian_robot.clay, self.geode_robot.clay])
        self.max_obsidian = max([self.ore_robot.obsidian, self.clay_robot.obsidian, self.obsidian_robot.obsidian,
                                 self.geode_robot.obsidian])

    def print(self):
        print(f"Blueprint {self.id}")
        print(f"  Ore robot: {self.ore_robot}")
        print(f"  Clay robot: {self.clay_robot}")
        print(f"  Obsidian robot: {self.obsidian_robot}")
        print(f"  Geode robot: {self.geode_robot}")
        print("")


class Run:
    def __init__(self, blueprint, current_cycle, cycles, ore, clay, obsidian, geode, ore_r, clay_r, obsidian_r,
                 geode_r):
        self.blueprint = blueprint
        self.cycles = cycles
        self.current_cycle = current_cycle
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode
        self.ore_robots = ore_r
        self.clay_robots = clay_r
        self.obsidian_robots = obsidian_r
        self.geode_robot = geode_r

    def __lt__(self, other):
        return other.geode < self.geode

    def compute_next_runs(self):
        next_states = []

        if self.current_cycle < self.cycles:
            if self.blueprint.max_ore > self.ore_robots and self.ore > 0:
                state = self.blueprint.ore_robot.schedule(deepcopy(self))
                if state.current_cycle <= state.cycles:
                    next_states.append(state)
            if self.blueprint.max_clay > self.clay_robots and self.ore > 0:
                state = self.blueprint.clay_robot.schedule(deepcopy(self))
                if state.current_cycle <= state.cycles:
                    next_states.append(state)
            if self.blueprint.max_obsidian > self.obsidian_robots and self.ore > 0 and self.clay > 0:
                state = self.blueprint.obsidian_robot.schedule(deepcopy(self))
                if state.current_cycle <= state.cycles:
                    next_states.append(state)
            if self.clay > 0 and self.obsidian > 0:
                state = self.blueprint.geode_robot.schedule(deepcopy(self))
                if state.current_cycle <= state.cycles:
                    next_states.append(state)

        return next_states

    def can_become_better(self, best):
        time_left = self.cycles - self.current_cycle

        potential = 0
        for i in range(0, time_left):
            potential = potential + i + self.geode_robot

        return potential + self.geode > best


def generate_robot(line, type):
    ore = 0
    clay = 0
    obsidian = 0

    line = line.strip().split("costs")[1].split("and")

    for element in line:
        if "ore" in element:
            ore = int(element.strip().split(" ")[0])
        elif "clay" in element:
            clay = int(element.strip().split(" ")[0])
        elif "obsidian" in element:
            obsidian = int(element.strip().split(" ")[0])

    return Robot(type, ore, clay, obsidian)


def compute_path(run):
    max_geodes = run.geode

    planned_runs = [run]

    while len(planned_runs) > 0:
        run = planned_runs.pop(0)

        if run.can_become_better(max_geodes):
            if run.geode > max_geodes:
                print(f"New max {run.geode}")

            max_geodes = max(max_geodes, run.geode)

            next_runs = run.compute_next_runs()
            for run in next_runs:
                insort(planned_runs, run)

    return max_geodes


def main():
    rounds = 32
    blueprints = []

    lines = open('inp.txt', 'r').readlines()

    for i in range(0, len(lines), 6):
        id = lines[i].strip().split(":")[0].split(" ")[1]

        blueprints.append(
            Blueprint(int(id), generate_robot(lines[i + 1], 'ore'), generate_robot(lines[i + 2], 'clay'),
                      generate_robot(lines[i + 3], 'obsidian'),
                      generate_robot(lines[i + 4], 'geode')))

    score = 1
    for blueprint in blueprints[:3]:
        score *= compute_path(Run(blueprint, 1, rounds, 1, 0, 0, 0, 1, 0, 0, 0))

    print(f"\nBiggest score for all blueprints is {score}")


if __name__ == "__main__":
    main()
