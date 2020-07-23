def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        if stoplight[key] == 'yellow':
            stoplight[key] = 'red'    
        if stoplight[key] == 'red':
            stoplight[key] = 'green'
            
    
            