#include <array>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>

void print_matrix(std::vector<std::vector<char>> &matrix) {
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[i].size(); j++) {
      std::cout << matrix[i][j];
    }
    std::cout << std::endl;
  }
}

std::pair<int, int> get_gaurd_coords(std::vector<std::vector<char>> &matrix) {
  // position of the gaurd
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[0].size(); j++) {
      if (matrix[i][j] == '^') {
        return {i, j};
      }
    }
  }

  return {-1, -1};
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

bool in_bounds(int x, int y, int n, int m) {
  return x >= 0 && y >= 0 && x < n && y < m;
}

void solve_part1(std::vector<std::vector<char>> &matrix, int x, int y) {
  int res = 1;
  matrix[x][y] = 'x';
  int n = matrix.size(), m = matrix[0].size();
  std::array<std::array<int, 2>, 4> dirs{{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}};
  int cur_dir = 0;

  while (in_bounds(x, y, n, m)) {
    if (in_bounds(x + dirs[cur_dir][0], y + dirs[cur_dir][1], n, m) &&
        matrix[x + dirs[cur_dir][0]][y + dirs[cur_dir][1]] == '#') {
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

  std::cout << res << "\n";
}

bool check_if_loop_is_possible(std::vector<std::vector<char>> &matrix, int x,
                               int y) {
  int n = matrix.size(), m = matrix[0].size();
  std::array<std::array<int, 2>, 4> dirs{{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}};
  std::set<std::tuple<int, int, int>> visited_states;
  int cur_dir = 0;

  // WARN: infinite loop here
  while (in_bounds(x, y, n, m)) {

    if (visited_states.count({x, y, cur_dir})) {
      return true; // Loop detected
    }

    visited_states.insert({x, y, cur_dir});

    if (in_bounds(x + dirs[cur_dir][0], y + dirs[cur_dir][1], n, m) &&
        (matrix[x + dirs[cur_dir][0]][y + dirs[cur_dir][1]] == '#' ||
         matrix[x + dirs[cur_dir][0]][y + dirs[cur_dir][1]] == 'o')) {

      cur_dir = (cur_dir + 1) % 4;
      continue;
    }

    x += dirs[cur_dir][0];
    y += dirs[cur_dir][1];
  }

  return false;
}

void solve_part2(std::vector<std::vector<char>> &matrix, int x, int y) {
  int n = matrix.size(), m = matrix[0].size();
  matrix[x][y] = 'x';
  std::vector<std::vector<char>> old_matrix = matrix;
  int res = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (matrix[i][j] == '.') {
        matrix[i][j] = 'o';
        if (check_if_loop_is_possible(matrix, x, y)) {
          res++;
        }
        matrix = old_matrix;
      }
    }
  }

  std::cout << res << "\n";
}

int main() {
  // std::vector<std::vector<char>> matrix(10, std::vector(10, ' '));
  std::vector<std::vector<char>> matrix(130, std::vector(130, ' '));
  get_input(matrix);
  const auto &[x, y] = get_gaurd_coords(matrix);
  solve_part1(matrix, x, y);
  get_input(matrix);
  solve_part2(matrix, x, y);
}
