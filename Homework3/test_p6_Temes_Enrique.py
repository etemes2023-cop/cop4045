import unittest

from p6_Temes_Enrique import Entry, File, Folder, find_large_files


class FindLargeFilesTests(unittest.TestCase):
    def test_file_meeting_threshold_is_returned(self):
        file = File("report.txt", 100)

        self.assertEqual(find_large_files(file, 100), [file])

    def test_file_below_threshold_is_not_returned(self):
        file = File("report.txt", 99)

        self.assertEqual(find_large_files(file, 100), [])

    def test_folder_searches_nested_folders_and_includes_threshold(self):
        root = Folder("root")
        nested = Folder("nested", root)
        small = File("small.bin", 9, root)
        exact = File("exact.bin", 10, nested)
        large = File("large.bin", 20, nested)
        root.add(small)
        root.add(nested)
        nested.add(exact)
        nested.add(large)

        self.assertEqual(find_large_files(root, 10), [exact, large])

    def test_empty_folder_returns_no_files(self):
        self.assertEqual(find_large_files(Folder("empty"), 1), [])


class AbsolutePathTests(unittest.TestCase):
    def test_root_path_contains_only_root(self):
        root = Folder("root")

        self.assertEqual(root.absolute_path(), [root])

    def test_nested_path_starts_at_entry_and_ends_at_root(self):
        root = Folder("root")
        subfolder = Folder("subfolder", root)
        file = File("document.txt", 5, subfolder)

        self.assertEqual(file.absolute_path(), [file, subfolder, root])
        self.assertIs(file.parent(), subfolder)

    def test_parentless_file_path_contains_only_file(self):
        file = File("standalone.txt", 5)

        self.assertEqual(file.absolute_path(), [file])


if __name__ == "__main__":
    unittest.main()
