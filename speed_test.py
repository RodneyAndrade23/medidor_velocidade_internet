import speedtest as st

server = st.Speedtest()
server.get_best_server()

down = server.download()
down = down / 1000000
print(f'Download speed: {down} Mb/s')


up = server.upload()
up = up / 1000000
print(f'Upload speed: {up} Mb/s')

ping = server.results.ping
print(f'Ping speed: {ping}')


