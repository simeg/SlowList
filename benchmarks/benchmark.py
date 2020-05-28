import os
import sys
import inspect

# Fix import mess
current_dir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from SlowList import SlowList  # noqa

N = 10_000

# Create a list of 100 ints
_100_ints = [0]
for n in range(98):
    _100_ints.append(1)
_100_ints.append(99)

# Create a list of 100 strings
_100_strings = ["first"]
for n in range(98):
    _100_strings.append("e")
_100_strings.append("last")


class Constructor_String(object):
    def slow_list(self):
        for _ in range(N):
            SlowList(*_100_strings)

    def native(self):
        for _x in range(N):
            _ = [*_100_strings]


class Constructor_Integer(object):
    def slow_list(self):
        for _ in range(N):
            SlowList(*_100_ints)

    def native(self):
        for _x in range(N):
            _ = [*_100_ints]


class Constructor_Of_String(object):
    def slow_list(self):
        for _ in range(N):
            SlowList.of(*_100_strings)

    def native(self):
        for _x in range(N):
            _ = [*_100_strings]


class Constructor_Of_Integer(object):
    def slow_list(self):
        for _ in range(N):
            SlowList.of(*_100_ints)

    def native(self):
        for _x in range(N):
            _ = [*_100_ints]


class Add_Integer(object):
    def slow_list(self):
        slow_list = SlowList()
        for x in range(N):
            slow_list.add(x)

    def native(self):
        list = []
        for x in range(N):
            list.append(x)


class Add_String(object):
    def slow_list(self):
        slow_list = SlowList()
        for x in range(N):
            slow_list.add(str(x))

    def native(self):
        list = []
        for x in range(N):
            list.append(str(x))


class Add_At_String(object):
    def slow_list(self):
        slow_list = SlowList("e1", "e2", "e3", "e4")
        for _ in range(N):
            slow_list.add_at(3, "string")

    def native(self):
        list = ["e1", "e2", "e3", "e4"]
        for _ in range(N):
            list.insert(3, "string")


class Add_At_Integer(object):
    def slow_list(self):
        slow_list = SlowList(1, 2, 3, 4, 5)
        for _ in range(N):
            slow_list.add_at(3, 9)

    def native(self):
        list = [1, 2, 3, 4, 5]
        for _ in range(N):
            list.insert(3, 9)


class Contains_String(object):
    def slow_list(self):
        slow_list = SlowList("e1", "e2", "e3", "e4")
        for _ in range(N):
            slow_list.contains("999999")

    def native(self):
        list = ["e1", "e2", "e3", "e4"]
        for _ in range(N):
            if "999" in list:
                raise RuntimeError("Should never end up here")


class Contains_Integer(object):
    def slow_list(self):
        slow_list = SlowList(1, 2, 3, 4)
        for _ in range(N):
            slow_list.contains(9)

    def native(self):
        list = [1, 2, 3, 4]
        for _ in range(N):
            if 9 in list:
                raise RuntimeError("Should never end up here")


class Get(object):
    def slow_list(self):
        slow_list = SlowList(*_100_ints)
        for _ in range(N):
            slow_list.get(99)

    def native(self):
        list = [*_100_ints]
        for _ in range(N):
            _ = list[99]


class Index_Of_String(object):
    def slow_list(self):
        slow_list = SlowList(*_100_strings)
        for _ in range(N):
            slow_list.index_of("last")

    def native(self):
        list = [*_100_strings]
        for _ in range(N):
            list.index("last")


class Index_Of_Integer(object):
    def slow_list(self):
        slow_list = SlowList(*_100_ints)
        for _ in range(N):
            slow_list.index_of(99)

    def native(self):
        list = [*_100_ints]
        for _ in range(N):
            list.index(99)


class Last_Index_Of_String(object):
    def slow_list(self):
        slow_list = SlowList(*_100_strings)
        for _ in range(N):
            slow_list.last_index_of("e")

    def native(self):
        list = [*_100_strings]
        for _ in range(N):
            # This is how to do last index of apparently
            len(list) - 1 - list[::-1].index("e")


class Last_Index_Of_Integer(object):
    def slow_list(self):
        slow_list = SlowList(*_100_ints)
        for _ in range(N):
            slow_list.last_index_of(1)

    def native(self):
        list = [*_100_ints]
        for _ in range(N):
            # This is how to do last index of apparently
            len(list) - 1 - list[::-1].index(1)


class Remove_String(object):
    def slow_list(self):
        for _ in range(N):
            slow_list = SlowList(*_100_strings)
            slow_list.remove("last")

    def native(self):
        for _ in range(N):
            list = [*_100_strings]
            list.remove("last")


class Remove_Integer(object):
    def slow_list(self):
        for _ in range(N):
            slow_list = SlowList(*_100_ints)
            slow_list.remove(99)

    def native(self):
        for _ in range(N):
            list = [*_100_ints]
            list.remove(99)


class Remove_At_String(object):
    def slow_list(self):
        for _ in range(N):
            slow_list = SlowList(*_100_strings)
            slow_list.remove_at(99)

    def native(self):
        for _ in range(N):
            listt = [*_100_strings]
            del listt[99]


class Remove_At_Integer(object):
    def slow_list(self):
        for _ in range(N):
            slow_list = SlowList(*_100_ints)
            slow_list.remove_at(99)

    def native(self):
        for _ in range(N):
            list = [*_100_ints]
            del list[99]


class Size_String(object):
    def slow_list(self):
        slow_list = SlowList(*_100_strings)
        for _ in range(N):
            slow_list.size()

    def native(self):
        list = [*_100_strings]
        for _ in range(N):
            len(list)


class Size_Integer(object):
    def slow_list(self):
        slow_list = SlowList(*_100_ints)
        for _ in range(N):
            slow_list.size()

    def native(self):
        list = [*_100_ints]
        for _ in range(N):
            len(list)


class Set_String(object):
    def slow_list(self):
        slow_list = SlowList(*_100_strings)
        for _ in range(N):
            slow_list.set(99, 99)

    def native(self):
        list = [*_100_strings]
        for _ in range(N):
            list[99] = 99


class Set_Integer(object):
    def slow_list(self):
        slow_list = SlowList(*_100_ints)
        for _ in range(N):
            slow_list.set(99, 99)

    def native(self):
        list = [*_100_ints]
        for _ in range(N):
            list[99] = 99


class To_String_String(object):
    def slow_list(self):
        slow_list = SlowList(*_100_strings)
        for _ in range(N):
            slow_list.to_string()

    def native(self):
        list = [*_100_strings]
        for _ in range(N):
            ''.join(list)


class To_String_Integer(object):
    def slow_list(self):
        slow_list = SlowList(*_100_ints)
        for _ in range(N):
            slow_list.to_string()

    def native(self):
        list = [*_100_ints]
        for _ in range(N):
            ''.join(str(e) for e in list)


if __name__ == "__main__":
    from timeit import timeit

    DEFAULT_NUMBER = 1
    functions = [
        ("Constructor_String", "constructor",
         "new instance with 100 strings", N),
        ("Constructor_Integer", "constructor",
         "new instance with 100 ints", N),
        ("Constructor_Of_String", "constructor",
         "new instance using of() with 100 strings", N),
        ("Constructor_Of_Integer", "constructor",
         "new instance using of() with 100 ints", N),
        ("Add_Integer", "add", "add strings to list", N),
        ("Add_String", "add", "add ints to list", N),
        ("Add_At_String", "add_at", "add_at fixed position with string", N),
        ("Add_At_Integer", "add_at", "add_at fixed position with int", N),
        ("Contains_String", "contains", "contains with string", N),
        ("Contains_Integer", "contains", "contains with int", N),
        ("Get", "get", "get last element of list of size 100", N),
        ("Index_Of_String", "index_of",
         "index_of last string in list of size 100", N),
        ("Index_Of_Integer", "index_of",
         "index_of last int in list of size 100", N),
        ("Last_Index_Of_String", "last_index_of",
         "last_index_of las string in list of size 100", N),
        ("Last_Index_Of_Integer", "last_index_of",
         "last_index_of last int in list of size 100", N),
        ("Remove_String", "remove",
         "remove last string in list of size 100", N),
        ("Remove_Integer", "remove",
         "remove last string in list of size 100", N),
        ("Remove_At_String", "remove_at",
         "remove_at last int in list of size 100", N),
        ("Size_String", "size", "size with string list of size 100", N),
        ("Size_Integer", "size", "size with int list of size 100", N),
        ("Set_String", "set", "set last string in list of size 100", N),
        ("Set_Integer", "set", "set last int in list of size 100", N),
        ("To_String_String", "to_string",
         "to_string string list of size 100", N),
        ("To_String_Integer", "to_string",
         "to_string int list of size 100", N),
    ]

    print("{:10}\t{:16}\t{:50}\t{:8}\t{}".format("List", "Function",
                                                 "Description", "N",
                                                 "Result"))
    for (clazz, fn, description, n) in functions:
        setup = "from __main__ import {}".format(clazz)

        # Benchmark slow list
        stmnt_slow_list = "{}().slow_list()".format(clazz)
        time_slow_list_s = timeit(stmt=stmnt_slow_list, setup=setup,
                                  number=DEFAULT_NUMBER)

        # Benchmark native list
        stmnt_native = "{}().native()".format(clazz)
        time_native_s = timeit(stmt=stmnt_native, setup=setup,
                               number=DEFAULT_NUMBER)

        # Convert to milliseconds
        time_native_ms = (round(time_native_s, ndigits=5) * 1000)
        time_slow_list_ms = (round(time_slow_list_s, ndigits=5) * 1000)

        # Truncate to only two decimals
        time_slow_list = f"{time_slow_list_ms:.2f}"
        time_native = f"{time_native_ms:.2f}"

        print(''.join('-' for _ in range(102)))
        print("{:10}\t{:16}\t{:50}\t{:8}\t{}ms".format("Native", fn,
                                                       description, n,
                                                       time_native))
        print("{:10}\t{:16}\t{:50}\t{:8}\t{}ms".format("SlowList", fn,
                                                       description, n,
                                                       time_slow_list))
