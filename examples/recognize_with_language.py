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
input.add("Data\\OCR\\chinese.png")


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
settings.language = ocr.Language.CHI


''' run recognition '''
res = api.recognize(input, settings)
print(res[0].recognition_text)

api.save_multipage_document("chinese1.txt", ocr.SaveFormat.TEXT, res)
res[0].save("chinese.json", ocr.SaveFormat.JSON)