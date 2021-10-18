import arcpy as ap
source = input("Please enter the path and name of the feature class to be buffered: ")
destination = input("Please enter the path and name of the Geodatabase (with .gdb extension) to store the output: ")
linearUnit = input("Please enter the linear unit in 'meters' or 'feet': ")
bufferCount = int(input("Please enter the number of buffers to be created: "))
bufferRadius = int(input("Please enter the radius of the first buffer: "))
bufferIncrease = int(input("Please enter the increment for increase size of each subsequent buffer: "))
print()

ap.env.workspace = destination
fc = "Educational_Institutions"
if ap.Exists(fc):  # Checking feature class exists within Geodatabase
    print("Feature class '{}' exists within the Geodatabase".format(fc))
ap.env.overwriteOutput = True
print()

BufferList = list(range(bufferRadius, bufferRadius + (bufferIncrease * bufferCount), bufferIncrease))

for buffer in BufferList:
    des = ap.Describe(source)
    output = (des.basename + "_{}".format(buffer))  # Adding buffer distance
    outputFc = (des.basename + "_")
    ap.Buffer_analysis(source, output, (str(buffer) + " " + linearUnit), "Full", "Round")
    print("FC created: " + outputFc + str(buffer))
