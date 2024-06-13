def encryption(path, key):
    #opening the file, to read, 'with' will self close
    with open(path, 'rb') as file:
        #reading the image
        image = file.read()

    #converting image into a byte array, and storing it inot imageData variable
    imageData = bytearray(image)

    #loop to iterate through each pixel in resultImage and using enumerate to keep track
    for index, value in enumerate(imageData):
        #XOR operation, common formula for image manipulation
        imageData[index] ^= key

    #opening the file, to write, 'with' will selfclose
    with open(path, 'wb') as file:
        #writing the resuktant image
        file.write(imageData)

#taking the path for the image as input
path = input("Enter the path of the image to be Encrypted/Decrypted: ")
#taking the key value
print("Note: Key value should be same for Encryption and Decryption")
key = int(input("Please enter your key value: "))

encryption(path, key)