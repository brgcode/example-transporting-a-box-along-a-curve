from compas.geometry import Point, Box, Transformation
from compas.geometry import NurbsCurve
# from compas.geometry import Polyline
from compas_view2.app import App

curve = NurbsCurve.from_points([Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)])
frames = [curve.frame_at(t) for t in curve.space(50)]
xforms = [Transformation.from_frame_to_frame(frames[0], frame) for frame in frames]

box = Box(frames[0], 2, 1, 0.5)

# viewer = App(width=1600, height=900)
# viewer.view.camera.rz = 90
# viewer.view.camera.rx = -75
# viewer.view.camera.tx = 0
# viewer.view.camera.ty = -1
# viewer.view.camera.distance = 6

# viewer.add(Polyline(curve.locus()))
# viewer.add(box.frame)
# boxobj = viewer.add(box, opacity=0.5)

# @viewer.on(interval=100, frames=len(frames))
# def move(f):
#    viewer.add(frames[f])
#    boxobj.matrix = xforms[f].matrix
#    boxobj.update()

# viewer.show()
