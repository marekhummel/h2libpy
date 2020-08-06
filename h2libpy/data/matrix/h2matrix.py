from ctypes import c_void_p, cast, pointer
from typing import List, Union

import h2libpy.lib.h2matrix as libh2matrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, try_wrap, verify_type
from h2libpy.data.matrix.amatrix import AMatrix
from h2libpy.data.matrix.enums import H2FillType, SizePart
from h2libpy.data.matrix.hmatrix import HMatrix
from h2libpy.data.misc.clusterbasis import ClusterBasis
from h2libpy.data.misc.uniform import Uniform


class H2Matrix(StructWrapper, cstruct=libh2matrix.CStructH2Matrix):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rb: 'ClusterBasis', cb: 'ClusterBasis',
            fill: 'H2FillType' = H2FillType.Nothing) -> 'H2Matrix':
        if fill == H2FillType.Uniform:
            return cls(libh2matrix.new_uniform_h2matrix(rb, cb))
        elif fill == H2FillType.Full:
            return cls(libh2matrix.new_full_h2matrix(rb, cb))
        elif fill == H2FillType.Zero:
            return cls(libh2matrix.new_zero_h2matrix(rb, cb))
        else:  # fill == H2FillType.Nothing:
            return cls(libh2matrix.new_h2matrix(rb, cb))

    @classmethod
    def new_super(cls, rb: 'ClusterBasis', cb: 'ClusterBasis',
                  rsons: int, csons: int) -> 'H2Matrix':
        return cls(libh2matrix.new_super_h2matrix(rb, cb, rsons, csons))

    @classmethod
    def from_block(cls, b: 'Block', rb: 'ClusterBasis',
                   cb: 'ClusterBasis') -> 'H2Matrix':
        return cls(libh2matrix.build_from_block_hmatrix(b, rb, cb))

    # ***** Properties *****

    def __getter_rb(self) -> 'ClusterBasis':
        return try_wrap(self.cobj().rb, ClusterBasis)

    def __getter_cb(self) -> 'ClusterBasis':
        return try_wrap(self.cobj().cb, ClusterBasis)

    def __getter_u(self) -> 'Uniform':
        return try_wrap(self.cobj().u, Uniform)

    def __getter_f(self) -> 'Uniform':
        return try_wrap(self.cobj().f, Uniform)

    # def __getter_son(self) -> List['H2Matrix']:
    #     pass

    def __getter_rsons(self) -> int:
        return self.cobj().rsons

    def __getter_csons(self) -> int:
        return self.cobj().csons

    def __getter_refs(self) -> int:
        return self.cobj().refs

    def __getter_desc(self) -> int:
        return self.cobj().desc

    # ***** Methods ******

    def clone(self, rb: 'ClusterBasis', cb: 'ClusterBasis', *,
              structure_only: bool = False) -> 'H2Matrix':
        if structure_only:
            clone = libh2matrix.clonestructure_h2matrix(self, rb, cb)
            return try_wrap(clone, H2Matrix)
        else:
            return try_wrap(libh2matrix.clone_h2matrix(self, rb, cb), H2Matrix)

    def update(self):
        libh2matrix.update_h2matrix(self)

    def ref(self, ptr: 'H2Matrix'):
        libh2matrix.ref_h2matrix(pointer(ptr), self)

    def unref(self):
        libh2matrix.unref_h2matrix(self)

    def size(self, *, part: 'SizePart' = SizePart.Total):
        if part == SizePart.Near:
            return libh2matrix.getnearsize_h2matrix(self)
        elif part == SizePart.Far:
            return libh2matrix.getfarsize_h2matrix(self)
        elif part == SizePart.Object:
            return libh2matrix.getsize_h2matrix(self)
        elif part == SizePart.Total:
            return libh2matrix.gettotalsize_h2matrix(self)

    def clear(self):
        libh2matrix.clear_h2matrix(self)

    def scale(self, alpha: float):
        libh2matrix.scale_h2matrix(alpha, self)

    def rand(self):
        libh2matrix.random_h2matrix(self)

    def enumerate(self) -> List['H2Matrix']:
        ptr = libh2matrix.enumerate_h2matrix(self)
        lst = cptr_to_list(ptr, self.desc)
        return [try_wrap(cs, H2Matrix) for cs in lst]

    def iterate(self, mname: int, rname: int, cname: int,
                pardepth: int, pre, post, data):
        cpre = libh2matrix.CFuncH2MatrixCallbackT(pre)
        cpost = libh2matrix.CFuncH2MatrixCallbackT(post)
        cdata = cast(data, c_void_p)
        libh2matrix.iterate_h2matrix(self, mname, rname, cname, pardepth,
                                     cpre, cpost, cdata)

    def project(self, src: Union['AMatrix', 'HMatrix']):
        verify_type(src, [AMatrix, HMatrix])
        if isinstance(src, AMatrix):
            libh2matrix.project_amatrix_h2matrix(self, src)
        elif isinstance(src, HMatrix):
            libh2matrix.project_hmatrix_h2matrix(self, src)

    def norm(self):
        return libh2matrix.norm2_h2matrix(self)

    def norm2_diff(self, other: 'H2Matrix') -> float:
        return libh2matrix.norm2diff_h2matrix(self, other)
