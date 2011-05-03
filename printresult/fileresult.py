import os

def writeresult(filename):
    mk_file(filename)

    archive = file(filename, 'w')
    archive.write(result)
    archive.close()

def mk_file(filename):
    try:
        os.mknod(filename)
    except OSError:
        os.remove(filename)
        os.mknod(filename)

def readresult(filename):
    archive = file(filename, 'r')
    result = archive.read()
    archive.close()
    return result

