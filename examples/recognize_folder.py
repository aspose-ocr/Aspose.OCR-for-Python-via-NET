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
input = ocr.OcrInput(ocr.InputType.DIRECTORY, filters)
input.add("Data\\OCR\\OCR")


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
settings.detect_areas_mode=ocr.DetectAreasMode.DOCUMENT


''' run recognition '''
res = api.recognize(input, settings)

''' print result '''
for r in res:
    print('------------------')
    print(r.recognition_text)