import base64
import glob

for fname in glob.glob('./test_images/*png'):
    encoded = base64.b64encode(open(fname, "rb").read())
    output_file = fname[:fname.rindex('.')]+'.txt'
    with open(output_file, 'w') as f:
        f.write(str(encoded)[2:-1])
