import zlib

sentence = 'Hello world! Python is great!'

sentence_compressed = zlib.compress(sentence.encode('utf-8'))

print(sentence_compressed)
print(zlib.decompress(sentence_compressed))
