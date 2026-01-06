import speedtest

# cria o objeto
speed = speedtest.Speedtest()

# executa os testes
download = speed.download()
upload = speed.upload()
ping = speed.results.ping

# exibe em Mbps
print(f"Download: {download / 1_000_000:.2f} Mbps")
print(f"Upload: {upload / 1_000_000:.2f} Mbps")
print(f"Ping: {ping:.0f} ms")
