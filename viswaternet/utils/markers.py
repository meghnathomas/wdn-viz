# -*- coding: utf-8 -*-
from matplotlib.path import Path
import numpy as np

verts_epa_valve = [
(-1,-1),
(1,-1),
(0,0),
(-1,-1),
(-1,1),
(1,1),
(0,0),
(-1,1)
]

lines_epa_valve = [
Path.MOVETO, #begin the figure in the lower right
Path.LINETO, 
Path.LINETO, 
Path.LINETO, 
Path.MOVETO, 
Path.LINETO, 
Path.LINETO, 
Path.LINETO,
]

verts_epa_pump = [
(-6.716386363636368628e+01, 2.138990909090906456e+01),
(8.972136363636307621e+00, 2.138990909090907167e+01),
(9.741136363636313078e+00, 2.143790909090907348e+01),
(1.051713636363632354e+01, 2.146190909090907439e+01),
(1.129913636363630580e+01, 2.146190909090907439e+01),
(1.208113636363634491e+01, 2.146190909090907439e+01),
(1.285713636363629853e+01, 2.143790909090907348e+01),
(1.362613636363630398e+01, 2.138990909090907167e+01),
(1.367413636363630580e+01, 2.138990909090907167e+01),
(1.367413636363630580e+01, 2.138690909090905734e+01),
(3.300213636363633896e+01, 2.016290909090907135e+01),
(4.829913636363630758e+01, 4.098909090909081065e+00),
(4.829913636363630758e+01, -1.553809090909092028e+01),
(4.829913636363631468e+01, -3.597309090909092077e+01),
(3.173413636363631696e+01, -5.253809090909091850e+01),
(1.129913636363631468e+01, -5.253809090909092561e+01),
(-8.463863636363662124e+00,-5.253809090909092561e+01),
(-2.460786363636367113e+01,-3.704409090909092583e+01),
(-2.564786363636366318e+01, -1.754009090909093871e+01),
(-6.716386363636368628e+01, -1.754009090909094226e+01),
(-6.716386363636368628e+01, 2.138990909090906456e+01),
(-6.716386363636368628e+01, 2.138990909090906456e+01),
]

lines_epa_pump = [
1,
2,
4,
4,
4,
4,
4,
4,
2,
2,
4,
4,
4,
4,
4,
4,
4,
4,
4,
2,
2,
79
]

verts_epa_tank = np.array([[ 609.77777778,  363.55555556],
       [ 669.77777778,  335.55555556],
       [ 696.77777778,  307.55555556],
       [ 723.77777778,  247.55555556],
       [ 753.77777778,  182.55555556],
       [ 753.77777778,  -17.44444444],
       [ 723.77777778,  -82.44444444],
       [ 679.77777778, -180.44444444],
       [ 605.77777778, -222.44444444],
       [ 476.77777778, -222.44444444],
       [ 394.77777778, -222.44444444],
       [ 394.77777778, -522.44444444],
       [ 394.77777778, -822.44444444],
       [  39.77777778, -822.44444444],
       [-315.22222222, -822.44444444],
       [-315.22222222, -522.44444444],
       [-315.22222222, -222.44444444],
       [-398.22222222, -222.44444444],
       [-526.22222222, -221.44444444],
       [-596.22222222, -183.44444444],
       [-641.22222222,  -87.44444444],
       [-662.22222222,  -43.44444444],
       [-665.22222222,  -22.44444444],
       [-665.22222222,   82.55555556],
       [-665.22222222,  187.55555556],
       [-662.22222222,  208.55555556],
       [-641.22222222,  252.55555556],
       [-613.22222222,  312.55555556],
       [-585.22222222,  339.55555556],
       [-525.22222222,  366.55555556],
       [-482.22222222,  386.55555556],
       [-462.22222222,  387.55555556],
       [  39.77777778,  387.55555556],
       [ 559.77777778,  387.55555556],
       [ 609.77777778,  363.55555556],
       [ 609.77777778,  363.55555556]])

lines_epa_tank =  [1,  4,  4,  4,  4,  4,  4,  4,  4,  4,  2,  2,  2,  2,  2,  2,  2,
        2,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  2,
        2, 79]

verts_epa_res = np.array([[ 646.033,  171.767],
       [ 649.033, -283.233],
       [  43.033, -283.233],
       [-562.967, -283.233],
       [-564.967,   19.767],
       [-568.967,  475.767],
       [-568.967,  600.767],
       [-564.967,  614.767],
       [-562.967,  620.767],
       [-548.967,  626.767],
       [-533.967,  626.767],
       [-507.967,  626.767],
       [-506.967,  625.767],
       [-506.967,  554.767],
       [-505.967,  514.767],
       [-504.967,  446.767],
       [-503.967,  404.767],
       [-502.967,  326.767],
       [  37.033,  326.767],
       [ 577.033,  326.767],
       [ 578.033,  404.767],
       [ 580.033,  482.767],
       [ 584.033,  591.767],
       [ 586.033,  614.767],
       [ 586.033,  620.767],
       [ 600.033,  626.767],
       [ 615.033,  626.767],
       [ 643.033,  626.767],
       [ 646.033,  171.767],
       [ 646.033,  171.767]])

lines_epa_res =  [ 1,  2,  2,  2,  2,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,
        2,  2,  2,  2,  4,  4,  4,  4,  4,  4,  2,  2, 79]

epa_valve = Path(verts_epa_valve,lines_epa_valve)
epa_pump = Path(verts_epa_pump,lines_epa_pump)
epa_tank = Path(verts_epa_tank,lines_epa_tank)
epa_res = Path(verts_epa_res,lines_epa_res)
