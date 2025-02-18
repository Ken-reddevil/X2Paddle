# 进行转换
python -m onnxsim ../dataset/crnn_lstm/crnn_lite_lstm.onnx ../dataset/crnn_lstm/crnn_lite_lstm_new.onnx --input-shape 1,3,32,32
x2paddle -f onnx -m ../dataset/crnn_lstm/crnn_lite_lstm_new.onnx -s pd_model_dygraph -df True
# 运行推理程序
python pd_infer.py
python benchmark_infer.py --use_gpu True --enable_trt True
python benchmark_infer.py --use_gpu True --enable_trt False
python benchmark_infer.py --use_gpu False --enable_mkldnn True
python benchmark_infer.py --use_gpu False --enable_mkldnn False
