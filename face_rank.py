import time

class FaceRankSystem:

    def __init__(self):
        self.face_list = []
        self.face_queue = []

    def add_face_by_time(self, timestamp, face, face_score):
        self.face_list.append([face, face_score])
        self.face_queue.append(timestamp)

    def mean_score_face_24h(self):
        now = time.time()
        for i in range(len(self.face_queue)):
            if self.face_queue[i] < now - 24 * 60 * 60:
                self.face_list.pop(i)
                self.face_queue.pop(i)
        return sum(self.face_list, key=lambda x: x[1]) / len(self.face_list)

    def max_score_face_24h(self):
        now = time.time()
        for i in range(len(self.face_queue)):
            if self.face_queue[i] < now - 24 * 60 * 60:
                self.face_list.pop(i)
                self.face_queue.pop(i)
        return max(self.face_list, key=lambda x: x[1])
