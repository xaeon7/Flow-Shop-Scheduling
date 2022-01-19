def goBack(self, widget):
    widget.setCurrentIndex(widget.currentIndex()-1)
    widget.removeWidget(self)