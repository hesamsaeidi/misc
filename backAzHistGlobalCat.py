# two regions are defined in this code
# stations in these regions clustered and
# backazimuth histogram plotted for these 2
import matplotlib.pyplot as plt
# import pickle
# import numpy as np


western_sta = set()
southern_sta = set()
western_pup = []
southern_pup = []
pup = []

western_staGlob = set()
southern_staGlob = set()
western_pupGlob = []
southern_pupGlob = []
pupGlob = []

def backazimuth(az):
    if az >= 180:
        backAz = az - 180

    else:
        backAz = az + 180
    return backAz

def is_west(stlat, stlon):
    stlat = float(stlat)
    stlon = float(stlon)
    if -8 < stlon < 12 and -12 < stlat < 10:
        return True

# def is_south(stlat, stlon):
#     stlat = float(stlat)
#     stlon = float(stlon)
#     if 8 < stlon < 35 and -34 < stlat < -12:
#         return True

def is_south(stlat, stlon):
    stlat = float(stlat)
    stlon = float(stlon)
    if 8 < stlon < 26 and -34 < stlat < -22:
        if stlat < 15-(1.6*stlon):
            return True



with open("/Path/to/allData.out", "r") as bf:
    allData = bf.readlines()

for i in range(len(allData)):
    SEP = allData[i].split(" ")
    stlat = SEP[9]
    stlon = SEP[10]
    pup.append(float(SEP[12]))
    backAz = backazimuth(float(SEP[12]))
    if is_west(stlat, stlon):
        western_sta.add((stlat, stlon))
        western_pup.append(backAz)
    elif is_south(stlat, stlon):
        southern_sta.add((stlat, stlon))
        southern_pup.append(backAz)

with open("/Path/to/allData.out.Glob", "r") as bf:
    allDataGlob = bf.readlines()

for i in range(len(allDataGlob)):
    SEPG = allDataGlob[i].split(" ")
    stlatG = SEPG[9]
    stlonG = SEPG[10]
    pupGlob.append(float(SEPG[12]))
    backAzG = backazimuth(float(SEPG[12]))
    if is_west(stlatG, stlonG):
        western_staGlob.add((stlatG, stlonG))
        western_pupGlob.append(backAzG)
    elif is_south(stlatG, stlonG):
        southern_staGlob.add((stlatG, stlonG))
        southern_pupGlob.append(backAzG)



print("All azimuth: ",max(pup), min(pup))
print("southern: ", max(southern_pup), min(southern_pup))
print("South Augmented: ",len(southern_pup), len(southern_sta))
print("West Augmented: ", len(western_pup), len(western_sta))
print("South Global: ",len(southern_pupGlob), len(southern_staGlob))
print("West Global: ", len(western_pupGlob), len(western_staGlob))
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_tight_layout(True)
fig.suptitle('Back Azimuth distribution')
ax1.hist(western_pup, bins=50, alpha=1, color='red')
ax1.hist(western_pupGlob, bins=50, alpha=1, color='blue')
ax1.set_title("Western batch")
ax2.hist(southern_pup, bins=50, alpha=1, label='Augmented South', color='red')
ax2.hist(southern_pupGlob, bins=50, alpha=1, label='Global South', color='blue')
ax2.set_title("Southern batch")
# make every part of the plot smaller in the tight layout
# and make room for the legend bbox
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 1.1, box.height*1.1])
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 1.1, box.height*1.1])

fig.legend(loc='upper left')
plt.show()
# plt.savefig("histGlobalCat.png", format="PNG")
# def write_to_file(file_name, input_set):
#     with open(file_name,"w") as f:
#         for i in input_set:
#             f.write(str(i[1])+" "+str(i[0])+'\n')
#
#
# write_to_file("globalStationsWest", western_staGlob)
# write_to_file("globalStationsSouth", southern_staGlob)
# write_to_file("AugmentedStationsWest", western_sta)
# write_to_file("AugmentedStationsSouth", southern_sta)
