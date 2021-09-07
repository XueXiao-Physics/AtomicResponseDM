from Element import element,au
import numpy as np
'''

Xe (Xenon)

'''  
C = [[[-0.965401, -0.040350, 0.001890, -0.003868, -0.000263,
         0.000547, -0.000791, 0.000014, -0.000013, -0.000286,
         0.000005, -0.000003, 0.000001] ] ,
     [[0.313912, 0.236118, -0.985333, 0.000229, -0.346825, 
        0.345786, -0.120941, -0.005057, 0.001528, -0.151508, 
        -0.000281, 0.000134, -0.000040] ,
      [0.051242, 0.781070, 0.114910, -0.000731, 0.000458,
       0.083993, -0.000265, 0.000034, 0.009061, -0.000014,
       0.000006, -0.000002] ] ,
     [[-0.140382, -0.125401, 0.528161, -0.000435, 0.494492, 
       -1.855445, 0.128637, -0.017980, 0.000792, 0.333907,
       -0.000228, 0.000191, -0.000037],
      [0.000264, 0.622357, -0.009861, -0.952677, -0.337900,
       -0.026340, -0.000384, -0.001665, 0.087491, 0.000240,
       -0.000083, 0.000026],
      [0.220185, 0.603140, 0.194682, -0.014369, 0.049865,
       -0.000300, 0.000418, -0.000133]] ,
     [[0.064020, 0.059550, -0.251138, 0.000152, -0.252274,
       1.063559, -0.071737, -0.563072, -0.697466, -0.058009,
       -0.018353, 0.00292, -0.000834],
      [0.013769, -0.426955, 0.045088, 0.748434, 0.132850,
       0.059406, -0.679569, -0.503653, -0.149635, -0.014193,
       0.000528, -0.000221],
      [-0.013758, -0.804573, 0.260624, 0.007490, 0.244109, 
       0.597018, 0.395554, 0.039786]] ,
     [[-0.022510, -0.021077, 0.088978, -0.000081, 0.095199,
       -0.398492, 0.025623, 0.274471, 0.291110, 0.011171,
       -0.463123, -0.545266, -0.167779],
      [-0.005879, 0.149040, -0.018716, -0.266839, -0.031096, 
       -0.024100, 0.267374, 0.161460, 0.059721, -0.428353,
       -0.542284, -0.201667]] ]

# Z_lj
Z = [ [54.9179, 47.25, 26.0942, 68.1771, 16.8296,
       12.0759, 31.903, 8.0145, 5.8396, 14.7123,
       3.8555, 2.6343, 1.8124] ,
     [58.7712, 22.6065, 48.9702, 13.4997, 9.8328,
      40.2591, 7.1841, 5.1284, 21.533, 3.4469,
      2.2384, 1.4588] , 
     [19.9787, 12.2129, 8.6994, 27.7398, 15.941, 
      6.058, 4.099, 2.5857] ]


n_list = [ [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5] ,
     [2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5] ,
     [3, 3, 3, 4, 4, 4, 4, 4] ]


E_B = [ [-1224.397767 * au] , 
       [-189.230111 * au,-177.782438 * au] , 
       [-40.175652 * au,-35.221651 * au,-26.118859 * au] , 
       [-7.856291 * au,-6.008328 * au,-2.777871 * au] ,
       [-0.944407 * au,-0.457283 * au] ]


Z_eff=[]
for n in range(len(E_B)):
    Z_eff.append([])
    for l in range(len(E_B[n])):
        Z_eff[n].append((n+1) * np.sqrt(-2*E_B[n][l] / au))

semi_full = {}

elem = element('Xe',C,Z,n_list,E_B,Z_eff,semi_full)
