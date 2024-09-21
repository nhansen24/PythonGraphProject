PythonGraphProject is a program that utilizes a CSV to create a graph, then that graph <br>
is passed into an A* function for determining optimal paths. Currently written for popular <br>
Seattle destinations, it recommends popular attractions between current location and target location.<br><br>

Limitations: 21 Sep 24 <br>
  As of first commit, graph is designed to only assign a Vertex the two closest geographic neighbor attractions. <br>
  This means no recommendations will appear if Test case is start = 'Space Needle' <br>
  and target = 'IKEA' because certain locations are geographically more isolated. <br>
  Thus IKEA and SEATAC may be neighbors but no path exists to downtown Seattle <br>
  with the current two neighbor per vertex constraint. <br>
  Possible fixes: include more neighbors per vertex or add more attractions on the CSV to 'bridge the gap' <br>
