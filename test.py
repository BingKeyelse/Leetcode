class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.threadpool = QtCore.QThreadPool()
        self.btnconnect_rasp.clicked.connect(lambda: self.start_worker_1())

    def start_worker_1(self):
        worker = Worker(self.start_stream_data_rasp, )
        self.threadpool.start(worker)

class Worker(QtCore.QRunnable):
    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs
	
    @pyqtSlot()
    def run(self):
        self.function(*self.args, **self.kwargs)