import arcpy as ap
source = ap.GetParameterAsText(0)
destination = ap.GetParameterAsText(1)
linearUnit = ap.GetParameterAsText(2)
bufferCount = ap.GetParameter(3)
bufferRadius = ap.GetParameter(4)
bufferIncrease = ap.GetParameter(5)

ap.env.workspace = destination
fc = "Educational_Institutions"
if ap.Exists(fc):  # Checking feature class exists within Geodatabase
    ap.AddMessage("Feature class '{}' exists within the Geodatabase".format(fc))
ap.env.overwriteOutput = True

BufferList = list(range(bufferRadius, bufferRadius + (bufferIncrease * bufferCount), bufferIncrease))

for buffer in BufferList:
    des = ap.Describe(source)
    output = (des.basename + "_{}".format(buffer))  # Adding buffer distance
    outputFc = (des.basename + "_")
    ap.Buffer_analysis(source, output, (str(buffer) + " " + linearUnit), "Full", "Round")
    ap.AddMessage("FC created: " + outputFc + str(buffer))
