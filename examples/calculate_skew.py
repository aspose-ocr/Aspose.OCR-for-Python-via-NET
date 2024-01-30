import aspose.ocr as ocr


''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')

''' initialize main class '''
api = ocr.AsposeOcr()

''' Create OcrInput and add images '''
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)
input.add("Data\\OCR\\skew_image.png")

''' calculate rotation '''
result = api.calculate_skew(input)

''' print result '''
print(result[0].angle)

''' case 2 '''

''' set filters '''
filter = ocr.models.preprocessingfilters.PreprocessingFilter();
filter.add(filter.rotate(15.0));

''' Create OcrInput and add images '''
images = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE, filter);
imgPath = "Data\\OCR\\table.png"
images.add(imgPath, 0, 1)

''' preprocess with filters and save on disc '''
output = ocr.ImageProcessing.save(images, "./")
images.clear()

''' calculate rotation after preprocessing '''
result = api.calculate_skew(output)

''' print result '''
print(result[0].angle)
output.clear()