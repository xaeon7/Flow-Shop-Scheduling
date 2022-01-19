def goHome(self, widget):
    widget.setCurrentIndex(0)
    
    for i in range(widget.count(), 0, -1):
        widget.removeWidget(widget.widget(i))