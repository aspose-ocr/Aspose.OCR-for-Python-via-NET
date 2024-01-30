import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' add filters if you need '''
filters = ocr.models.preprocessingfilters.PreprocessingFilter()
#filters.add(ocr.models.preprocessingfilters.PreprocessingFilter.auto_denoising())


''' initialize image collection and put images into it '''
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE, filters)
input.add("Data\\OCR\\table.png")


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
settings.detect_areas_mode=ocr.DetectAreasMode.TABLE


''' run recognition '''
res = api.recognize(input)
print(res[0].recognition_text)