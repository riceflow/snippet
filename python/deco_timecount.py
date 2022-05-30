import time

""" 時間を計測するデコレータ """
def time_decorator(view):
    def _inner(*args, **kwargs):
        start = time.time()
        response = view(*args, **kwargs)
        end = time.time()
        print(f"計測時間：{end - start}")
        return response
    return _inner

@time_decorator # デコレータの適用
def hoge():
    print("hoge")
