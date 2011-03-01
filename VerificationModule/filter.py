# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author : Maxime Gaudin
# Year : 2011

iterator = inData0.iterator()
idts = inData0.getDataTableSpec() 

clustersCollndex = idts.findColumnIndex("Cluster")
nbClusterIndex = idts.findColumnIndex("nbCluster")

MaxDimensionIndex = nbClusterIndex - 1

iterationColIndex = idts.findColumnIndex("Iteration") 
iterationList = [] # ( [cluster1, cluster2, ... ] ) 
rows = []
row =  iterator.next()
rows.append(row) 
while iterator.hasNext():
	clustersCoordinates = []
	nbClusters = str(row.getCell(nbClusterIndex)) 

	# Récupération des données
	for i in range(0, int(nbClusters)):
		currentCluster = []

		for j in range(1, MaxDimensionIndex):
			currentCluster.append(str(row.getCell(j))) 

		clustersCoordinates.append(currentCluster)

		if iterator.hasNext():
			row = iterator.next()
			rows.append(row) 

		clustersCoordinates.sort()

		iterationList.append(clustersCoordinates) 

	# Analyse
	# List -> Set
	uniques = []
	for x in iterationList:
		if x not in uniques: uniques.append(x)

	# Sortie du résultat
	for r in rows:
		resultCell = StringCell(str(len(uniques)))
		newRow = AppendedColumnRow(r, [resultCell])
		outContainer.addRowToTable(newRow)
