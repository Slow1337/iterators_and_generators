class FlatIterator:
    def __init__(self, nested_iterable):
        self.nested_iterable = nested_iterable
        self.flat_list = []

    def unnest_method(self, nested_element):
        for item in nested_element:
            self.flat_list.append(item)
            
    def __iter__(self):
        self.slice_id = 0
        for element in self.nested_iterable:
            if isinstance(element, list):
                self.unnest_method(element)
        self.count = len(self.flat_list)
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        iterated_item = self.flat_list[self.slice_id]
        self.slice_id += 1
        return iterated_item

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in FlatIterator(nested_list):
	print(item) #
