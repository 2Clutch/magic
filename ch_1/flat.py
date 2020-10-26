class Flat:

    def __init__(self):
        self.list = None

    def flat(self, sample_list):
        """
        Flattens an array of arbitrarily nested arrays

        :arg:
            sample_list (list): list of arbitrarily nested list

        :returns:
            a flattened/normal list
        """
        self.list = sample_list

        flat_list = []

        for i in self.list:
            if isinstance(i, (list, tuple)):
                for j in self.flat(i):
                    flat_list.append(j)
            else:
                flat_list.append(i)

        return list(flat_list)


if __name__ == '__main__':
    test = Flat()

    test_list = [[1, 2, [3]], 4]
    result = test.flat(test_list)

    print(result)
