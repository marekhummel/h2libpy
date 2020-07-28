code = r"""
 struct _sparsematrix {
  /** @brief Number of rows. */
  uint rows;
  /** @brief Number of columns. */
  uint cols;
  /** @brief Number of non-zero entries. */
  uint nz;

  /** @brief Starting indices for row representations in @c col and
   *  @c coeff. */
  uint *row;
  /** @brief Column indices of non-zero entries. */
  uint *col;
  /** @brief Coefficients of non-zero entries. */
  pfield coeff;
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
