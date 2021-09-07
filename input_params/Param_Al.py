from Element import element,au
import numpy as np

C = [[[0.373865,0.456146,0.20250,0.001901,0.000823,-0.000267,-0.000560,0.000083,-0.000044,0.000013] ] ,
[[0.061165,-0.460373,0.055062,0.297052,0.750997,0.064079,0.000270,-0.001972,0.000614,-0.000064] ,[0.015480,0.204774,0.474317,0.339646,0.024290,0.003529,-0.000204,0.000199]],
 [[0.020024 , -0.119051 , 0.017451 , 0.079185 , 0.130917 , 0.13913 , 0.000038 , -0.303750 , -0.547941 , -0.285949], [ -0.001690 , -0.048903 , -0.058101 , -0.090680 , -0.001445 , 0.234760 , 0.496072 , 0.359277  ]]  ]


Z = [ [18.1792,10.8835,15.7593,5.7600,4.0085,2.8676,33.5797,2.1106,1.3998,1.0003] ,
     [14.4976, 6.6568, 4.2183, 3.0026, 11.0822, 1.6784, 1.0788, 0.7494] ]

n_list = [ [1, 1, 2, 2, 2, 2, 3, 3, 3, 3] ,[2, 2, 2, 2, 3, 3, 3, 3] ]


E_B = [ [-58.501026 * au] ,[-4.910672 * au,-3.218303 * au] , [-0.393420 * au,-0.209951 * au] ]


Z_eff=[]
for n in range(len(E_B)):
    Z_eff.append([])
    for l in range(len(E_B[n])):
        Z_eff[n].append((n+1) * np.sqrt(-2*E_B[n][l] / au))

semi_full = {(3,1):(1,6)}

elem = element('Al',C,Z,n_list,E_B,Z_eff,semi_full)

