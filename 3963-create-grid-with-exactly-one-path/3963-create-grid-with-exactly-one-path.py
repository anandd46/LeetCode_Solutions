class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        grid.append("." * n)
        for _ in range(m - 1):
            grid.append("#" * (n - 1) + ".")
        return grid