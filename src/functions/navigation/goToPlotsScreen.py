from screens.PlotsScreen import DisplayGantt

def goToPlotsScreen(widget):
    
    plots = DisplayGantt(widget)
    widget.addWidget(plots)
    widget.setCurrentIndex(widget.currentIndex() + 1)