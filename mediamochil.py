import time

__author__ = 'hemanth'
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from mochil_gui import Ui_MainWindow
import pyglet
from mutagen.easyid3 import EasyID3


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)
        self.debug = False

        headers = [self.tr("Title"), self.tr("Artist"), self.tr("Album"), self.tr("Year")]
        self.musicTable.setHorizontalHeaderLabels(headers)
        self.musicTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.musicTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.connect(self.musicTable, SIGNAL('cellPressed(int, int)'), self.tableClicked)

        self.volume.valueChanged.connect(self.volume_control)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setSingleStep(1)

        self.connect(self.open, SIGNAL("clicked()"), self.addFiles)
        self.dw_directory = "./"
        self.sources = []
        self.player = pyglet.media.Player()
        self.mediaLoad = None
        self.connect(self.horizontalSlider, SIGNAL("sliderReleased()"), self.seek)
        self.connect(self.pause, SIGNAL("clicked()"), self.player.pause)
        self.connect(self.play, SIGNAL("clicked()"), self.player.play)
        self.connect(self.next_item, SIGNAL("clicked()"), self.player.next_source)
        self.worker = DownloadWorker(self.player)
        self.worker.updateProgress.connect(self.set_progress)
        #self.worker.start()

    def volume_control(self):
        if self.debug:
            print " volume is now " + str(self.volume.value() + 1) + "%"
        self.player.volume = float(self.volume.value() + 1)/100

    def seek(self):
        position = self.translate(self.horizontalSlider.value(), 0.00, 99.00, 0.00, self.mediaLoad.duration)
        self.player.seek(position)
        if self.debug:
            print "seek " + str(position)

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

    def set_progress(self, progress):
        print progress
    def tableClicked(self, row, column):
        pass
        # oldState = self.mediaObject.state()
        #
        # self.mediaObject.stop()
        # self.mediaObject.clearQueue()
        #
        # self.mediaObject.setCurrentSource(self.sources[row])
        #
        # if oldState == Phonon.PlayingState:
        #     self.mediaObject.play()

    def addFiles(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, self.tr("Select Music Files"),
            QDesktopServices.storageLocation(QDesktopServices.MusicLocation),
            self.tr("Media Files (*.mp3 *.mp4 *.aac)")
        )
        if files == "":
            return
        index = len(self.sources)

        for mediafile in files:
            title = "unknown"
            artist, album, year = "", "", ""
            try:
                tag = EasyID3(mediafile)
                title = tag['title'][0]
                artist = tag['artist'][0]
                album = tag['album'][0]
                year = tag['date'][0]
            except:
                pass


            titleItem = QTableWidgetItem(title)
            titleItem.setFlags(titleItem.flags() ^ Qt.ItemIsEditable)
            artistItem = QTableWidgetItem(artist)
            artistItem.setFlags(artistItem.flags() ^ Qt.ItemIsEditable)
            albumItem = QTableWidgetItem(album)
            albumItem.setFlags(albumItem.flags() ^ Qt.ItemIsEditable)
            yearItem = QTableWidgetItem(year)
            yearItem.setFlags(yearItem.flags() ^ Qt.ItemIsEditable)

            currentRow = self.musicTable.rowCount()
            self.musicTable.insertRow(currentRow)
            self.musicTable.setItem(currentRow, 0, titleItem)
            self.musicTable.setItem(currentRow, 1, artistItem)
            self.musicTable.setItem(currentRow, 2, albumItem)
            self.musicTable.setItem(currentRow, 3, yearItem)
        for mediafile in files:
            self.mediaLoad = pyglet.media.load(mediafile)
            self.player.queue(self.mediaLoad)
        print self.mediaLoad.duration
        self.player.play()




class DownloadWorker(QThread):
    """
    Threading to  show a fancy progress
    """
    updateProgress = Signal(float)
    #You can do any extra things in this init you need, but for this example
    #nothing else needs to be done expect call the super's init
    def __init__(self,player):
        QThread.__init__(self)
        self.player = player


    #A QThread is run by calling it's start() function, which calls this run()
    #function in it's own "thread".
    def run(self):
        #Notice this is the same thing you were doing in your progress() function
        while(1):
            time.sleep(1)
            self.updateProgress.emit(float(self.player.time))
        return



app = QApplication(sys.argv)
form = MainWin()
form.show()
app.exec_()
