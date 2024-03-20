from barcode.writer import ImageWriter
from barcode import EAN13

#последняя цифра генерируется автоматически на основе первых 12 цифр
#barcode_number = '123456789012'
barcode_number = '154545787878'

barcode = EAN13(barcode_number, writer=ImageWriter())
barcode.save('img_barcode')