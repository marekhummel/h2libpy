code = r"""
    def __getter_dim(self) -> int:
        return self.cobj().dim

    def __getter_v(self) -> Tuple[float, ...]:
        return tuple(cptr_to_list(self.cobj().v, self.dim))

"""


import re
rgx = re.compile(r'def __getter_(?P<field>.*?)\(self\) -> (?P<type>.*):')

print("    # ***** Fields *****")
for line in code.split('\n'):
    if m := rgx.match(line.strip()):
        print(f"    {m.group('field')}: {m.group('type')}")
