
lines = []

with open('Day-4/day4_input.txt', 'r') as file:
  for line in file.readlines():
    line = line.rstrip('\n')
    lines.append(list(line))
  file.close()


def countWord(grid):
  word = "XMAS"
  word_length = len(word)
  directions = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Diagonal down-right
    (1, -1),  # Diagonal down-left
    (-1, 1),  # Diagonal up-right
    (-1, -1)  # Diagonal up-left
  ]
  
  rows = len(grid)
  cols = len(grid[0])
  count = 0
  
  # check if a word exists starting from a point
  def checkDirection(x, y, dx, dy):
    for i in range(word_length):
      nx, ny = x + i * dx, y + i * dy
      if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
        return False
    return True

  # traverse the grid
  for r in range(rows):
    for c in range(cols):
      for dx, dy in directions:
        if checkDirection(r, c, dx, dy):
          count += 1

  return count

result = countWord(lines)
print(result)