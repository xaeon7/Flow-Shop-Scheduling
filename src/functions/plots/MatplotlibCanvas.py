from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 90):
        fig, self.gnt = plt.subplots(figsize = (width, height), dpi = dpi)
        super(MatplotlibCanvas, self).__init__(fig)
        fig.patch.set_facecolor('#F8F7FC')
        fig.tight_layout()