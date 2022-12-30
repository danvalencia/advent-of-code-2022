import pathlib as p
import re

class FileSystem:
	def __init__(self):
		self.root = Dir("/")
	
	def get_root(self):
		return self.root

	def print_fs(self):
		self.root.print()

	def get_size(self):
		return self.root.get_size()
	
class Dir:
	def __init__(self, name, parent=None):
		self.name = name
		self.children = {} 
		self.parent = parent

	def get_size(self):
		_size = 0
		for child in self.children.values():
			_size += child.get_size()
		return _size
	
	def mk_dir(self, dir_name):
		d=Dir(dir_name, self)
		if dir_name in self.children:
			d = self.children[dir_name]
		else:
			self.children[dir_name] = d
		return d

	def create_file(self, file_name, file_size):
		f = File(file_name, file_size, self)
		if file_name in self.children:
			f = self.children[file_name]
		else:
			self.children[file_name] = f
		return f

	def get_name(self):
		if self.parent:
			if self.parent.get_name() == "/":
				return "/" + self.name
			else:
				return self.parent.get_name() + "/" + self.name
		return ""

	def get_children(self):
		return self.children
	
	def print(self):
		print(self.get_name())
		print('--')
		for child in self.children.values():
			child.print()

	def __str__(self) -> str:
		return self.get_name()

class File:
	def __init__(self, name, size, parent_dir):
		self.name = name
		self.size = size
		self.parent = parent_dir

	def get_size(self):
		return self.size
	
	def get_name(self):
		return self.name
	
	def get_abs_name(self):
		return self.parent.get_name + "/" + self.name

	def print(self):
		print(self.get_name() + " - " + str(self.size))

class Session:
	def __init__(self, file_system: FileSystem):
		self.file_system = file_system
		self.cwd = file_system.get_root()

	def get_fs(self):
		return self.file_system

	def get_cwd(self):
		return self.cwd

	def change_dir(self, new_dir):
		if new_dir == '..':
			# Handle move up
			if not self.cwd.parent:
				print("We're already in root, can't go up further with cd ..")
			else:
				self.cwd = self.cwd.parent
		else:
			if new_dir == '/':
				self.cwd = self.file_system.get_root()
			else:
				sub_dir = self.find_sub_dir(new_dir)
				if sub_dir:
					self.cwd = sub_dir
				else:
					raise Exception("Directory " + str(sub_dir) + " does not exist inside dir: " + self.cwd.name)
	
	def find_sub_dir(self, sub_dir):
		for child in self.cwd.children.values():
			if isinstance(child, Dir) and child.name == sub_dir:
				return child
		return None

	def find_dir_size_by_max_size(self, max_size):
		return self.dfs(self.file_system.get_root(), max_size)
		
	def dfs(self, node, max_size):
		if isinstance(node, Dir):
			s = 0
			if node.get_size() <= max_size:
				s += node.get_size()
			for n in node.get_children().values():
				s += self.dfs(n, max_size)
			return s

		return 0


	def create_file(self, file_name, file_size):
		self.cwd.create_file(file_name, file_size)
	
	def mk_dir(self, dir_name):
		return self.cwd.mk_dir(dir_name)

fs = FileSystem()
# fs.get_root().mk_dir("foo").mk_dir("bar").mk_dir("baz")

session = Session(fs)

curr_command = None
with open(p.Path(__file__).parent.joinpath('input.txt'), 'r') as file:
	for line in file:
		if line.startswith('$ cd '):
			curr_command = 'cd'
			session.change_dir(line.strip()[5:])
		elif line.startswith('$ ls'):
			curr_command = 'ls'
		elif m := re.match(r"(\d+) (.*)", line):
			regex_groups = m.groups()
			file_size = int(regex_groups[0])
			file_name = regex_groups[1]
			session.create_file(file_name, file_size)
		elif m := re.match(r"dir (.*)", line):
			regex_groups = m.groups()
			dir_name = regex_groups[0]
			session.mk_dir(dir_name)
		
fs.print_fs()

print("Total size: " + str(fs.get_size()))
print("Dir size by max size: " + str(session.find_dir_size_by_max_size(100000)))
print("CWD: " + str(session.get_cwd()))