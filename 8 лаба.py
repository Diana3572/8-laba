from PIL import Image
def nn1():

    image = Image.open('открытка.jpg')
    cropped = image.crop((160, 150, 800, 420))
    cropped.show()
    cropped.save('открытка2.jpg')

print(nn1())

def nn2():
    from PIL import Image

    try:
        image1 = Image.open("Новый год.jpg")
        image2 = Image.open("День рождения.jpg")
        b = {"Новый год": image1, "День рождения": image2}
        a = input("Введите праздник (на русском языке): ")

        if a in b:
            img = b[a]
            img.show()
        else:
            print("Для этого праздника нет картинки")
    except FileNotFoundError:
        print("Файл с изображением не найден")

print(nn2())

