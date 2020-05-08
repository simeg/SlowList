class SlowList(object):
    """
    A simple list type. Stores all elements in a single String. SlowList is
    heterogeneous, meaning you can store data of different types in a single
    list.
    """

    __list: str = ""
    __delimiter: str = ","

    def __init__(self, *args: object):
        """Constructor with optional arguments.

        Returns:
            object: instance of SlowList

        """
        self.clear()
        if len(args) > 0:
            for arg in args:
                self.add(arg)

    def add(self, element: object) -> None:
        """Appends the specified element to the end of this list.

        Args:
            element (object): element to be appended to this list

        """
        e = self.__type(element)

        if self.is_empty():
            self.__list = e
        else:
            self.__list += "{}{}".format(self.__delimiter, e)

    def add_at(self, index: int, element: object) -> None:
        """Inserts the specified element at the specified position in this
        list.

        Args:
            index (int): index at which the specified element is to be inserted
            element (object): element to be appended to this list

        Raises:
            IndexError: if the index is out of range

        """
        if index > self.size() or index < 0:
            raise IndexError("Index out of bounds")

        e = self.__type(element)

        # If index 0 then put in front
        if index == 0:
            self.__list = "{}{}{}".format(e, self.__delimiter,
                                          self.__list)
        elif index == self.size():  # If end of list
            self.add(element)
        else:
            count = 1
            prev = 0
            while True:
                current = self.__list.index(self.__delimiter, prev + 1)
                if count == index:
                    pre = self.__list[:current]
                    post = self.__list[current:]
                    new_element = "{}{}".format(self.__delimiter, e)
                    self.__list = "{}{}{}".format(pre, new_element, post)
                    return
                else:
                    prev = current
                    count += 1

    def clear(self) -> None:
        """Removes all of the elements from this list.

        """
        self.__list = ""

    def contains(self, element: object) -> bool:
        """Returns true if this list contains the specified element.

        More formally, returns true if and only if this list contains at least
        one element e such that `element == e`.

        Args:
            element (object): element whose presence in this list is to be
                tested

        Returns:
            bool: true if this list contains the specified element

        """
        e = self.__type(element)

        for i in range(self.size()):
            if self.get(i) == e:
                return True
        return False

    def get(self, index: int) -> object:
        """Returns the element at the specified position in this list.

        Args:
            index (int): index of the element to return

        Returns:
            int: the element at the specified position in this list

        Raises:
            IndexError: if the index is out of range

        """
        if self.is_empty() or index < 0:
            raise IndexError("Index out of bounds")

        if index > 0 and index >= self.size():
            raise IndexError("Index out of bounds")

        # If first element is requested and size is 1
        if self.size() == 1 and index == 0:
            return self.__list

        count = 0
        for e in self.__list.split(self.__delimiter):
            if index == count:
                return e
            count += 1

    def index_of(self, element: object) -> int:
        """Returns the index of the first occurrence of the specified element
        in this list, or -1 if this list does not contain the element.

        More formally, returns the lowest index i such that
        `element == get(i)`, or -1 if there is no such index.

        Args:
            element (object): element to search for

        Returns:
            int: the index of the first occurrence of the specified element in
                this list, or -1 if this list does not contain the element

        """
        e = self.__type(element)

        for i in range(self.size()):
            if self.get(i) == e:
                return i

        return -1

    def is_empty(self) -> bool:
        """Returns true if this list contains no elements.

        Returns:
            bool: true if this list contains no elements

        """
        return self.__list == ""

    def last_index_of(self, element: object) -> int:
        """Returns the index of the last occurrence of the specified element in
        this list, or -1 if this list does not contain the element.

        More formally, returns the highest index i such that
        `element == get(i)`, or -1 if there is no such index.

        Args:
            element (object): element to search for

        Returns:
            int: the index of the last occurrence of the specified element in
                this list, or -1 if this list does not contain the element

        """
        e = self.__type(element)

        for i in reversed(range(self.size())):
            if self.get(i) == e:
                return i

        return -1

    @classmethod
    def of(cls, *args: object):
        """Constructor with optional arguments.

        Returns:
            object: instance of SlowList

        """
        return cls(*args)

    def remove(self, element: object) -> bool:
        """Removes the first occurrence of the specified element from this
        list, if it is present.

        If this list does not contain the element, it is unchanged. More
        formally, removes the element with the lowest index i such that
        `element == get(i)` (if such an element exists). Returns true if this
        list contained the specified element (or equivalently, if this list
        changed as a result of the call).

        Args:
            element (object): element to be removed from this list, if present

        Returns:
            bool: true if this list contained the specified element

        """
        e = self.__type(element)

        for i in range(self.size()):
            if self.get(i) == e:
                __ = self.remove_at(i)
                return True

        return False

    def remove_at(self, index: int) -> object:
        """Removes the element at the specified position in this list.

        Shifts any subsequent elements to the left (subtracts one from their
        indices). Returns the element that was removed from the list.

        Args:
            index (int): the index of the element to be removed

        Returns:
            object: the element previously at the specified position

        Raises:
            IndexError: if the index is out of range

        """
        if self.is_empty() or index >= self.size():
            raise IndexError("Index out of bounds")

        # (Optimization) If only one element and index is 0
        if self.size() == 1 and index == 0:
            e = self.get(0)
            self.clear()
            return e

        if index == 0:
            first_delimiter = self.__list.index(self.__delimiter, 0)
            # Get list except first element
            post = self.__list[first_delimiter + 1:]
            # Get replaced element before modifying list
            replaced_element = self.__list[:first_delimiter]

            # Construct new list
            self.__list = "{}".format(post)

            return replaced_element

        count = 1
        prev = 0
        while True:
            current = self.__list.index(self.__delimiter, prev + 1)
            if count == index:
                # Get the list before index
                pre = self.__list[:current]

                # Get the list after index
                try:
                    next_delimiter = self.__list.index(self.__delimiter,
                                                       current + 1)
                    post = self.__list[next_delimiter:]
                except ValueError:
                    # If last element
                    next_delimiter = len(self.__list)
                    post = ""

                # Get replaced element
                replaced_element = self.__list[current + 1:next_delimiter]

                # Construct new list
                self.__list = "{}{}".format(pre, post)

                return replaced_element
            prev = current
            count += 1

    def size(self):
        """Returns the number of elements in this list.

        Returns:
            int: the number of elements in this list

        """
        if self.is_empty():
            return 0
        return self.__list.count(self.__delimiter) + 1

    def set(self, index: int, element: object) -> object:
        """Replaces the element at the specified position in this list with the
        specified element.

        Args:
            index: index of the element to replace
            element: element to be stored at the specified position

        Returns:
            object: the element previously at the specified position

        Raises:
            IndexError: if the index is out of range

        """
        if self.is_empty() or index >= self.size():
            raise IndexError("Index out of bounds")

        e = self.__type(element)

        # (Optimization) If only one element and index is 0
        if self.size() == 1 and index == 0:
            replaced_element = self.remove_at(0)
            self.add(element)
            return replaced_element

        # If first element in list
        if index == 0:
            first_delimiter = self.__list.index(self.__delimiter, 0)
            # Get list except first element
            post = self.__list[first_delimiter:]
            # Get replaced element before modifying list
            replaced_element = self.get(0)

            # Construct new list
            self.__list = "{}{}".format(e, post)

            return replaced_element

        count = 1
        prev = 0
        while True:
            current = self.__list.index(self.__delimiter, prev + 1)
            if count == index:
                # Get the list before index
                pre = self.__list[:current]

                # Get the list after index
                try:
                    next_delimiter = self.__list.index(self.__delimiter,
                                                       current + 1)
                    post = self.__list[next_delimiter:]
                except ValueError:
                    # If last element
                    next_delimiter = len(self.__list)
                    post = ""

                # Get replaced element
                replaced_element = self.__list[current + 1:next_delimiter]

                # Construct new list
                new_element = "{}{}".format(self.__delimiter, e)
                self.__list = "{}{}{}".format(pre, new_element, post)

                return replaced_element
            prev = current
            count += 1

    def to_string(self) -> str:
        """Returns a string representation of the object.

        Returns:
            str: a string representation of the object

        """
        if self.is_empty():
            return ""

        list = self.__list
        # Insert whitespace between elements
        formatted_elements = list.replace(self.__delimiter,
                                          "{}{}".format(self.__delimiter, " "))
        return "[{}]".format(formatted_elements)

    def __type(self, var: object) -> str:
        """Returns the internal representation depending on the type.

        For String it will return:
            '99'
        For Integer it will return:
            99

        Args:
            var (object): variable to convert

        Returns:
            str: internal representation of type

        Raises:
            TypeError: if data type not supported

        """
        if self.__is_int(var):
            return str(var)
        elif self.__is_string(var):
            return "'{}'".format(var)
        else:
            raise TypeError("Datatype not supported")

    @staticmethod
    def __is_int(var: object) -> bool:
        """Returns whether the variable is a valid Integer or not.

        Args:
            var (object): variable to check

        Returns:
            bool: whether the variable is a valid Integer or not

        """
        return isinstance(var, int)

    @staticmethod
    def __is_string(var: object) -> bool:
        """Returns whether the variable is a valid String or not.

        Args:
            var (object): variable to check

        Returns:
            bool: whether the variable is a valid String or not

        """
        return isinstance(var, str)
