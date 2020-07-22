from h2libpy.data.geometry.macrosurface3d import MacroSurface3d
from h2libpy.data.geometry.surface3d import Surface3d
# from h2libpy.data.vector.avector import AVector


mg = MacroSurface3d.new_sphere()
gr = Surface3d.from_macrosurface3d(mg, 32)

print('vert', gr.vertices)
print('edges', gr.edges)
print('tri', gr.triangles)
print('x', gr.x[:10])
print('e', gr.e[:10])
print('t', gr.t[:10])
print('s', gr.s[:10])
print('n', gr.n[:10])
print('g', gr.g)
print('hmin', gr.hmin)
print('hmax', gr.hmax)
