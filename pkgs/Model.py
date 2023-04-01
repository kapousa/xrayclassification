# import pickle
#
# from ultralyticsplus import YOLO, postprocess_classify_output
#
#
# class Model:
#
#     def train_model(self):
#         try:
#             # load model
#             model = YOLO('keremberke/yolov8m-chest-xray-classification')
#
#             # set model parameters
#             model.overrides['conf'] = 0.25  # model confidence threshold
#
#             pickle.dump(model, open('../model/chest_xray_model.pkl', 'wb'))
#
#             return 1
#
#         except Exception as e:
#             return 0
#
#     def predict(self, image_path):
#         try:
#             # open a file, where you stored the pickled data
#             file = open('model/chest_xray_model.pkl', 'rb')
#
#             # dump information to that file
#             model = pickle.load(file)
#
#             # close the file
#             file.close()
#
#             # set image
#             image = image_path
#
#             # perform inference
#             results = model.predict(image)
#
#             # observe results
#             print(results[0].probs)  # [0.1, 0.2, 0.3, 0.4]
#             processed_result = postprocess_classify_output(model, result=results[0])
#             print(processed_result)  # {"cat": 0.4, "dog": 0.6}
#
#             for k,v in processed_result.items():
#                 processed_result.update({k : "{} %".format(round(float(v) * 100, 2))})
#
#             return processed_result
#
#         except Exception as e:
#             return "No prediction"
