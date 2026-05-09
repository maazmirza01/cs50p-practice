print("Enter your filename :", end=" ")
filename = input().lower().strip()

if filename.endswith(".gif"):
    print("filetype: image/gif")
elif filename.endswith(".jpg"):
    print("filetype: image/jpg")
elif filename.endswith(".jpeg"):
    print("filetype: image/jpeg")
elif filename.endswith(".png"):
    print("filetype: image/png")
elif filename.endswith(".pdf"):
    print("filetype: Web file/pdf")
elif filename.endswith(".txt"):
    print("filetype: text file/txt")
elif filename.endswith(".zip"):
    print("filetype: compressd file/zip")
else:
    print("application/octet-stream")
        