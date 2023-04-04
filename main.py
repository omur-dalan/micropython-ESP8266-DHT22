#Create a socket for httprequests
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


def read_temp():
    
    result_json = """{"""
    
    for sensor in sensors:
    
        sensor.measure()
        sleep(1)
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        result_of_single_sensor = """"sensor": [{ "temperature": """+str(temp)+ """},{"humidity": """+str(hum)+"""}]"""
        
        result_json = result_json + result_of_single_sensor
    
    result_json = result_json + """}"""
    
    return result_json



def web_page():
   
    html = read_temp()
    #html = """{"sensor-01": [{ "temperature": """+str(read_temp()[0])+ """},{"humidity": """+str(read_temp()[1])+"""}]}"""
    #If more than one sensor
    #html = """{"sensor-01": [{ "temperature": """+"10"+ """},{"humidity": """+"20"+"""}], "sensor-02": [{"temperature":"1"},{"humidity":"2"}]}"""

    return html



while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Rquest Content = %s' % request)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: application/json\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
        print(e)
