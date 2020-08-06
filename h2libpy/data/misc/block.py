import h2libpy.lib.block as libblock
import h2libpy.lib.h2matrix as libh2matrix
import h2libpy.lib.hmatrix as libhmatrix
from h2libpy.base.structwrapper import StructWrapper
from h2libpy.data.misc.cluster import Cluster
from h2libpy.base.util import try_wrap, cptr_to_list
from typing import List
from ctypes import cast, c_void_p


class Block(StructWrapper, cstruct=libblock.CStructBlock):
    # ***** Constructors / destructor *****

    @classmethod
    def new(cls, rc: 'Cluster', cc: 'Cluster', a: bool,
            rsons: int, csons: int) -> 'Block':
        return cls(libblock.new_block(rc, cc, a, rsons, csons))

    @classmethod
    def build(cls, rc: 'Cluster', cc: 'Cluster', data, admis, *,
              strict: bool, lower: bool) -> 'Block':
        cdata = cast(data, c_void_p)
        cadm = libblock.CFuncAdmissible(admis)
        if strict and lower:
            return cls(libblock.build_strict_lower_block(rc, cc, cdata, cadm))
        elif strict:
            return cls(libblock.build_strict_block(rc, cc, cdata, cadm))
        elif lower:
            obj = libblock.build_nonstrict_lower_block(rc, cc, cdata, cadm)
            return cls(obj)
        else:
            return cls(libblock.build_nonstrict_block(rc, cc, cdata, cadm))

    @classmethod
    def from_hmatrix(cls, h: 'HMatrix'):
        return cls(libhmatrix.build_from_hmatrix_block(h))

    @classmethod
    def from_h2matrix(cls, h: 'H2Matrix'):
        return cls(libh2matrix.build_from_h2matrix_block(h))

    # ***** Properties *****

    def __gettter_rc(self) -> 'Cluster':
        return try_wrap(self.cobj().rc, Cluster)

    def __gettter_cc(self) -> 'Cluster':
        return try_wrap(self.cobj().cc, Cluster)

    def __getter_a(self) -> bool:
        return self.cobj().a

    # def __getter_son(self) -> List['Block']:
    #     return self.cobj().son

    def __getter_rsons(self) -> int:
        return self.cobj().rsons

    def __getter_csons(self) -> int:
        return self.cobj().csons

    def __getter_desc(self) -> int:
        return self.cobj().desc

    # ***** Methods ******

    def update(self):
        libblock.update_block(self)

    def iterate(self, bname: int, rname: int, cname: int, pre, post, data):
        cpre = libblock.CFuncBlockCallbackT(pre)
        cpost = libblock.CFuncBlockCallbackT(post)
        cdata = cast(data, c_void_p)
        libblock.iterate_block(self, bname, rname, cname, cpre, cpost, cdata)

    def iterate_rowlist(self, bname: int, rname: int, cname: int,
                        pardepth: int, pre, post, data):
        cpre = libblock.CFuncBlockEntryCallbackT(pre)
        cpost = libblock.CFuncBlockEntryCallbackT(post)
        cdata = cast(data, c_void_p)
        libblock.iterate_rowlist_block(self, bname, rname, cname, pardepth,
                                       cpre, cpost, cdata)

    def iterate_collist(self, bname: int, rname: int, cname: int,
                        pardepth: int, pre, post, data):
        cpre = libblock.CFuncBlockEntryCallbackT(pre)
        cpost = libblock.CFuncBlockEntryCallbackT(post)
        cdata = cast(data, c_void_p)
        libblock.iterate_collist_block(self, bname, rname, cname, pardepth,
                                       cpre, cpost, cdata)

    def iterate_byrow(self, bname: int, rname: int, cname: int,
                      pardepth: int, pre, post, data):
        cpre = libblock.CFuncBlockCallbackT(pre)
        cpost = libblock.CFuncBlockCallbackT(post)
        cdata = cast(data, c_void_p)
        libblock.iterate_byrow_block(self, bname, rname, cname, pardepth,
                                     cpre, cpost, cdata)

    def iterate_bycol(self, bname: int, rname: int, cname: int,
                      pardepth: int, pre, post, data):
        cpre = libblock.CFuncBlockCallbackT(pre)
        cpost = libblock.CFuncBlockCallbackT(post)
        cdata = cast(data, c_void_p)
        libblock.iterate_bycol_block(self, bname, rname, cname, pardepth,
                                     cpre, cpost, cdata)

    def enumerate(self) -> List['Block']:
        ptr = libblock.enumerate_block(self)
        lst = cptr_to_list(ptr, self.desc)
        return [try_wrap(b, Block) for b in lst]

    def enumerate_level(self) -> List[int]:
        ptr = libblock.enumerate_level_block(self)
        return cptr_to_list(ptr, self.desc)

    def depth(self) -> int:
        return libblock.getdepth_block(self)

    def compute_csp(self) -> int:
        return libblock.compute_csp_block(self)
