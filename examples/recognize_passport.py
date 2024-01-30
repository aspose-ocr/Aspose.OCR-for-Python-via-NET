import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' add filters if you need '''
filters = ocr.models.preprocessingfilters.PreprocessingFilter()
#filters.add(ocr.models.preprocessingfilters.PreprocessingFilter.auto_skew())

''' initialize image collection and put images into it '''
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE, filters)
input.add("Data\\OCR\\passport.jpg")

''' change recognition options if you need '''
settings = ocr.PassportRecognitionSettings()

''' run recognition '''
res = api.recognize_passport(input, settings)

''' print result '''
print(res[0].recognition_text)