def close(self):
    try:
        self.throw(GeneratorExit)
    except(GeneratorExit, StopIteration):
        pass
    else:
        raise RuntimeError("generator ignored GeneratorExit")
