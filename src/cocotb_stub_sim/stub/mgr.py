
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

    def run(self):
        print("--> Mgr.run")
        while (len(self.cb_l) > 0):
            cb = self.cb_l.pop(0)
            self.sim_time += cb.time_off
            print("cb: %s" % str(cb))
            cb()
            pass
        print("<-- Mgr.run")

    def stop_simulator(self):
        self.ep.shutdown()

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
            print("TODO: insert callback")

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

