from ctypes import POINTER
from typing import List, Tuple

import h2libpy.lib.macrosurface3d as libmacrosurface3d
import h2libpy.lib.surface3d as libsurface3d
from h2libpy.base.cutil import carray_to_tuple, cptr_to_list, deref
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.geometry.macrosurface3d import MacroSurface3d


class Surface3d(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libsurface3d.CStructSurface3d))
        self._as_parameter_ = cobj

    def __del__(self):
        libsurface3d.del_surface3d(self)

    @classmethod
    def new(cls, vertices: int, edges: int, triangles: int) -> 'Surface3d':
        return cls(libsurface3d.new_surface3d(vertices, edges, triangles))

    @classmethod
    def from_macrosurface3d(cls, mg: 'MacroSurface3d', split: int) \
            -> 'Surface3d':
        obj = libmacrosurface3d.build_from_macrosurface3d_surface3d(mg, split)
        return cls(obj)

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

    def __getter_n(self) -> List[Tuple[float, float, float]]:
        vs = cptr_to_list(self.cobj().n, self.triangles)
        return [carray_to_tuple(v) for v in vs]

    def __getter_g(self) -> float:
        return deref(self.cobj().g).value

    def __getter_hmin(self) -> float:
        return self.cobj().hmin

    def __getter_hmax(self) -> float:
        return self.cobj().hmax

    # ***** Methods ******
