from screens.DelayScreen import DelayInput

def goToDelayScreen(widget):
    
    inputDelay = DelayInput(widget)
    widget.addWidget(inputDelay)
    widget.setCurrentIndex(widget.currentIndex()+1)