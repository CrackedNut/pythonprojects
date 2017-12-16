from zipfile import ZipFile as zipf

zip = zipf("test.zip", "r")

zip.extract("troj.apk","./")

zip.close()

