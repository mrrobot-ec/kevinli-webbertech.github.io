# ANALYZING DATA AND GENERATING REPORTS

### **Forensic data analysis**

Digital forensics investigators spend most of their time analyzing their data. Data analysis is the culmination of a forensics investigation process. All your work for preparing, preserving, and acquiring data is essentially for making the analysis step possible. Analyzing data involves lots of searching and indexing is a technique that helps accelerate the search process. All major digital forensics products use indexing to improve their speed. Autopsy is an open source digital suite. It comes with powerful search and report generation features. It's nice that you can download Autopsy for free and try it for learning purposes. Commercial forensic software suites are pretty expensive and even cost prohibitive for individuals. If you work for a small organization with limited budget or have personal needs to conduct digital forensics investigations, Autopsy is a perfect tool for that. We have a couple of dedicated lessons to check out Autopsy more. It's also nice to explore specialized forensics utilities like Free Hex Editor Neo. You can download the latest version here and play with it. Neo provides some handy features like bit shifting and file type information extraction. Criminals are always trying to mislead you to protect their secrets, but a tool like Neo can help you see through all their deceptions. In addition to changing file extensions and shifting bids in a file, crooks and spies also hide information in picture files. A steganography tool like OpenStego is what they use to do this. We have a lesson for you too and you'll get a decent exposure. There are many more data analysis techniques and mechanisms out there. What we covered in this course is only the tip of the iceberg, Although not exhaustive, you'll still have a good feel for what analysis means in digital forensics by the time you're done with all the lessons in this chapter.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/forensic-data-analysis?autoSkip=true&resume=false&u=56745521#)

### **Indexing**

Indexing refers to the process of creating a catalog by going through an evidence drive and recording the location of each data item. To give you an analogy, creating an index for a book is similar to creating an index for an evidence drive. Once you create an index in your book, you can quickly go to a page of your interest based on a keyword. The same applies to your evidence drive. Once you have your indexing done, the speed of searching gets faster because there's now a direct mapping between your searched keyword and the location containing the keyword in your evidence drive. All you have to do is to go to a location according to the index without really having to do the same search over and over again every time you look for a keyword. Initially, indexing takes a long time because it has to go through every single data item in your evidence drive, and then somehow record the location of each data item according to its keyword. Therefore, typically when you try to acquire an image out of an evidence drive, you always have an option to do your indexing first. Indexing is sometimes referred to as preprocessing. When you see the word preprocessing, you should associate that word with indexing.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/indexing?resume=false&u=56745521#)

### **Searching**

Having the ability to search is essential in digital forensics. Investigators always need to do their keyword searches tied to their investigations. To demonstrate how a search is conducted in a computer forensic suite, let's use Autopsy. Autopsy is one of the most popular forensic software suites out there, and I highly recommend it. We'll start by creating a new case. Click on new case. Type your case name here. We'll use 001\. Choose your base directory. Desktop is fine. Click on next. And use case number 001\. You don't have to fill out the rest of the information. Click on finish. Now, the next step involves loading an image. I already created an image of an evidence drive. We'll be using that image for this exercise. Click on next. Click on disc image or VM file. Click on next. Click on browse. Choose usbimage.001. Click on open. By the way, you'll find this image file in your exercise files folder. Click on next. Click next again. Click on finish. Your image is now successfully loaded. Go ahead and select data sources. Click on the plus sign. Click on the plus sign again. Click on the plus sign next to uspimage.001, Select volume 2\. And you can see the files inside that volume. One of the things you notice here is files with X marks. What this means is that the files have been deleted. However, your computer forensic suite is able to detect these deleted files and you can even recover them by right clicking on the file. For example, dreamCar.jpg, choose extract files. We'll now try to export the file to our desktop. Click on open and click on save. You can see the file just created on my desktop. Let's see if I can open it. What a handsome car. Let's go ahead and close it. Next, we'll conduct a search, which is our primary mission here. We'll try to find all the files that contain a name, in this case, Bill. So click on keyword search. Type Bill. Click on search. Out of all the files we have on the disc image, only one file contains the name Bill. This is a handy feature not only for conducting your computer forensics investigation, but also for anything you do daily. You always need to look for a file according to a keyword. Of course, any computer software suite should have a feature like this, but they're not all created equally. How well their search feature works could be an excellent way to measure the quality of a computer forensic suite.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/searching?resume=false&u=56745521#)

### **Generating a Report**

Having the ability to auto generate a report is a very useful feature. Investigators usually auto generate their reports and use them as a starting point. We'll use Autopsy to demonstrate how you can auto generate a digital forensics report. We already loaded our image here. First, let's mark a piece of evidence so that it appears in my report. Let's pick a file here. I'm going to choose Dreamcar.jpg again. Do a right click and then choose add file tag. Next, select tag and comment. I'm going to leave a comment here as comment. Click on okay. And now you can see a new icon next to the file. Now the evidence is marked and it's going to show up in your report for sure. Let's generate our report. Go to tools. Choose generate report. The default choice is fine, which is HTML report. Click on next. Click on next, and click on finish. And click on close. To see your report, go to reports, click on HTML report. Double click it. Now, next to the star icon here, you can see tagged files. Click on the link and you can see the actual picture file. Let's go back. The evidence you marked is now showing up with your comments, which is comment. Any mainstream computer forensic software suite should come with a feature to auto generate a report like this. If you don't see it, you should seriously doubt the quality of the software.

- https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/generating-a-rreport?resume=false&u=56745521#

### **Case Study: Hex editor analysis of a file with a wrong extension**

Criminals often simply change the extensions of files to mislead computer forensics investigators. With the wrong file extension, it's difficult to know exactly what the original file type was. To find out the true file type, you could use a hex editor. We have a mystery file here called secret.jpg, and now I'll try to open it with a built-in Windows Photos app. The Windows Photos app is complaining because this is not a picture file and that's our clue that something's not right with a file extension. Let's close the Photos app and then open Neo. Click on file, open, open file, select secret.jpg. Click open. What you see here is all in hex numbers. These beginning bits of the file are called the file header signature. The file header signature of this file is 50 4b 03 04 14 00 06 00, and this is our clue. It also shows xml here, and we know somehow it's related to xml, but we don't know exactly what file type this is. For later use, let's copy the file header signature. Now let's close Neo. There are tables of file header signatures and they're called magic tables. You can find them on the internet. Based on the file header signature, one of the possibilities is Microsoft Office Word file. Let's try to change the file extension of the image file and see what happens. Let's try docx. docx presenter. It's asking whether I really want to do this, and the answer is yes. Let's open the file, and the file opens successfully, which means that this is the right file type and it says "This is a test\!"

- https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/case-study-hex-editor-analysis-of-a-file-with-a-wrong-extension?resume=false&u=56745521#

### **Hex editor analysis of a bit-shifted file**

Criminals shift bits in a file to hide a secret. To reveal the secret, you need a hex editor to shift the bits back to their original positions. Here we have a mystery file called secret.txt. Let me try to open this file using Notepad. I don't know what happened to the original text, but my strong suspicion is that the bits in the file might have been shifted. To know whether this is true or not, I'm going to open this file in Hex Workshop, a commercial hex editor. Compared to Neo, Hex Workshop provides more features in its trial version. Go to file, click open, choose secret.txt, click open. You'll find the secret.txt file in your exercise files folder. We'll try to shift the bits to your left first. Go to tools, operations, shift left. Choose eight bit unsigned byte. Click okay. It's still scrambled. Now let's try to shift the bits to your right. Let's close the file. Don't save the changes. Let's open the file again. File, open, Secret.txt. Click open. Now I'll try to shift the bits to my right. Go to tools, operations, shift right, choose eight bit unsigned byte. Click okay. As you can see, the secret message is now revealed. The admin password is password. Shifting bits is one of the most basic techniques you can use to hide your secret. Maybe you can use this technique to keep your secret diary.

- https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/hex-editor-analysis-of-a-bit-shifted-file?resume=false&u=56745521#

### **Case Study: Steganography**

Steganography is a way to hide information inside the picture file. Just like any other files, we store pictures in zeros and ones on our computer. The smallest unit of an image file is a pixel, and a picture file stores its pixel information and binary numbers in a REST or file format. Assume that we use 24 bits to store a pixel. If it changed the last bit of each pixel data, it won't change the pixel too much in terms of its color. This is why we can change a picture by embedding our own information into the pixel data and still make   it look indistinguishable from its original version. If we have 10,000 pixels in a picture, we have 10,000 opportunities to change their binary representations slightly. OpenStego is a free steganography tool. You can download it from this website. Let's give it a try. The user interface is relatively simple. The first field asks for a message to hide. I already created the secret message called message dot txt. You'll find the message dot txt file in your exercise file folder. Let's open it, and this is what it looks like. And let's go ahead and load it. The cover file refers to an image where my secret message will be embedded. It's this image file, olives dot png, and let's load it too. I'll put stego file as a new picture file to be created out of my cover file and will contain the secret message file information. I'll just specify the path and the file name here. We'll call the new file stego dot png. Click open. We have an option to encrypt the secret message. We'll use the default encryption algorithm, which is AES. We'll also provide the password. That's it. Click on hide data, and you see the stego file I just created. Let's open the stego dot png file side by side to the olives dot png file. Can you tell the difference? I can't. It'll be extremely difficult to find out which image is the one containing secrets, unless you created it.

- https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/case-study-steganography?resume=false&u=56745521#