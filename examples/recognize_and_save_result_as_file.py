import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')

''' initialize main class '''
api = ocr.AsposeOcr()

''' set preprocessing options '''
filters = ocr.models.preprocessingfilters.PreprocessingFilter()
filters.add(ocr.models.preprocessingfilters.PreprocessingFilter.auto_skew())

''' Create OcrInput and add images '''
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE, filters)
input.add("Data\\OCR\\sample.png")
input.add("Data\\OCR\\table.png")

''' set recognition options '''
settings = ocr.RecognitionSettings()
settings.detect_areas_mode = ocr.DetectAreasMode.TABLE
settings.threads_count = 1
settings.language = ocr.Language.ENG


''' recognize '''
result = api.recognize(input, settings)

''' print result '''
print(result[0].recognition_text)


''' save result as multipage document '''
api.save_multipage_document("test.xml", ocr.SaveFormat.XML, result)
api.save_multipage_document("test.pdf", ocr.SaveFormat.PDF, result)