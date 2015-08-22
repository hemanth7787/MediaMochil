__author__ = 'Zion'
from abc import ABCMeta, abstractmethod
import pyglet


class Engine(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.player = None
        self.media = None

    @abstractmethod
    def play(self):
        raise NotImplementedError()

    @abstractmethod
    def load(self, uri):
        raise NotImplementedError()

    @abstractmethod
    def pause(self):
        raise NotImplementedError()

    @abstractmethod
    def seek(self, position):
        raise NotImplementedError()

    @abstractmethod
    def set_volume(self, value):
        raise NotImplementedError()

    @abstractmethod
    def get_volume(self):
        raise NotImplementedError()

    @abstractmethod
    def get_current_time(self):
        raise NotImplementedError()

    @abstractmethod
    def get_duration(self):
        raise NotImplementedError()


class PygletEngine(Engine):
    def __init__(self):
        super(PygletEngine, self).__init__()
        self.player = pyglet.media.Player()
        self.media = None

    def play(self):
        self.player.queue(self.media)
        self.player.play()

    def load(self, uri):
        self.media = pyglet.media.load(uri)

    def get_duration(self):
        return self.media.duration

    def pause(self):
        self.player.pause()

    def seek(self, position):
        self.player.seek(position)

    def set_volume(self, value):
        self.player.volume = value

    def get_volume(self):
        return self.player.volume

    def get_current_time(self):
        return self.player.time

    def is_media_loaded(self):
        return self.media is not None

    def is_playing(self):
        return self.player.playing
