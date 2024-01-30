import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' add filters if you need '''
filters = ocr.models.preprocessingfilters.PreprocessingFilter()
#filters.add(ocr.models.preprocessingfilters.PreprocessingFilter.invert())


''' initialize image collection and put images into it '''
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE, filters)
input.add("Data\\OCR\\sample.png")


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
#settings.detect_areas_mode=ocr.DetectAreasMode.COMBINE
settings.detect_areas_mode=ocr.DetectAreasMode.TEXT_IN_WILD
#settings.detect_areas_mode=ocr.DetectAreasMode.NONE


''' run recognition '''
res = api.recognize(input)
print(res[0].recognition_text)