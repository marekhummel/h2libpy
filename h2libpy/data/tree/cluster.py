from ctypes import POINTER

import h2libpy.lib.cluster as libcluster
from h2libpy.base.structwrapper import StructWrapper


class Cluster(StructWrapper):
    # ***** Constructors / destructor *****

    def __init__(self, cobj):
        assert isinstance(cobj, POINTER(libcluster.CStructCluster))
        self._as_parameter_ = cobj

    def __del__(self):
        pass

    # ***** Properties *****

    # ***** Methods ******
