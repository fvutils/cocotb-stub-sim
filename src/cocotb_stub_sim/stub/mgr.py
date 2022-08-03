
import traceback

class CbClosure(object):

    def __init__(self, time_off, cb, ud):
        self.time_off = time_off
        self.cb = cb
        self.ud = ud

    def __call__(self):
        if self.cb is not None:
            self.cb(self.ud)

    def deregister(self):
        self.cb_id = -1

class Mgr(object):

    _inst = None

    def __init__(self):
        self.sim_time = 0
        self.precision = -9
        self.cb_l = []
        self._stop_request = False

    def run(self):
        """Propagates events as long as callbacks are registered"""
        while not self._stop_request and (len(self.cb_l) > 0):
            cb = self.cb_l.pop(0)
            self.sim_time += cb.time_off
            cb()
        
        return self._stop_request

    def stop_simulator(self):
        self._stop_request = True

    def get_sim_time(self):
        time = self.sim_time
        return ((time >> 32), time & 0xFFFFFFFF)

    def get_precision(self):
        return self.precision

    def register_timed_callback(self, t, cb, ud):
        ret = CbClosure(t, cb, ud)
        if len(self.cb_l) == 0:
            self.cb_l.append(ret)
        else:
            if ret.time_off < self.cb_l[0].time_off:
                self.cb_l.insert(0, ret)
            else:
                inserted = False
                for i in range(len(self.cb_l)):
                    if ret.time_off < self.cb_l[i].time_off:
                        inserted = True
                        self.cb_l.insert(i, ret)
                        break
                    else:
                        ret.time_off -= self.cb_l[i].time_off
                
                if not inserted:
                    self.cb_l.append(ret)

        return ret

    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = Mgr()
        return cls._inst

    @classmethod
    def init(cls):
        cls._inst = Mgr()
        return cls._inst

