#!/usr/bin/python
#encoding:utf8

def hexbytes(xs, group_size=1, byte_separator=' ', group_separator=' '):
    def ordc(c):
        return ord(c) if isinstance(c,str) else c
    
    if len(xs) <= group_size:
        s = byte_separator.join('%02X' % (ordc(x)) for x in xs)
    else:
        r = len(xs) % group_size
        s = group_separator.join(
            [byte_separator.join('%02X' % (ordc(x)) for x in group) for group in zip(*[iter(xs)]*group_size)]
        )
        if r > 0:
            s += group_separator + byte_separator.join(['%02X' % (ordc(x)) for x in xs[-r:]])
    return s

def hexprint(xs):
    r = []
    for x in xs:
        try:
            i = ord( x ) 
        except:
            i = x 
        if i > 31 and i < 127 :
            r.append( chr( i ) )
        else:
            r.append( '.' )
    return ''.join( r ) 
    # if want to show some chinese in hexdump, use following code
    def chrc(c):
        return c if isinstance(c,str) else chr(c)
    
    def ordc(c):
        return ord(c) if isinstance(c,str) else c
    
    def isprint(c):
        return ordc(c) > 31 if isinstance(c,str) else c > 31
    
    return ''.join([chrc(x) if isprint(x) else '.' for x in xs])



def hexdump(xs, group_size=8, byte_separator=' ', group_separator='  ', printable_separator=' | ', address=0, address_format='%08X', line_size=16, begin_address=0):

    import pdb
    if xs == None:
        return '--NONE--'
    if type( xs ) == unicode:
        xs = xs.encode('utf8')

    if address is None:
        s = hexbytes(xs, group_size, byte_separator, group_separator)
        if printable_separator:
            s += printable_separator + hexprint(xs)
    else:
        try:
            r = len(xs) % line_size
        except:
            pdb.set_trace()
        s = ''
        bytes_len = 0
        sameline = 0
        preline = line =  None
        for offset in range(0, len(xs)-r, line_size):
            chunk = xs[offset:offset+line_size]
            ibytes = hexbytes(chunk, group_size, byte_separator, group_separator)
            line = ibytes
            
            if preline == None:
                sameline = 1
            elif line == preline:
                # 如果当前行与前面的相等
                sameline += 1
            elif line != preline:
                # 超过了次数
                if sameline >= 2:
                    s += ' ' * 10 + '... ...  [repeat %s lines] ... ...\n' % ( sameline - 1 )
                    # 重复部分还需要展示下
                    s += (address_format + ': %s%s\n') % ( begin_address + address + offset - line_size, preline, printable_separator + hexprint( xs[offset-line_size:offset] ) if printable_separator else '')

            if line != preline:
                # 将当前数据追加
                s += (address_format + ': %s%s\n') % ( begin_address + address + offset, ibytes, printable_separator + hexprint(chunk) if printable_separator else '')
            
            if line != preline: sameline = 0
            preline = line
            bytes_len = len(ibytes)
        
        
        if sameline >=1:
            # 非整数部分正好是非重复的
            if sameline >=2 : s += ' ' * 10 + '... ... [repeat %s lines] ... ...\n' % ( sameline-1 )
            
            s += (address_format + ': %s%s\n') % ( begin_address + address + offset, ibytes, printable_separator + hexprint(chunk) if printable_separator else '')

        if r > 0:
            # 尾数部分
            offset = len(xs)-r
            chunk = xs[offset:offset+r]
            ibytes = hexbytes(chunk, group_size, byte_separator, group_separator)
            ibytes += byte_separator
            ibytes += ' '*(bytes_len - len(ibytes))
            s += (address_format + ': %s%s\n') % ( begin_address + address + offset, ibytes, printable_separator + hexprint(chunk) if printable_separator else '')
    
    return s

def printstr( buf, minlen = 5 ):
    # 显示字符串
    i = 0 
    xlen = len( buf ) 
    tmp = ''
    while True:
        if i >= xlen:
            break
        c = ord( buf[i] )
        if c == 0x0d or c == 0x0a or ( c > 31 and c < 127 ):
            tmp += buf[i]
        else:
            if len( tmp ) > minlen:
                print tmp
            tmp = ''
        i += 1


if __name__ == '__main__':
    '''
    print hexdump('a\nb\rc\f\vdef\t')
    print hexdump('a\nb\rc\f\vdef\t', printable_separator='  ')
    print hexdump('a\nb\rc\f\vdef\t', byte_separator=' ')
    print hexdump('a\nb\rc\f\vdef\t', byte_separator=' ', printable_separator='  ')
    print hexdump('Why don\'t you love the bluebells, love? 靠\x03 UTF-8的中文也行啊', byte_separator=' ', group_size=8, group_separator='  ', printable_separator='|  ', address=12)
    print hexdump('Why don\'t you love the bluebells, love?', byte_separator=' ', group_size=4, group_separator='-', printable_separator='  ', address=12)
    print hexdump('Why don\'t you love the bluebells, love?', byte_separator=' ', group_size=4, group_separator='-', printable_separator='  ', address=13, line_size=7)
    print hexdump( u'123' )
    x = 'a' * ( 16 +  16 * 6 + 16  ) + 'b' * 16 + 'c'*16 + 'd'*16 + 'e' * (16+ 16*10 + 16) + 'z' * 10
    print hexdump( x, begin_address=100 ) 
    '''
    import sys
    if len( sys.argv ) == 2:
        print hexdump( file( sys.argv[1] ).read() ) 
    else:
        while sys.stdin:
            line = sys.stdin.read()
            if not line:
                break
            print hexdump( line )
