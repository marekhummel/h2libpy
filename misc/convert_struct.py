code = r"""
 /** @brief Number of vertices */
  uint vertices;

  /** @brief Number of edges */
  uint edges;

  /** @brief Number of triangles */
  uint triangles;

  /** @brief Vertex coordinates */
  real (*x)[3];

  /** @brief Edge vertices */
  uint (*e)[2];

  /** @brief Triangle vertices.
   *
   *  The vertices are ordered counter-clockwise as seen from outside
   *  of the geometry, i.e., taking the cross product of
   *  <tt>x[t[i][1]]-x[t[i][0]]</tt> and <tt>x[t[i][2]]-x[t[i][0]]</tt>
   *  is supposed to yield an outer normal vector of the (unparametrized)
   *  triangle. */
  uint (*t)[3];

  /** @brief Triangle edges.
   *
   *  Edge <tt>s[i][j]</tt> lies opposite of vertex <tt>t[i][j]</tt>. */
  uint (*s)[3];

  /** @brief Parametrization callback.
   *
   *  Given a triangle index <tt>i</tt> and coordinates <tt>xr1</tt>
   *  and <tt>xr2</tt> in the reference triangle
   *  @f$\widehat{T}=\{ (s,t)\ :\ 0\leq s,t\leq 1,\ s+t\leq 1 \}@f$,
   *  this function returns the point @f$\Phi_i(\widehat{x})@f$
   *  in the parametrized triangle in the array <tt>xt</tt>.
   *
   *  Usually, the callback function will use the geometric information
   *  in <tt>x</tt>, <tt>e</tt>, <tt>t</tt>, and <tt>s</tt> to
   *  accomplish its task.
   *  Additional information can be provided via the pointer
   *  <tt>phidata</tt>.
   *
   *  It is up to the user to ensure that the vertices and edges
   *  of a refined triangulation produced by evaluating @f$\Phi_i@f$ in
   *  the vertices and along the edges of the macro triangulation
   *  in adjacent triangles match. */
  void (*phi)(uint i, real xr1, real xr2, void *phidata, real xt[3]);

  /** @brief Pointer that will be passed to the <tt>phi</tt> callback
   *  function. */
  void *phidata;
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
