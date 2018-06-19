from service.models.song_request import SongRequest


class TwilioMessage:
    def __init__(self, msg_to: str, msg_from: str, msg_body: str):
        self.msg_to = msg_to
        self.msg_from = msg_from
        self.msg_body = msg_body

        self._is_song_request = "unknown"
        self._song_request = None

    @property
    def is_song_request(self):
        if self._is_song_request == "unknown":
            self._is_song_request = len(self.msg_body.split(",")) == 3

        return self._is_song_request

    def extract_song(self) -> SongRequest:
        if not self.is_song_request:
            return False

        if self._song_request:
            return self._song_request

        title, artist, time = self.msg_body.split(",")
        self._song_request = SongRequest(
            artist=artist.lstrip(),
            title=title,
            time=time.lstrip()
        )

        return self._song_request

    @classmethod
    def apply(cls, params: dict):
        return TwilioMessage(
            msg_to=params["To"],
            msg_from=params["From"],
            msg_body=params["Body"]
        )
