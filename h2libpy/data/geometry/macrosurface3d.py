from typing import List, Tuple

import h2libpy.lib.macrosurface3d as libmacrosurface3d
from h2libpy.base.cutil import carray_to_tuple, cptr_to_list
from h2libpy.base.structwrapper import StructWrapper


class MacroSurface3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        super().__init__(cobj, libmacrosurface3d.CStructMacroSurface3d)

    def __del__(self):
        pass
        # libmacrosurface3d.del_macrosurface3d(self)

    @classmethod
    def new(cls, vertices: int, edges: int, triangles: int) \
            -> 'MacroSurface3d':
        obj = libmacrosurface3d.new_macrosurface3d(vertices, edges, triangles)
        return cls(obj)

    @classmethod
    def new_sphere(cls) -> 'MacroSurface3d':
        return cls(libmacrosurface3d.new_sphere_macrosurface3d())

    # ***** Properties *****

    def __getter_vertices(self) -> int:
        return self.cobj().vertices

    def __getter_edges(self) -> int:
        return self.cobj().edges

    def __getter_triangles(self) -> int:
        return self.cobj().triangles

    def __getter_x(self) -> List[Tuple[float, float, float]]:
        vs = cptr_to_list(self.cobj().x, self.vertices)
        return [carray_to_tuple(v) for v in vs]

    def __getter_e(self) -> List[Tuple[int, int]]:
        vs = cptr_to_list(self.cobj().e, self.edges)
        return [carray_to_tuple(v) for v in vs]

    def __getter_t(self) -> List[Tuple[int, int, int]]:
        vs = cptr_to_list(self.cobj().t, self.triangles)
        return [carray_to_tuple(v) for v in vs]

    def __getter_s(self) -> List[Tuple[int, int, int]]:
        vs = cptr_to_list(self.cobj().s, self.triangles)
        return [carray_to_tuple(v) for v in vs]

    # ***** Methods ******
