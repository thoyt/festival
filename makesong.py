from jinja2 import Template


class Song(object):
    def __init__(self, bpm=120):
        self._bpm = bpm
        self._notes = []

    @property
    def bpm(self):
        return self._bpm

    @property
    def notes(self):
        return self._notes

    def as_xml(self):
        with open("songTemplate.jinja", "r") as f:
            t = Template(f.read())
        return t.render(
            bpm=self.bpm,
            notes=self.notes,
        )

    def add_note(self, word="la", beats="1.0", pitch="C4"):
        self._notes.append({
            "word": word,
            "beats": beats,
            "pitch": pitch,
        })

    def add_notes(self, notes):
        for note in notes:
            self.add_note(*note)


if __name__ == "__main__":
    s = Song()
    s.add_notes([
        ("heathcliff", "1.0,1.5", "Db5,Db5"),
        (None, '1.0'),
        ("its", "0.5", "F5"),
        ("me", "1.0", "Eb5"),
        ("i'm", "0.5", "Db5"),
        ("cathy", "0.5,1.0", "F5,Eb5"),
    ])
    print s.as_xml()