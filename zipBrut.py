import optparse
import zipfile
from threading import Thread


def extract_zip(zfile, password):
    try:
        password = bytes(password.encode('utf-8'))
        zfile.extractall(pwd=password)
        print("[+] Password Found: " + (password.decode("utf-8")) + '\n')
    except:
        pass


def main():
    parser = optparse.OptionParser("usage %prog " + '-f <zipfile> -d <dictionary>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname is None) | (options.dname is None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    main()