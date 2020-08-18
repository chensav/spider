# encoding=utf-8
import json
import zlib
import websocket


def websocket_fmz():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    try:
        url1 = 'wss://www.fmz.com/ws_botvs_v1?compress=zlib'
        ws = websocket.create_connection(url1, timeout=10, headers=headers)
    except:
        url2 = 'wss://cn.fmzio.com/ws_botvs_v1?compress=zlib'
        ws = websocket.create_connection(url2, timeout=10, headers=headers)

    b = "120,156,101,142,65,11,194,48,12,133,255,75,206,69,218,233,152,244,170,32,130,120,208,227,40,210,214,176,150,117,171,180,213,131,226,127,55,14,189,40,185,124,121,121,121,201,3,6,44,46,158,65,182,176,193,114,136,38,150,53,22,237,3,48,56,94,77,182,201,27,156,100,18,190,142,93,236,50,40,6,23,157,244,144,105,183,21,141,168,23,75,197,126,129,241,169,42,254,1,193,249,31,214,162,34,84,148,23,244,216,129,132,187,59,173,246,116,174,196,30,71,234,9,173,182,14,65,242,55,133,96,180,237,183,244,51,8,26,221,48,101,31,201,55,159,53,207,23,52,75,58,244"
    b = [int(i) for i in b.split(",")]
    ws.send_binary(bytes(b))

    # b2 = "120,156,21,140,49,11,194,48,20,132,255,203,205,69,90,28,132,172,29,196,197,197,177,136,60,227,163,9,77,147,146,60,28,20,255,123,207,155,238,190,59,238,139,85,45,148,23,220,132,179,218,77,205,98,158,27,238,29,54,169,178,54,22,19,154,175,113,51,82,226,36,121,134,195,39,60,198,43,58,88,89,52,51,211,122,241,65,225,250,191,75,233,41,126,185,240,23,67,79,13,236,223,90,91,44,28,31,15,167,223,14,111,183,37,192"
    # b2 = [int(i) for i in b2.split(",")]
    # ws.send_binary(bytes(b2))

    for i in range(1):
        content_compress = ws.recv()
        # print(content_compress)
        content = zlib.decompress(content_compress)
        print(content.decode())
        # ws.send_binary(bytes(b))

    ws.close()


if __name__ == '__main__':
    websocket_fmz()
