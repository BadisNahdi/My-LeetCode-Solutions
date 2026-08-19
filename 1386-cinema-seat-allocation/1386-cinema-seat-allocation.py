class Solution(object):

    def maxNumberOfFamilies(self, n, reservedSeats):

        res = n * 2
        taken_group = set()

        for seat in reservedSeats:

            row = seat[0]
            j = seat[1]

            if 2 <= j <= 5:
                taken_group.add((row, 0))

            if 4 <= j <= 7:
                taken_group.add((row, 1))

            if 6 <= j <= 9:
                taken_group.add((row, 2))

        rows = set(row for row, group in taken_group)

        for row in rows:

            A = (row, 0) not in taken_group
            B = (row, 1) not in taken_group
            C = (row, 2) not in taken_group

            if A and C:
                actual = 2
            elif A or B or C:
                actual = 1
            else:
                actual = 0

            res -= (2 - actual)

        return res