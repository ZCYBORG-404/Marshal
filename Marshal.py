
import marshal, sys, os, time
B = '\x1b[34m'
R = '\x1b[31m'
G = '\x1b[32m'
W = '\x1b[0m'
Y = '\x1b[33;5m'

def banner():
    os.system('clear')
    print R + '     +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+'
    print W + '     |C|o|m|p|i|l|e| |M|a|r|s|h|a|l|'
    print R + '     +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+'
    print Y + '0{' + 39 * '=' + '}0'
    print Y + '|' + B + ' Coded by: ' + W + 'Zcyb0RG' + Y + '|'
    print Y + '|' + B + ' Github  : ' + W + 'https://github.com/ZCYBORG-404' + Y + '|'
    print Y + '|' + B + ' Insta   : ' + W + 'random_para.tolol' + Y + '|'
    print Y + '0{' + 39 * '=' + '}0\n'


try:
    banner()
    print G + 'Ex :/sdcard/ex.py'
    file = raw_input('\x1b[0m[\x1b[31mInput Your File Path\x1b[0m]> \x1b[36m')
    o = file.replace('.py', '')
except IndexError:
    print R + '[' + W + '!' + R + '] ' + W + 'there is an error\n'
    sys.exit()
except KeyboardInterrupt:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit\n'
    time.sleep(3)
    sys.exit()
except EOFError:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit\n'
    time.sleep(3)
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file not exist\n'
        sys.exit()

    try:
        code = compile(strng, '<debby>', 'exec')
        data = marshal.dumps(code)
    except TypeError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file already compiled\n'
        sys.exit()

fileout = open(o + 'enc.py', 'wb')
fileout.write('#Compiled By Zcyb0RG\n')
fileout.write('#dont forget to check my github: https://github.com/ZCYBORG-404\n')
fileout.write('#dont forget to follow my instagram random_para.tolol and zcyborg__\n')
fileout.write('#tidak ada system yang aman\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
banner()
print B + '[' + W + '+' + B + '] ' + G + 'file saved : ' + W + o + 'enc.py\n'
