from ctypes import c_void_p, cast, pointer
from typing import List, Union

import h2libpy.data.matrix as mat
import h2libpy.data.misc as misc
import h2libpy.lib.h2matrix as libh2matrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.base.util import cptr_to_list, try_wrap, verify_type


class H2Matrix(StructWrapper, cstruct=libh2matrix.CStructH2Matrix):
    # ***** Fields *****
    rb: 'misc.ClusterBasis'
    cb: 'misc.ClusterBasis'
    u: 'misc.Uniform'
    f: 'misc.Uniform'
    rsons: int
    csons: int
    refs: int
    desc: int

    # ***** Constructors *****

    @classmethod
    def new(cls, rb: 'misc.ClusterBasis', cb: 'misc.ClusterBasis',
            fill: 'mat.H2FillType' = mat.H2FillType.Nothing) -> 'H2Matrix':
        if fill == mat.H2FillType.Uniform:
            return cls(libh2matrix.new_uniform_h2matrix(rb, cb))
        elif fill == mat.H2FillType.Full:
            return cls(libh2matrix.new_full_h2matrix(rb, cb))
        elif fill == mat.H2FillType.Zero:
            return cls(libh2matrix.new_zero_h2matrix(rb, cb))
        else:  # fill == mat.H2FillType.Nothing:
            return cls(libh2matrix.new_h2matrix(rb, cb))

    @classmethod
    def new_super(cls, rb: 'misc.ClusterBasis', cb: 'misc.ClusterBasis',
                  rsons: int, csons: int) -> 'H2Matrix':
        return cls(libh2matrix.new_super_h2matrix(rb, cb, rsons, csons))

    @classmethod
    def from_block(cls, b: 'misc.Block', rb: 'misc.ClusterBasis',
                   cb: 'misc.ClusterBasis') -> 'H2Matrix':
        return cls(libh2matrix.build_from_block_h2matrix(b, rb, cb))

    # ***** Properties *****

    def __getter_rb(self) -> 'misc.ClusterBasis':
        return try_wrap(self.cobj().rb, misc.ClusterBasis)

    def __getter_cb(self) -> 'misc.ClusterBasis':
        return try_wrap(self.cobj().cb, misc.ClusterBasis)

    def __getter_u(self) -> 'misc.Uniform':
        return try_wrap(self.cobj().u, misc.Uniform)

    def __getter_f(self) -> 'misc.Uniform':
        return try_wrap(self.cobj().f, misc.Uniform)

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

    def clone(self, rb: 'misc.ClusterBasis', cb: 'misc.ClusterBasis', *,
              structure_only: bool = False) -> 'H2Matrix':
        if structure_only:
            clone = libh2matrix.clonestructure_h2matrix(self, rb, cb)
            return try_wrap(clone, H2Matrix)
        else:
            return try_wrap(libh2matrix.clone_h2matrix(self, rb, cb), H2Matrix)

    def update(self) -> None:
        libh2matrix.update_h2matrix(self)

    def ref(self, ptr: 'H2Matrix') -> None:
        libh2matrix.ref_h2matrix(pointer(ptr.cobj()), self)

    def unref(self) -> None:
        libh2matrix.unref_h2matrix(self)

    def memsize(self, *, part: 'mat.SizePart' = mat.SizePart.Total) -> int:
        if part == mat.SizePart.Near:
            return libh2matrix.getnearsize_h2matrix(self)
        elif part == mat.SizePart.Far:
            return libh2matrix.getfarsize_h2matrix(self)
        elif part == mat.SizePart.Object:
            return libh2matrix.getsize_h2matrix(self)
        else:  # part == mat.SizePart.Total:
            return libh2matrix.gettotalsize_h2matrix(self)

    def clear(self) -> None:
        libh2matrix.clear_h2matrix(self)

    def scale(self, alpha: float) -> None:
        libh2matrix.scale_h2matrix(alpha, self)

    def rand(self) -> None:
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

    def project(self, src: Union['mat.AMatrix', 'mat.HMatrix']) -> None:
        verify_type(src, [mat.AMatrix, mat.HMatrix])
        if isinstance(src, mat.AMatrix):
            libh2matrix.project_amatrix_h2matrix(self, src)
        elif isinstance(src, mat.HMatrix):
            libh2matrix.project_hmatrix_h2matrix(self, src)

    def norm(self) -> float:
        return libh2matrix.norm2_h2matrix(self)

    def norm2_diff(self, other: 'H2Matrix') -> float:
        return libh2matrix.norm2diff_h2matrix(self, other)

    def delete(self) -> None:
        libh2matrix.del_h2matrix(self)
