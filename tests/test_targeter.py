from targeter import acquire
from targeter.targeter import _walk
from os.path import dirname, realpath, join
from nose.tools import assert_equal


test_path = dirname(realpath(__file__))
rootpath = join(test_path, 'assets')


def test_walk():
    names = ['testfile_foo_0.txt', 'testfile_foo_1.txt',
             'testfile_bar_0.txt', 'testfile_bar_1.txt']
    correct = sorted_rootpath_join(names)
    assert_equal(sorted(_walk(rootpath, 1)), correct)

def test_walk_depth2():
    names = ['testfile_foo_0.txt', 'testfile_foo_1.txt',
             'testfile_bar_0.txt', 'testfile_bar_1.txt',
             'subdir1/config_foo.xml', 'subdir1/config_bar.xml']
    correct = sorted_rootpath_join(names)
    assert_equal(sorted(_walk(rootpath, 2)), correct)


def check_acquire(names, pattern, depth):
    correct = sorted_rootpath_join(names)
    res = acquire(rootpath, pattern, depth) 
    assert_equal(sorted(res), correct)


def test_acquire_depth1():
    names = ['testfile_foo_0.txt', 'testfile_foo_1.txt']
    pattern = '.*_foo_.*'
    yield check_acquire, names, pattern, 1

def test_acquire_depth2():
    names = ['testfile_foo_0.txt', 'testfile_foo_1.txt', 
             'subdir1/config_foo.xml']
    pattern = '.*_foo.*'
    yield check_acquire, names, pattern, 2

def test_acquire_depth2_bar():
    names = ['testfile_bar_0.txt', 'testfile_bar_1.txt', 
             'subdir1/config_bar.xml']
    pattern = '.*_bar.*'
    yield check_acquire, names, pattern, 2


def sorted_rootpath_join(names):
    return sorted([join(rootpath, x) for x in names])
