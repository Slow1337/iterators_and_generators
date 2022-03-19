nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(nested_iterable):
    for nest in nested_iterable:
        for item in nest:
            yield item
            

for item in flat_generator(nested_list):
	print(item)