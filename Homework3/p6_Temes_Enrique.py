class Entry:
    def __init__(self, name: str, parent: "Entry | None" = None):
        self.name = name
        self._parent = parent

    def parent(self) -> "Entry | None":
        return self._parent

    def absolute_path(self) -> list["Entry"]:
        if self._parent is None:
            return [self]
        return [self] + self._parent.absolute_path()

    def size(self) -> int:
        raise NotImplementedError("Entry subclasses must implement size()")


class File(Entry):
    def __init__(self, name: str, bytes_used: int, parent: Entry | None = None):
        if not isinstance(bytes_used, int) or isinstance(bytes_used, bool) or bytes_used < 0:
            raise ValueError("bytes_used must be a nonnegative integer")
        super().__init__(name, parent)
        self.bytes_used = bytes_used

    def size(self) -> int:
        return self.bytes_used


class Folder(Entry):
    def __init__(self, name: str, parent: Entry | None = None):
        super().__init__(name, parent)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        self._children.append(entry)

    def size(self) -> int:
        return sum(entry.size() for entry in self._children)

    def children(self) -> tuple[Entry, ...]:
        return tuple(self._children)


def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    """Find files at least minimum_size bytes, starting at entry.

    If entry is a File, return it only when its size meets the threshold.
    If entry is a Folder, recursively search all of its descendants.
    """
    if isinstance(entry, File):
        return [entry] if entry.size() >= minimum_size else []

    if isinstance(entry, Folder):
        files = [
            found_file
            for child in entry.children()
            for found_file in find_large_files(child, minimum_size)
        ]
        return sorted(files, key=lambda file: file.size())

    return []


# Part F: demonstrate nested folders, recursive sizes, searches, and paths.
outer = Folder("outer")
middle = Folder("middle", outer)
inner = Folder("inner", middle)
outer.add(middle)
middle.add(inner)

small_file = File("small.txt", 10, outer)
medium_file = File("medium.txt", 25, middle)
large_file = File("large.txt", 50, inner)
outer.add(small_file)
middle.add(medium_file)
inner.add(large_file)

# A single call includes files and all nested-folder contents: 10 + 25 + 50.
assert outer.size() == 85

# At least 25 bytes: medium and large. At least 50 bytes: large only.
print("Z23734170")
print([file.name for file in find_large_files(outer, 25)])
assert find_large_files(outer, 25) == [medium_file, large_file]
assert find_large_files(outer, 50) == [large_file]

# The path starts at the file and follows its parents up to the root.
assert large_file.absolute_path() == [large_file, inner, middle, outer]
print("Part F outer folder size:", outer.size())
print("Part F files at least 25 bytes:", [file.name for file in find_large_files(outer, 25)])
print("Part F files at least 50 bytes:", [file.name for file in find_large_files(outer, 50)])
print("Part F large file absolute path:", [entry.name for entry in large_file.absolute_path()])
