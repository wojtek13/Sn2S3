
from pylab import *
import math as m
from scipy.integrate import quad
import fit_lorentz as FLnew

def Lorentz(x,loc_par,gamma,height):
    return height*gamma**2/((x-loc_par)**2+gamma**2)


startFittingRange = 150
endFittingRange = 330
alfa=0
alfa1 = []
intensity185 = []
intensity210 = []
intensity240 = []
intensity310 = []
while alfa<=360:
    nazwa = ("2015-09-14_Sn2S3_MonikaWojtek/%03d_VH_Sn2S3.txt" % alfa)
    Data = np.loadtxt(nazwa)
    RamanShift=Data[:,0]
    Intensity=Data[:,1]
    print alfa
    fittingRange=(RamanShift<endFittingRange)*(RamanShift>startFittingRange)
    fitParameters = FLnew.perform_fitting(RamanShift, Intensity)
    alfa1.append(alfa)
    intensity185.append(quad(Lorentz, 140, 340, args=(fitParameters[0][1], fitParameters[0][0], fitParameters[0][2])))
    intensity210.append(quad(Lorentz, 140, 340, args=(fitParameters[1][1], fitParameters[1][0], fitParameters[1][2])))
    intensity240.append(quad(Lorentz, 140, 340, args=(fitParameters[2][1], fitParameters[2][0], fitParameters[2][2])))
    intensity310.append(quad(Lorentz, 140, 340, args=(fitParameters[4][1], fitParameters[4][0], fitParameters[4][2])))
    alfa+=5

#print alfa1
#peak185
for i in range(len(alfa1)):
    plot(intensity185[i][0]*m.cos(m.radians(float(alfa1[i]))), float(intensity185[i][0])*m.sin(m.radians(float(alfa1[i]))), 'o')
show()
plot(alfa1, intensity185, '.')
show()
#f1 = open("peak254.txt", "w")
#f2 = open("peak324.txt", "w")
#f3 = open("peak156.txt", "w")
#f4 = open("peak193.txt", "w")
#for i in range(len(alfa1)):
#    f1.write(str(alfa1[i])+"\t"+str(intensity185[i][0])+"\n")
#    f2.write(str(alfa1[i])+"\t"+str(intensity210[i][0])+"\n")
#    f3.write(str(alfa1[i])+"\t"+str(intensity240[i][0])+"\n")
#    f4.write(str(alfa1[i])+"\t"+str(intensity310[i][0])+"\n")

#f1.close()
#f2.close()
#f3.close()
#f4.close()

#peak210
for i in range(len(alfa1)):
    plot(intensity210[i][0]*m.cos(m.radians(float(alfa1[i]))), float(intensity210[i][0])*m.sin(m.radians(float(alfa1[i]))), 'o')
show()
plot(alfa1, intensity210, '.')
show()

#peak240
for i in range(len(alfa1)):
    plot(intensity240[i][0]*m.cos(m.radians(float(alfa1[i]))), float(intensity240[i][0])*m.sin(m.radians(float(alfa1[i]))), 'o')
show()
plot(alfa1, intensity240, '.')
show()

#peak310
for i in range(len(alfa1)):
    plot(intensity310[i][0]*m.cos(m.radians(float(alfa1[i]))), float(intensity310[i][0])*m.sin(m.radians(float(alfa1[i]))), 'o')
show()
plot(alfa1, intensity310, '.')
show()