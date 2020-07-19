code = """

struct _dblock
{
  /** @brief Row cluster */
  pdcluster rc;
  /** @brief Column cluster */
  pdcluster cc;

  /** @brief Row direction */
  uint rd;
  /** @brief Column direction */
  uint cd;

  /** @brief Admissibility flag */
  bool adm;

  /** @brief Number of row sons */
  uint rsons;

  /** @brief Number of column sons */
  uint csons;

  /** @brief Pointers to sons.
   *
   *  <tt>son[i+j*rsons]</tt> points to the son in row <tt>i</tt>
   *  and column <tt>j</tt>. */
  pdblock *son;

  /** @brief Number of descendants, including this block */
  uint desc;
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
        print(f'(\'{n}\', {fulltype}),')
