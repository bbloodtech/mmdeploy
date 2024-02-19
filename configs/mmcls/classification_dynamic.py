_base_ = ['./classification_static.py']

onnx_config = dict(
    dynamic_axes={
        'input': {
            0: '8',
            1: '3',
            2: '48',
            3: '1280'
        },
        'output': {
            0: '8',
            1: '3'
        }
    },)
    # input_shape=[8, 3, 48, 1200],)
