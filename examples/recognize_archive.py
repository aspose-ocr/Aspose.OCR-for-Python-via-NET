import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' add filters if you need '''
filters = ocr.models.preprocessingfilters.PreprocessingFilter()
filters.add(ocr.models.preprocessingfilters.PreprocessingFilter.auto_skew())


''' initialize image collection and put archive into it '''
input = ocr.OcrInput(ocr.InputType.ZIP, filters)
input.add("Data\\OCR\\OCR.zip")


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
settings.detect_areas_mode=ocr.DetectAreasMode.PHOTO


''' run recognition '''
res = api.recognize(input)

''' print result '''
for r in res:
    print('------------------')
    print(r.recognition_text)