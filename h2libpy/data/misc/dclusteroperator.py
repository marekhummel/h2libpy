import h2libpy.lib.dclusteroperator as libdclusteroperator
from h2libpy.base.structwrapper import StructWrapper


class DClusterOperator(StructWrapper,
                       cstruct=libdclusteroperator.CStructDClusterOperator):
    pass
    # ***** Constructors / destructor *****

    # ***** Properties *****

    # ***** Methods ******
