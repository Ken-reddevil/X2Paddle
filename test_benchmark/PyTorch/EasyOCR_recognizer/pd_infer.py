from __future__ import print_function
import paddle.fluid as fluid
import paddle
import sys
import os
import numpy as np

img = np.load("../dataset/EasyOCR_recognizer/img.npy")
pytorch_output = np.load("../dataset/EasyOCR_recognizer/result.npy")
f = open("result.txt", "w")
f.write("======EasyOCR recognizer: \n")
try:
    # trace
    paddle.enable_static()
    exe = paddle.static.Executor(paddle.CPUPlace())
    [prog, inputs, outputs] = fluid.io.load_inference_model(
        dirname="pd_model_trace/inference_model/",
        executor=exe,
        model_filename="model.pdmodel",
        params_filename="model.pdiparams")
    result = exe.run(prog, feed={inputs[0]: img}, fetch_list=outputs)
    df = pytorch_output - result
    if np.max(np.fabs(df)) > 1e-04:
        print("Trace Failed", file=f)
    else:
        print("Trace Successed", file=f)
except:
    print("!!!!!Failed", file=f)
f.close()
