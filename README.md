Steganography: Hiding and Retrieving Messages in Images
This program implements Least Significant Bit (LSB) steganography to hide and retrieve messages within images.

Hiding a Message
To hide a message inside an image, use the following command:

 python3 imageLSB.py hide cover.png "THE MESSAGE"
 Output will be : Message successfully hidden in 'cover_new.png'

Retrieving a Message
To extract a hidden message from an image, use the following command:

python3 imageLSB.py retrieve cover_new.png
Output will be : Retrieved message: THE MESSAGE
