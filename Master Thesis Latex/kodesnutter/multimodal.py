import pyprocessing as p

def simple_multi_modal():
    source, recognized_input = animation_q.get_nowait()
    # non-blocking check for items in animation_q.
    # If queue is empty a Queue.Empty exception is raised.
    # data read from queue is a tuple of strings: (source, recognized_input)
    if source == 'gesture':
        p.fill(0, 102, randint(50,150))
        p.textSize(48)
    elif source == 'speech':
        p.fill(102, randint(50,150), 0)
        p.textSize(32)
    else:
        pass
    p.text(recognized_input, randint(50,550), randint(50,550))