import sys

all_dirs = set()

class ElfFile:
     def __init__(self, parent: 'ElfFile', name: str, is_dir: bool, size: int = 0):
          self.parent = parent
          self.name = name
          self.is_dir = is_dir
          self.file_size = size

          self.children = dict()

          if self.is_dir:
               global all_dirs
               all_dirs.add(self)

          if self.parent:
               self.parent.add_child(self)

     def add_child(self, child: 'ElfFile'):
          if child.name in self.children:
               raise ValueError()
          
          self.children[child.name] = child

     def get_or_make_child(self, name: str, is_dir: bool, size: int = 0) -> 'ElfFile':
          if name in self.children:
               return self.children[name]
          
          return ElfFile(self, name, is_dir, size)

     def size(self) -> int:
          if not self.is_dir:
               return self.file_size
          
          sz = 0
          for child in self.children.values():
               sz += child.size()
          
          return sz

def setup():
     pass

def part1(filename):
     root_dir = ElfFile(None, '/', True)
     current_dir = root_dir
     with open(filename) as f:
          # Throw away the first '$ cd /'
          f.readline()

          for line in f:
               line = line.strip()
               # Handle cd ..
               if line == '$ cd ..':
                    current_dir = current_dir.parent
                    continue

               # Handle cd to a subdirectory
               if line.startswith('$ cd'):
                    subdir_name = line[5:]
                    current_dir = current_dir.get_or_make_child(subdir_name, True)
                    continue
               
               # Handle ls
               if line == '$ ls':
                    continue

               # Every other case is a directory listing, so handle that.
               size, name = line.split()
               current_dir.get_or_make_child(
                    name,
                    size == 'dir',
                    int(size) if size != 'dir' else 0
               )

     small_dir_sizes = 0
     for dir in all_dirs:
          sz = dir.size()
          if sz < 100000:
               small_dir_sizes += sz

     print(small_dir_sizes)

def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
