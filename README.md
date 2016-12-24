### targeter

Use regex to select files from a folder.

Example file tree:

    some/dir/
    ├── subdir1
    │   ├── config_bar.xml
    │   └── config_foo.xml
    ├── testfile_bar_0.txt
    ├── testfile_bar_1.txt
    ├── testfile_foo_0.txt
    └── testfile_foo_1.txt

    from targeter import acquire
    rootpath = '/path/to/some/dir'

    acquire(rootpath, '.*foo.*')
    # => ['/path/to/some/dir/testfile_foo_0.txt',
    #     '/path/to/some/dir/testfile_foo_1.txt']

    acquire(rootpath, '.*foo.*', depth=2)
    # => ['/path/to/some/dir/testfile_foo_0.txt',
    #     '/path/to/some/dir/testfile_foo_1.txt',
    #     '/path/to/some/dir/subdir1/config_foo.xml']

