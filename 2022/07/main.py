import sys

from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str

_, *lines = list(map(str.strip,open(sys.argv[1]).readlines()))

root_path = 'home'
directories = {'home': []}

for line in lines:
    match line.split():
        case ['$', 'ls']:
            continue
        case ['$', 'cd', '..']:
            root_path = '/'.join(root_path.split('/')[:-1])
        case ['$', 'cd', dir_name]:
            root_path += '/' + dir_name
            directories[root_path] = []
        case ["dir", dir_name]:
            directories[root_path].append(Directory(root_path + '/' + dir_name))
        case [size, name]:
            directories[root_path].append(File(root_path + '/' + name, int(size)))
        case _:
            print("Did not match:", line)

def get_directory_size(dir_path):
    stack = [dir_path]
    total = 0

    while len(stack) > 0:
        current = stack.pop(0)

        match current:
            case Directory(path):
                stack.extend(directories[path])
            case File(_, size):
                total += size
    return total

directories_size = {}

for directory_path in directories.keys():
    directories_size[directory_path] = get_directory_size(Directory(directory_path))

print(sum(filter(lambda size: size < 100_000, directories_size.values())))

file_system_size = 70_000_000
required_space   = 30_000_000
occupied_space   = max(directories_size.values())
free_space       = file_system_size - occupied_space
space_needed     = required_space - free_space

print(sorted(filter(lambda size: size > space_needed, directories_size.values()))[0])
