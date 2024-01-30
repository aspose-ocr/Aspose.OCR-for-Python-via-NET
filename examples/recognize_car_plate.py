import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' add filters if you need '''
filters = ocr.models.preprocessingfilters.PreprocessingFilter()
filters.add(ocr.models.preprocessingfilters.PreprocessingFilter.auto_skew())

''' initialize image collection and put images into it '''
input = ocr.OcrInput(ocr.InputType.TIFF, filters)
input.add("Data\\OCR\\car.jfif")

''' change recognition options if you need '''
settings = ocr.CarPlateRecognitionSettings()

''' run recognition '''
res = api.recognize_car_plate(input, settings)

''' print result '''
print(res[0].recognition_text)