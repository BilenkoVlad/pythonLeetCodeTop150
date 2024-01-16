import pytest

from easy_level.best_time_to_buy_and_sell_stock import BestTimeToBuyAndSellStock


class TestBestTimeToBuyAndSellStock:
    @pytest.mark.parametrize("prices,output", [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ])
    def test_best_time_to_buy_and_sell_stock(self, prices, output):
        assert BestTimeToBuyAndSellStock.max_profit(prices=prices) == output
