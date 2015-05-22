def dimming():
    global lights_activated
    source, data = animation_q.get_nowait()
    if source == 'dim' and lights_activated:
        d = int(float(data))
        if d < 200:
            r = d
            g = d
        else:
            r = 255
            g = 255
        b = d - 20
        p.background(200)
        p.fill(r,g,b)
        p.rect(0,0,600,600)
    elif data == 'LIGHTS':
        lights_activated = True
    else:
        pass