# in order to calcuolate the deflection intergation has to be performed
M_x = []
E = 68.9*10**9
G=26*10**9
I_


#Torque deflection:
def T_integrand(T,G,J):
    int = T/(G*J)
    return int
T_int = T_integrand(T,G,J)

