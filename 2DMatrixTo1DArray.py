# If you have a 2D matrix and you want to transform to a 1D array, going left to right, top to bottom, starting at top left cell. 
# The way to convert a (row,col) in 2D to index in 1D is:

# From 2D to 1D:
# ---------------
# index = row*numCols + col. where row and col are 0-starting indices of the cell in matrix, 
# and index is the 0-starting index of the 1D array.  numCols is number of columns of the matrix.

# From 1D to 2D:
# --------------
# from above, you get:
# row = index // numCols
# col = index % numCols
# otherwise known as divmod(index,numCols)

# Applicable problem: 
# Search in 2D Matrix II
