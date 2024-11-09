from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
import test_module

# Generate and save figures
line_plot = draw_line_plot()
line_plot.savefig('line_plot.png')

bar_plot = draw_bar_plot()
bar_plot.savefig('bar_plot.png')

box_plot = draw_box_plot()
box_plot.savefig('box_plot.png')

# Run the tests
if __name__ == "__main__":
    test_module.main()
