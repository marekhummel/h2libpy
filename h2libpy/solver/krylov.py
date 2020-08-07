from ctypes import c_uint, c_void_p, cast
from typing import List

import h2libpy.data.matrix as mat
import h2libpy.data.vector as vec
import h2libpy.lib.krylov as libkrylov
from h2libpy.base.util import pylist_to_ptr


def norm2_matrix(mvm, A, rows: int, cols: int) -> float:
    cmvm = libkrylov.CFuncMvmT(mvm)
    ca = cast(A, c_void_p)
    return libkrylov.norm2_matrix(cmvm, ca, rows, cols)


def norm2diff_matrix(mvma, A, mvmb, B, rows: int, cols: int) -> float:
    cmvma = libkrylov.CFuncMvmT(mvma)
    ca = cast(A, c_void_p)
    cmvmb = libkrylov.CFuncMvmT(mvmb)
    cb = cast(B, c_void_p)
    return libkrylov.norm2diff_matrix(cmvma, ca, cmvmb, cb, rows, cols)


def norm2diff_pre_matrix(mvma, A, evalb, evaltransb, B, 
                         rows: int, cols: int) -> float:
    cmvma = libkrylov.CFuncMvmT(mvma)
    ca = cast(A, c_void_p)
    cevalb = libkrylov.CFuncPrcdT(evalb)
    cevaltransb = libkrylov.CFuncPrcdT(evaltransb)
    cb = cast(B, c_void_p)
    return libkrylov.norm2diff_pre_matrix(cmvma, ca, cevalb, cevaltransb, cb, 
                                          rows, cols)


def norm2diff_id_matrix(mvma, A, solveb, solvetransb, B, 
                        rows: int, cols: int) -> float:
    cmvma = libkrylov.CFuncMvmT(mvma)
    ca = cast(A, c_void_p)
    csolveb = libkrylov.CFuncPrcdT(solveb)
    csolvetransb = libkrylov.CFuncPrcdT(solvetransb)
    cb = cast(B, c_void_p)
    return libkrylov.norm2diff_id_pre_matrix(cmvma, ca, cevalb, cevaltransb,
                                             cb, rows, cols)


def init_cg(addeval, matrix, b: 'vec.AVector', x: 'vec.AVector', 
            r: 'vec.AVector', p: 'vec.AVector', a: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    libkrylov.init_cg(caddeval, cmatrix, b, x, r, p, a)


def step_cg(addeval, matrix, b: 'vec.AVector', x: 'vec.AVector', 
            r: 'vec.AVector', p: 'vec.AVector', a: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    libkrylov.step_cg(caddeval, cmatrix, b, x, r, p, a)


def evalfunctional_eg(addeval, matrix, b: 'vec.AVector', x: 'vec.AVector', 
                      r: 'vec.AVector') -> float:
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    libkrylov.evalfunctional_cg(caddeval, cmatrix, b, x, r)


def init_pcg(addeval, matrix, prcd, pdata, b: 'vec.AVector', x: 'vec.AVector', 
             r: 'vec.AVector', q: 'vec.AVector', p: 'vec.AVector', 
             a: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    libkrylov.init_pcg(caddeval, cmatrix, cprcd, cpdata, b, x, r, q, p, a)


def step_pcg(addeval, matrix, prcd, pdata, b: 'vec.AVector', x: 'vec.AVector', 
             r: 'vec.AVector', q: 'vec.AVector', p: 'vec.AVector', 
             a: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    libkrylov.step_pcg(caddeval, cmatrix, cprcd, cpdata, b, x, r, q, p, a)


def init_uzawa(solve_a11, matrix_a11, mvm_a21, matrix_a21, b1: 'vec.AVector',
               b2: 'vec.AVector', x1: 'vec.AVector', x2: 'vec.AVector',
               r2: 'vec.AVector', p2: 'vec.AVector', a1: 'vec.AVector', 
               s2: 'vec.AVector'):
    csolvea11 = libkrylov.CFuncPrcdT(solve_a11)
    cmatrixa11 = cast(matrix_a11, c_void_p)
    cmvma21 = libkrylov.CFuncMvmT(mvm_a21)
    cmatrixa21 = cast(matrix_a21, c_void_p)
    libkrylov.init_uzawa(csolvea11, cmatrixa11, cmvma21, cmatrixa21, 
                         b1, b2, x1, x2, r2, p2, a1, s2)


def step_uzawa(solve_a11, matrix_a11, mvm_a21, matrix_a21, b1: 'vec.AVector',
               b2: 'vec.AVector', x1: 'vec.AVector', x2: 'vec.AVector',
               r2: 'vec.AVector', p2: 'vec.AVector', a1: 'vec.AVector', 
               s2: 'vec.AVector'):
    csolvea11 = libkrylov.CFuncPrcdT(solve_a11)
    cmatrixa11 = cast(matrix_a11, c_void_p)
    cmvma21 = libkrylov.CFuncMvmT(mvm_a21)
    cmatrixa21 = cast(matrix_a21, c_void_p)
    libkrylov.step_uzawa(csolvea11, cmatrixa11, cmvma21, cmatrixa21, 
                         b1, b2, x1, x2, r2, p2, a1, s2)


def init_puzawa(solve_a11, matrix_a11, mvm_a21, matrix_a21, prcd, pdata,
                b1: 'vec.AVector', b2: 'vec.AVector', x1: 'vec.AVector', 
                x2: 'vec.AVector', r2: 'vec.AVector', q2: 'vec.AVector',
                p2: 'vec.AVector', a1: 'vec.AVector', s2: 'vec.AVector'):
    csolvea11 = libkrylov.CFuncPrcdT(solve_a11)
    cmatrixa11 = cast(matrix_a11, c_void_p)
    cmvma21 = libkrylov.CFuncMvmT(mvm_a21)
    cmatrixa21 = cast(matrix_a21, c_void_p)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    libkrylov.init_puzawa(csolvea11, cmatrixa11, cmvma21, cmatrixa21, cprcd,
                          cpdata, b1, b2, x1, x2, r2, q2, p2, a1, s2)
                          

def step_puzawa(solve_a11, matrix_a11, mvm_a21, matrix_a21, prcd, pdata,
                b1: 'vec.AVector', b2: 'vec.AVector', x1: 'vec.AVector', 
                x2: 'vec.AVector', r2: 'vec.AVector', q2: 'vec.AVector',
                p2: 'vec.AVector', a1: 'vec.AVector', s2: 'vec.AVector'):
    csolvea11 = libkrylov.CFuncPrcdT(solve_a11)
    cmatrixa11 = cast(matrix_a11, c_void_p)
    cmvma21 = libkrylov.CFuncMvmT(mvm_a21)
    cmatrixa21 = cast(matrix_a21, c_void_p)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    libkrylov.step_puzawa(csolvea11, cmatrixa11, cmvma21, cmatrixa21, cprcd,
                          cpdata, b1, b2, x1, x2, r2, q2, p2, a1, s2)

                
def init_bicg(addeval, addeval_trans, matrix, b: 'vec.AVector',
              x: 'vec.AVector', r: 'vec.AVector', rt: 'vec.AVector',
              p: 'vec.AVector', pt: 'vec.AVector', a: 'vec.AVector', 
              at: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    caddevaltrans = libkrylov.CFuncAddevalT(addeval_trans)
    cmatrix = cast(matrix, c_void_p)
    libkrylov.init_bicg(caddeval, caddevaltrans, cmatrix, b, x, r, rt, p, pt, 
                        a, at)
                        
                
def step_bicg(addeval, addeval_trans, matrix, b: 'vec.AVector',
              x: 'vec.AVector', r: 'vec.AVector', rt: 'vec.AVector',
              p: 'vec.AVector', pt: 'vec.AVector', a: 'vec.AVector', 
              at: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    caddevaltrans = libkrylov.CFuncAddevalT(addeval_trans)
    cmatrix = cast(matrix, c_void_p)
    libkrylov.step_bicg(caddeval, caddevaltrans, cmatrix, b, x, r, rt, p, pt, 
                        a, at)

                                        
def init_bicgstab(addeval, matrix, b: 'vec.AVector', x: 'vec.AVector', 
                  r: 'vec.AVector', rt: 'vec.AVector', p: 'vec.AVector',
                  a: 'vec.AVector', at: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    libkrylov.init_bicgstab(caddeval,cmatrix, b, x, r, rt, p, a, at)
    
                                        
def step_bicgstab(addeval, matrix, b: 'vec.AVector', x: 'vec.AVector', 
                  r: 'vec.AVector', rt: 'vec.AVector', p: 'vec.AVector',
                  a: 'vec.AVector', at: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    libkrylov.step_bicgstab(caddeval,cmatrix, b, x, r, rt, p, a, at)


def init_gmres(addeval, matrix, b: 'vec.AVector', x: 'vec.AVector', 
               rhat: 'vec.AVector', q: 'vec.AVector', kk: List[int], 
               qr: 'mat.AMatrix', tau: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    ckk = pylist_to_ptr(kk, c_uint)
    libkrylov.init_gmres(caddeval, cmatrix, b, x, rhat, q, ckk, qr, tau)


def step_gmres(addeval, matrix, b: 'vec.AVector', x: 'vec.AVector', 
               rhat: 'vec.AVector', q: 'vec.AVector', kk: List[int], 
               qr: 'mat.AMatrix', tau: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    ckk = pylist_to_ptr(kk, c_uint)
    libkrylov.step_gmres(caddeval, cmatrix, b, x, rhat, q, ckk, qr, tau)


def finish_gmres(addeval, matrix, b: 'vec.AVector', x: 'vec.AVector', 
                 rhat: 'vec.AVector', q: 'vec.AVector', kk: List[int], 
                 qr: 'mat.AMatrix', tau: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    ckk = pylist_to_ptr(kk, c_uint)
    libkrylov.finish_gmres(caddeval, cmatrix, b, x, rhat, q, ckk, qr, tau)


def residualnorm_gmres(rhat: 'vec.AVector', k: int) -> float:
    return libkrylov.residualnorm_gmres(rhat, k)


def init_pgmres(addeval, matrix, prcd, pdata, b: 'vec.AVector', 
                x: 'vec.AVector', rhat: 'vec.AVector', q: 'vec.AVector', 
                kk: List[int], qr: 'mat.AMatrix', tau: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    ckk = pylist_to_ptr(kk, c_uint)
    libkrylov.init_pgmres(caddeval, cmatrix, cprcd, cpdata, b, x, rhat, q, 
                          ckk, qr, tau)


def step_pgmres(addeval, matrix, prcd, pdata, b: 'vec.AVector', 
                x: 'vec.AVector', rhat: 'vec.AVector', q: 'vec.AVector', 
                kk: List[int], qr: 'mat.AMatrix', tau: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    ckk = pylist_to_ptr(kk, c_uint)
    libkrylov.step_pgmres(caddeval, cmatrix, cprcd, cpdata, b, x, rhat, q, 
                          ckk, qr, tau)


def finish_pgmres(addeval, matrix, prcd, pdata, b: 'vec.AVector', 
                x: 'vec.AVector', rhat: 'vec.AVector', q: 'vec.AVector', 
                kk: List[int], qr: 'mat.AMatrix', tau: 'vec.AVector'):
    caddeval = libkrylov.CFuncAddevalT(addeval)
    cmatrix = cast(matrix, c_void_p)
    cprcd = libkrylov.CFuncPrcdT(prcd)
    cpdata = cast(pdata, c_void_p)
    ckk = pylist_to_ptr(kk, c_uint)
    libkrylov.finish_pgmres(caddeval, cmatrix, cprcd, cpdata, b, x, rhat, q, 
                            ckk, qr, tau)


def residualnorm_pgmres(rhat: 'vec.AVector', k: int) -> float:
    return libkrylov.residualnorm_pgmres(rhat, k)
