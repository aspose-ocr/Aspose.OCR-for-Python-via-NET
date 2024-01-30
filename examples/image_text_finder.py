import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')

''' initialize main class '''
api = ocr.AsposeOcr()

# set recognition options
sett = ocr.RecognitionSettings()

#search text
result = api.image_has_text("Data\\OCR\\sample.png", 'More', sett, True, True)

#print result
print(result)




#  TEXT COMPARE

#run comparison
result = api.compare_image_texts("Data\\OCR\\sample.png", "Data\\OCR\\skew_image.png", sett, True)

# print result
print(result)