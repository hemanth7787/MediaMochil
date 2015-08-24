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
    def play_next(self):
        raise NotImplementedError()

    @abstractmethod
    def play_previous(self):
        raise NotImplementedError()

    @abstractmethod
    def load(self, uri):
        raise NotImplementedError()

    @abstractmethod
    def pause(self):
        raise NotImplementedError()

    @abstractmethod
    def stop(self):
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

    @abstractmethod
    def is_media_loaded(self):
        raise NotImplementedError()

    @abstractmethod
    def is_playing(self):
        raise NotImplementedError()

    @abstractmethod
    def play_list_add(self, plist):
        raise NotImplementedError()

    @abstractmethod
    def play_list_remove(self, index):
        raise NotImplementedError()

    @abstractmethod
    def play_list_clear(self):
        raise NotImplementedError()

    @abstractmethod
    def get_current_play_list_item(self):
        raise NotImplementedError()

    @abstractmethod
    def play_list_is_empty(self):
        raise NotImplementedError()


class PygletEngine(Engine):
    def __init__(self):
        super(PygletEngine, self).__init__()
        self.player = pyglet.media.Player()
        self.media = None
        self.play_list = []
        self.current_playing = 0
        self.status_types = ["init", "paused", "playing", "eof"]
        self.status = self.status_types[0]

    def play(self):
        print self.status
        if self.status == self.status_types[1]:
            self.player.play()
        else:
            source_exist = True if self.media else False
            self.load(self.get_current_play_list_item())
            self.player.queue(self.media)
            if source_exist:
                self.player.next_source()
            else:
                self.player.play()
        if self.is_playing():
            self.status = self.status_types[2]
        else:
            self.status = self.status_types[0]

    def play_next(self):
        if len(self.play_list) != self.current_playing+1:
            self.current_playing += 1
            self.play()

    def play_previous(self):
        if self.current_playing != 0:
            self.current_playing -= 1
            self.play()

    def load(self, uri):
        self.media = pyglet.media.load(uri)

    def pause(self):
        self.player.pause()
        self.status = self.status_types[1]

    def stop(self):
        self.player.pause()
        self.status = self.status_types[0]
        self.player = pyglet.media.Player()
        self.media = None

    def seek(self, position):
        self.player.seek(position)

    def set_volume(self, value):
        self.player.volume = value

    def get_duration(self):
        return self.media.duration

    def get_volume(self):
        return self.player.volume

    def get_current_time(self):
        return self.player.time

    def is_media_loaded(self):
        return self.media is not None

    def is_playing(self):
        return self.player.playing

    def play_list_add(self, plist):
        self.play_list += plist

    def play_list_remove(self, index):
        self.play_list.remove(index)

    def play_list_clear(self):
        self.play_list = []
        self.current_playing = 0

    def get_current_play_list_item(self):
        return self.play_list[self.current_playing]

    def play_list_is_empty(self):
        return self.play_list == []
