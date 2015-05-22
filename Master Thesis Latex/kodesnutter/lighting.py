def lighting():
    source, data = animation_q.get_nowait()
    d = data.split(' ')
    (a, r, g, b) = list(map(int, d)) # max values: 37889
    if source == 'lighting':
        p.fill(a,a,a)
        p.rect(200,100,200,100)
        p.fill(r,0,0,a)
        p.rect(100,300,100,100)
        p.fill(0,g,0,a)
        p.rect(250,300,100,100)
        p.fill(0,0,b,a)
        p.rect(400,300,100,100)
    else:
        pass