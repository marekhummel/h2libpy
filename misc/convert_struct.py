code = r"""
struct _clustergeometry {
struct _blockentry {
  /** @brief block tree.*/
  pcblock b;
  /** @brief Number of the block tree.*/
  uint bname;
  /** @brief Number of the row cluster of <tt>b</tt>.*/
  uint rname;
  /** @brief Number of the column cluster of <tt>b</tt>.*/
  uint cname;
  /** @brief Pointer to the blockentry object of the father of <tt>b</tt>.*/
  pcblockentry father;
  /** @brief Pointer to the blockentry object of the sucessor of <tt>b</tt>.*/
  pblockentry next;
};

};
"""


import re
rgx = re.compile(r'([A-Za-z0-9_]+)\s+(\**)([A-Za-z0-9_]+);')

for line in code.split('\n'):
    if m := rgx.match(line.strip()):
        t = m.group(1)
        p = m.group(2)
        n = m.group(3)

        t = 'c_' + t if t in ['uint', 'int', 'bool'] else t
        t = f'PTR({t[2:]})' if t.startswith('pc') else t
        t = f'PTR({t[1:]})' if t.startswith('p') else t
        fulltype = 'PTR(' * len(p) + t + ')' * len(p)
        fulltype = fulltype.replace('PTR(void)', 'c_void_p')
        print(f'(\'{n}\', {fulltype}),')
