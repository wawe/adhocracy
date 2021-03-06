from adhocracy.tests import TestController
import adhocracy.lib.sorting


class TestSorting(TestController):

    def test_controversy(self):
        c = adhocracy.lib.sorting.proposal_controversy_calculate

        assert c(0, 0) < c(1, 0)
        assert c(1, 0) == c(0, 1)
        assert c(1, 1) < c(2, 2)
        assert c(1, 2) == c(2, 1)
        assert c(1, 2) < c(2, 2)
        assert c(1, 3) < c(2, 2)
        assert c(10, 10) < c(40, 60)
        assert c(20, 20) > c(30, 40)
        assert c(20, 20) > c(25, 15)
        assert c(25, 15) == c(15, 25)
        assert c(10, 10) > c(1, 99)
        assert c(10, 20) < c(20, 40)
        assert c(10, 20) < c(15, 25)
        assert c(10, 10) < c(40, 60)
