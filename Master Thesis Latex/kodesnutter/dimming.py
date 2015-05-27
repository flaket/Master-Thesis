def dimming():
    global lights_activated
    source, light_level = animation_q.get_nowait()
    if source == 'dim' and lights_activated:
        light_level = int(float(light_level))
        if light_level < 200:
            r = light_level
            g = light_level
        else:
            r = 255
            g = 255
        b = light_level - 20
        p.background(200)
        p.fill(r,g,b)
        p.rect(0,0,600,600)
    elif data == 'LIGHTS':
        lights_activated = True
    else:
        pass