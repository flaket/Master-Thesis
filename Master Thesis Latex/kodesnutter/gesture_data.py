from serial import Serial

def gesture_recognition(q):
    ser = Serial('/dev/cu.usbmodem1431', 9600)
    buf = []
    while True:
        c = ser.read()
        if c == '\n':
            result = ''.join(buf)
            q.put(('gesture', result), block=True, timeout=1)
            buf = []
        elif c == '\r':
            pass
        else:
            buf.append(c)