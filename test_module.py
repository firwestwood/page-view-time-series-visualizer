import unittest
import time_series_visualizer
import matplotlib.pyplot as plt

class TimeSeriesVisualizerTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = time_series_visualizer.draw_line_plot()
        self.assertTrue(isinstance(fig, plt.Figure))

    def test_bar_plot(self):
        fig = time_series_visualizer.draw_bar_plot()
        self.assertTrue(isinstance(fig, plt.Figure))

    def test_box_plot(self):
        fig = time_series_visualizer.draw_box_plot()
        self.assertTrue(isinstance(fig, plt.Figure))

if __name__ == "__main__":
    unittest.main()
