from ctypes import pointer
from typing import List, Tuple

import h2libpy.data.geometry as geo
import h2libpy.lib.macrosurface3d as libmacrosurface3d
import h2libpy.lib.surface3d as libsurface3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import (carray_to_tuple, cptr_to_list, deref,
                               pylist_to_ptr, try_wrap)
from h2libpy.lib.settings import real


class Surface3d(StructWrapper, cstruct=libsurface3d.CStructSurface3d):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, vertices: int, edges: int, triangles: int) -> 'Surface3d':
        return cls(libsurface3d.new_surface3d(vertices, edges, triangles))

    @classmethod
    def from_macrosurface3d(cls, mg: 'geo.MacroSurface3d', split: int) \
            -> 'Surface3d':
        obj = libmacrosurface3d.build_from_macrosurface3d_surface3d(mg, split)
        return cls(obj)

    @classmethod
    def from_file(cls, file: str,
                  fmt: 'geo.ReadFormat' = geo.ReadFormat.Default) \
            -> 'Surface3d':
        cfile = file.encode()
        if fmt == geo.ReadFormat.NetCDF:
            return cls(libsurface3d.read_nc_surface3d(cfile))
        elif fmt == geo.ReadFormat.Netgen:
            return cls(libsurface3d.read_netgen_surface3d(cfile))
        elif fmt == geo.ReadFormat.Gmsh:
            return cls(libsurface3d.read_gmsh_surface3d(cfile))
        elif fmt == geo.ReadFormat.Unv:
            return cls(libsurface3d.read_unv_surface3d(cfile))
        else:  # fmt == geo.ReadFormat.Default
            return cls(libsurface3d.read_surface3d(cfile))

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

    def prepare(self):
        libsurface3d.prepare_surface3d(self)

    def get_properties(self) -> Tuple[float, float, float, float]:
        phmin = pointer(real())
        phmax = pointer(real())
        panglemin = pointer(real())
        pangleedge = pointer(real())
        libsurface3d.getproperties_surface3d(self, phmin, phmax, panglemin,
                                             pangleedge)
        return (phmin.contents.value, phmax.contents.value,
                panglemin.contents.value, pangleedge.contents.value)

    def print(self):
        libsurface3d.print_surface3d(self)

    def check(self) -> int:
        return libsurface3d.check_surface3d(self)

    def is_closed(self) -> bool:
        return libsurface3d.isclosed_surface3d(self)

    def is_oriented(self) -> bool:
        return libsurface3d.isoriented_surface3d(self)

    def scale(self, a: List[float], b: List[float]):
        ca = pylist_to_ptr(a, real)
        cb = pylist_to_ptr(b, real)
        libsurface3d.scale_surface3d(self, ca, cb)

    def translate(self, t: List[float]):
        ct = pylist_to_ptr(t, real)
        libsurface3d.translate_surface3d(self, ct)

    def merge(self, other: 'Surface3d') -> 'Surface3d':
        obj = libsurface3d.merge_surface3d(self, other)
        return try_wrap(obj, Surface3d)

    def write(self, file: str, *, netcdf: bool = False):
        cfile = file.encode()
        if netcdf:
            libsurface3d.write_nc_surface3d(self, cfile)
        else:
            libsurface3d.write_surface3d(self, cfile)

    def refine_red(self, other: 'Surface3d') -> 'Surface3d':
        obj = libsurface3d.refine_red_surface3d(self)
        return try_wrap(obj, Surface3d)
