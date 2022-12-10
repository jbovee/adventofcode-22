get_input = lambda filename: [l.strip('\n') for l in open(filename,'r+',encoding='utf-8').readlines()]

class Directory:
    def __init__(self,name,parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = []
        self.files = []
    
    def add_sub_dir(self,name):
        if not self.sub_dir_exists(name):
            subdir = Directory(name,self)
            self.subdirs.append(subdir)

    def add_file(self,name,size):
        newfile = File(name,size)
        self.files.append(newfile)
    
    def sub_dir_exists(self,name):
        if name in [dir.name for dir in self.subdirs]:
            return True
        return False
    
    def get_sub_dir(self,name):
        if self.sub_dir_exists(name):
            return list(filter(lambda d: d.name == name, self.subdirs))[0]
        raise Exception('{} directory has no sub directory {}'.format(self.name,name))
    
    def get_root_dir(self):
        while self.parent is not None:
            self = self.parent
        return self

    def get_total_size(self):
        total = 0
        for f in self.files:
            total += f.size
        if len(self.subdirs) > 0:
            total += sum([subdir.get_total_size() for subdir in self.subdirs])
        return total
    
    def get_dir_sizes(self):
        dirSizes = []
        dirSizes.append(self.get_total_size())
        for subdir in self.subdirs:
            dirSizes += subdir.get_dir_sizes()
        return dirSizes
    
    def solution(self):
        total = 0
        if self.get_total_size() < 100000:
            total += self.get_total_size()
        total += sum([subdir.solution() for subdir in self.subdirs])
        return total

class File:
    def __init__(self,name,size):
        self.name = name
        self.size = int(size)

def main():
    data = get_input('input')
    # populate root directory with input
    cwd = Directory('/')
    for i in range(len(data)):
        cmd = data[i].split()
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == '/':
                    cwd = cwd.get_root_dir()
                elif cmd[2] == '..':
                    cwd = cwd.parent
                else:
                    cwd.add_sub_dir(cmd[2])
                    cwd = cwd.get_sub_dir(cmd[2])
            elif cmd[1] == 'ls':
                # nothing to do really
                pass
        elif cmd[0] == 'dir': 
            cwd.add_sub_dir(cmd[1])
        else:
            filesize,filename = cmd[0],cmd[1]
            cwd.add_file(filename,filesize)
    cwd = cwd.get_root_dir()
    print('Total of dirs <= 100000: {}'.format(cwd.solution()))

    totalUsed = cwd.get_total_size()
    toFree = 30000000 - (70000000 - totalUsed)
    allDirSizes = cwd.get_dir_sizes()
    smallest = list(filter(lambda x: x > toFree,sorted(allDirSizes)))[0]
    print('Smallest dir to make space: {}'.format(smallest))

if __name__ == '__main__':
    main()