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

# Lecture des données
rows = []
while iterator.hasNext():
	row =  iterator.next()
	rows.append(row)

iterationColIndex = idts.findColumnIndex("Iteration") 
iterationList = [] # ( [cluster1, cluster2, ... ] ) 

for currentRow in rows:
	clustersCoordinates = []
	nbClusters = str(currentRow.getCell(nbClusterIndex)) 

	# Récupération des données
	for i in range(0, int(nbClusters)):
		currentCluster = []

		for j in range(1, MaxDimensionIndex):
			currentCluster.append(str(currentRow.getCell(j))) 

		clustersCoordinates.append(currentCluster)
		clustersCoordinates.sort()
		iterationList.append(clustersCoordinates) 

# Analyse
# List -> Set
uniques = []
for x in iterationList:
	if x not in uniques: uniques.append(x)

print(uniques)

# Sortie du résultat
for currentRow in rows:
	resultCell = StringCell(str(len(uniques)))
	newRow = AppendedColumnRow(currentRow, [resultCell])
	outContainer.addRowToTable(newRow)
