import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' initialize image collection and put images into it '''
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)
input.add("Data\\OCR\\sample_spanish_line.png")

''' case 1 '''
''' run recognition '''
res = api.recognize_lines(input)

''' print result '''
print(res[0].recognition_text)


''' case 2 '''
''' set recognition options '''
settings = ocr.RecognitionSettings()
settings.recognize_single_line = True
settings.language = ocr.Language.SPA


''' recognize '''
result = api.recognize(input, settings)

''' print result '''
print(result[0].recognition_text)