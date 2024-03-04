from .psg import PSG
from .hypnogram import Hypnogram


class PSGHypnogramPair:
    def __init__(self, psg_file_path, hypnogram_file_path, session_id=None):
        self.psg = PSG(psg_file_path)
        self.hypnogram = Hypnogram(hypnogram_file_path)
        self.session_id = session_id
    
    def get_psg(self):
        return self.psg
    
    def get_hypnogram(self):
        return self.hypnogram