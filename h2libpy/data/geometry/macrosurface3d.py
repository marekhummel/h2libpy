from typing import List, Tuple

import h2libpy.lib.macrosurface3d as libmacrosurface3d
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import carray_to_tuple, cptr_to_list


class MacroSurface3d(StructWrapper,
                     cstruct=libmacrosurface3d.CStructMacroSurface3d):
    # ***** Fields *****
    vertices: int
    edges: int
    triangles: int
    x: List[Tuple[float, ...]]
    e: List[Tuple[int, ...]]
    t: List[Tuple[int, ...]]
    s: List[Tuple[int, ...]]

    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, vertices: int, edges: int, triangles: int) \
            -> 'MacroSurface3d':
        obj = libmacrosurface3d.new_macrosurface3d(vertices, edges, triangles)
        return cls(obj)

    @classmethod
    def new_sphere(cls) -> 'MacroSurface3d':
        return cls(libmacrosurface3d.new_sphere_macrosurface3d())

    @classmethod
    def new_parabolic_mirror(cls) -> 'MacroSurface3d':
        return cls(libmacrosurface3d.new_parabolic_mirror_macrosurface3d())

    @classmethod
    def new_cuboid(cls) -> 'MacroSurface3d':
        return cls(libmacrosurface3d.new_cuboid_macrosurface3d())

    @classmethod
    def new_cube(cls, ax: float, bx: float, ay: float, by: float,
                 az: float, bz: float) -> 'MacroSurface3d':
        obj = libmacrosurface3d.new_cube_macrosurface3d(ax, bx, ay, by, az, bz)
        return cls(obj)

    @classmethod
    def new_cylinder(cls) -> 'MacroSurface3d':
        return cls(libmacrosurface3d.new_cylinder_macrosurface3d())

    # ***** Properties *****

    def __getter_vertices(self) -> int:
        return self.cobj().vertices

    def __getter_edges(self) -> int:
        return self.cobj().edges

    def __getter_triangles(self) -> int:
        return self.cobj().triangles

    def __getter_x(self) -> List[Tuple[float, ...]]:
        vs = cptr_to_list(self.cobj().x, self.vertices)
        return [tuple(float(x) for x in carray_to_tuple(v)) for v in vs]

    def __getter_e(self) -> List[Tuple[int, ...]]:
        vs = cptr_to_list(self.cobj().e, self.edges)
        return [tuple(int(x) for x in carray_to_tuple(v)) for v in vs]

    def __getter_t(self) -> List[Tuple[int, ...]]:
        vs = cptr_to_list(self.cobj().t, self.triangles)
        return [tuple(int(x) for x in carray_to_tuple(v)) for v in vs]

    def __getter_s(self) -> List[Tuple[int, ...]]:
        vs = cptr_to_list(self.cobj().s, self.triangles)
        return [tuple(int(x) for x in carray_to_tuple(v)) for v in vs]
