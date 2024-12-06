#include <array>
#include <fstream>
#include <iostream>
#include <vector>

void print_matrix(std::vector<std::vector<char>> &matrix) {
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[i].size(); j++) {
      std::cout << matrix[i][j];
    }
    std::cout << std::endl;
  }
}

void get_input(std::vector<std::vector<char>> &matrix) {
  std::ifstream file("day6_input.txt");
  int i = 0;

  while (file.good()) {
    std::string line;
    std::getline(file, line);
    for (int j = 0; j < line.size(); j++) {
      matrix[i][j] = line[j];
    }
    i++;
  }

  file.close();
}

std::pair<int, int> get_gaurd_coords() {
  std::pair<int, int> p({92, 74});
  return p;
}

bool in_bounds(int x, int y, int n, int m) {
  return x >= 0 && y >= 0 && x < n && y < m;
}

void solve(std::vector<std::vector<char>> &matrix, int x, int y) {
  int res = 1;
  int n = matrix.size(), m = matrix[0].size();
  std::array<std::array<int, 2>, 4> dirs{{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}};
  int cur_dir = 0;
  matrix[x][y] = 'x';

  while (in_bounds(x, y, n, m)) {
    if (matrix[x + dirs[cur_dir][0]][y + dirs[cur_dir][1]] == '#') {
      cur_dir = (cur_dir + 1) % 4;
      continue;
    }

    x += dirs[cur_dir][0];
    y += dirs[cur_dir][1];

    if (in_bounds(x, y, n, m) && matrix[x][y] != 'x') {
      res++;
      matrix[x][y] = 'x';
    }
  }

  std::cout << res;
}

int main() {
  std::vector<std::vector<char>> matrix(130, std::vector(130, ' '));
  get_input(matrix);
  const auto &[x, y] = get_gaurd_coords();
  solve(matrix, x, y);
}
