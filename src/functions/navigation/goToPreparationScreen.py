from screens.PreparationScreen import PrepInput

def goToPreprationScreen(widget):
    
    inputPrep = PrepInput(widget)
    widget.addWidget(inputPrep)
    widget.setCurrentIndex(widget.currentIndex() + 1)