from threp.decode import load
from threp.static import FrameKey

class THReplay:
    def __init__(self, replay_file):
        self.__replay_info = load(replay_file)

    def get_info(self):
        return self.__replay_info

    def getBaseInfo(self):
        return self.__replay_info['base_info']

    def getBaseInfoDic(self):
        return self.__replay_info['base_infos']

    def getStageScore(self):
        return self.__replay_info['stage_score']

    def getActions(self):
        return self.__replay_info['actions']

    def getPlayer(self):
        return self.__replay_info['player']

    def getSlowRate(self):
        return self.__replay_info['slowrate']

    def getDate(self):
        return self.__replay_info['date']

    def getFrameCount(self):
        return self.__replay_info['frame_count']

    def getError(self):
        return self.__replay_info['error']