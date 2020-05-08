class SlowList:
    __list: str = ""
    __delimiter: str = ","

    def __init__(self, *args):
        self.__list = ""
        if len(args) > 0:
            for arg in args:
                self.add(arg)

    @classmethod
    def of(cls, *args):
        return cls(*args)

    def add(self, element):
        e = self.__type(element)

        if self.is_empty():
            self.__list = e
        else:
            self.__list += "{}{}".format(self.__delimiter, e)

    def addAt(self, index, element):
        if index > self.size() or index < 0:
            raise IndexError("Index out of bounds")

        e = self.__type(element)

        # If index 0 then put in front
        if index == 0:
            self.__list = "{}{}{}".format(e, self.__delimiter,
                                          self.__list)
        elif index == self.size():  # If end of list
            self.__list += ",{}".format(e)
        else:
            count = 1
            prev = 0
            should_run = True
            while should_run:
                current = self.__list.index(self.__delimiter, prev + 1)
                if count == index:
                    pre = self.__list[:current]
                    post = self.__list[current:]
                    new_element = "{}{}".format(self.__delimiter, e)
                    self.__list = "{}{}{}".format(pre, new_element, post)
                    should_run = False
                else:
                    prev = current
                    count += 1

    def clear(self):
        self.__list = ""

    def contains(self, element):
        e = self.__type(element)

        for i in range(self.size()):
            if self.get(i) == e:
                return True
        return False

    def get(self, index):
        if self.is_empty() or index < 0:
            raise IndexError("Index out of bounds")

        if index > 0 and index >= self.size():
            raise IndexError("Index out of bounds")

        # If first element is requested and size is 1
        if self.size() == 1 and index == 0:
            return self.__list

        split = self.__list.split(self.__delimiter)
        count = 0
        for e in split:
            if index == count:
                return e
            count += 1

    def index_of(self, element):
        """
        Returns the index of the first occurrence of the specified element in
        this list, or -1 if this list does not contain the element.

        :param element: Any
        :return: Int
        """
        if self.is_empty():
            return -1

        e = self.__type(element)

        index = 0
        for split_e in self.__list.split(self.__delimiter):
            if e == split_e:
                return index
            index += 1

        return -1

    def is_empty(self):
        return self.__list == ""

    def last_index_of(self, element):
        """
        Returns the index of the last occurrence of the specified element in
        this list, or -1 if this list does not contain the element.

        :param element: Any
        :return: Int
        """
        if self.is_empty():
            return -1

        e = self.__type(element)

        index = self.size() - 1
        split = self.__list.split(self.__delimiter)
        for split_e in reversed(split):
            if e == split_e:
                return index
            index -= 1

        return -1

    def remove(self, element):
        """
        Removes and returns the first occurrence of the specified element from
        this list, if it is present.

        :param element: Integer
        :return: Object
        """

        if self.is_empty():
            return False

        e = self.__type(element)

        index = 0
        split = self.__list.split(self.__delimiter)
        for split_e in split:
            if split_e == e:
                __ = self.remove_at(index)
                return True
            index += 1

        return False

    def remove_at(self, index):
        """
        Removes and returns the element at the specified position in this list.

        :param index: Integer
        :return: Object
        """

        if self.is_empty() or index >= self.size():
            raise IndexError("Index out of bounds")

        # (Optimization) If only one element and index is 0
        if self.size() == 1 and index == 0:
            e = self.__list
            self.__list = ""
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
                except Exception:
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
        if self.is_empty():
            return 0
        return self.__list.count(self.__delimiter) + 1

    def set(self, index, element):
        """
        Replaces the element at the specified position in this list with the
        specified element. Returns the replaced element.

        :param index: Int
        :param element: Object
        :return: Object
        """
        if self.is_empty() or index >= self.size():
            raise IndexError("Index out of bounds")

        e = self.__type(element)

        # (Optimization) If only one element and index is 0
        if self.size() == 1 and index == 0:
            elems = self.__list
            self.__list = e
            return elems

        # If first element in list
        if index == 0:
            first_delimiter = self.__list.index(self.__delimiter, 0)
            # Get list except first element
            post = self.__list[first_delimiter:]
            # Get replaced element before modifying list
            replaced_element = self.__list[:first_delimiter]

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
                except Exception:
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

    def to_string(self):
        if self.is_empty():
            return ""
        elements = self.__list
        # Insert whitespace between elements
        spaced_element = "{}{}".format(self.__delimiter, " ")
        formatted_elements = elements.replace(self.__delimiter, spaced_element)
        return "[{}]".format(formatted_elements)

    def __type(self, element):
        if self.__is_int(element):
            return str(element)
        elif self.__is_string(element):
            return "'{}'".format(element)
        else:
            raise TypeError("Datatype not supported")

    def __is_int(self, var):
        return isinstance(var, int)

    def __is_string(self, var):
        return isinstance(var, str)
