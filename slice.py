

def sl(m, x_s, x_e, y_s, y_e):
    m_local = m[:][y_s:y_e]
    xlen = len(m)
    for i in range(xlen):
        m_local = m_local[i][x_s:x_e]
    return m_local

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
slice = [matrix[i][3:5] for i in range(0,3)]
print (slice)

print (slice[1])
slice2 = [slice[i][1:2] for i in range(2,3)]
print (slice2)
#m = sl(matrix, 0, 3, 0, 3)
