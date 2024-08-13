list = ["gif", "jpeg", "jpg", "png", "pdf", "txt", "zip" ]
name = input ("File name: ").strip().lower()
if list[0] in name:
    print ("image/gif")
elif list[1] in name:
    print ("image/jpeg", end='')
elif list[2] in name:
    print ("image/jpeg", end='')
elif list[3] in name:
    print ("image/png")
elif list[4] in name:
    print ("application/pdf")
elif list[5] in name:
    print ("text/plain", end='')
elif list[6] in name:
    print ("application/zip", end='')
else:
    print ("application/octet-stream")
