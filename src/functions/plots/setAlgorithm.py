def setAlgorithm(self, widget):
      
    if not widget.delay and not widget.prep:
        self.flowShopSchedule.CDS()

    elif widget.delay and not widget.prep:
        self.flowShopSchedule.Delay(widget.delaySeq, widget.optimize)

    elif not widget.delay and widget.prep:
        self.flowShopSchedule.Preparation(widget.prepMatrix, widget.algo)

    elif widget.delay and widget.prep:
        self.flowShopSchedule.PreparationAndDelay(widget.prepMatrix, widget.delaySeq, widget.algo)