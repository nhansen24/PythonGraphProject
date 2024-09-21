PythonGraphProject is a program that utilizes a CSV to create a graph, then that graph is passed into an A* function for determining optimal paths. 
Currently written for popular Seattle destinations, it recommends popular attractions between current location and target location.

Limitations: 21 Sep 24
  As of first commit the graph is designed to only assign a Vertex the two closest geographic neighbor attractions. 
  This means no recommendations will appear if Test case is start = 'Space Needle' and target = 'IKEA' because certain locations are geographically more isolated.
  Thus IKEA and SEATAC may be neighbors but no path exists to downtown Seattle with the current two neighbor per vertex constraint.
  Possible fixes would be to include more neighbors per vertex or add more attractions on the CSV to 'bridge the gap' 
