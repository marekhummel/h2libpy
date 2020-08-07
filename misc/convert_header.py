import re

root = '../H2Lib/Library/'
file = 'bem3d.h'

rgx_sig = r'(?im)^(?!\s*\/?\*)(?:\s*HEADER_PREFIX )?(?P<restype>.*)(?:\n\s*| )(?P<funcname>.*)\((?P<params>(?:.|\n)*?)\);$'
rgx_prms = r'(?im)(?:const )?(?P<type>\w+?)\s?(?P<ptr>\**)\s?(?P<var>\w+?),'


def to_cstruct(type):
    if len(type) < 1: return type
    if type not in ['real', 'field'] and not type.startswith('c_'):
        return f'CStruct{type[0].capitalize()}{type[1:]}'
    return type


def replace_types(p):
    ctypes = {'void': 'c_void', 'bool': 'c_bool', 'uint': 'c_uint', 'size_t': 'c_size_t', 'char': 'c_char', 'int': 'c_int'}
    ret = p
    if (p.startswith('pc') and not p.startswith('pcluster') and not p.startswith('pchar')):
        ret = p[2:]
        ret = ctypes[ret] if ret in ctypes else to_cstruct(ret)
        ret = f'PTR({ret})'
    elif p.startswith('p'):
        x = len(re.match(r'^(p*).*$', p).group(1))
        ret = p[x:]
        ret = ctypes[ret] if ret in ctypes else to_cstruct(ret)
        ret = 'PTR(' * x + ret + ')' * x
    else:
        ret = ctypes[p] if p in ctypes else to_cstruct(p)
    ret = ret.replace('PTR(c_char)', 'c_char_p').replace('PTR(c_void)', 'c_void_p')
    return ret


with open(root + file, mode='r') as f:
    content = f.read()
    for m in re.finditer(rgx_sig, content):
        res = m.group('restype')
        func = m.group('funcname')

        params = []
        for p in re.finditer(rgx_prms, m.group('params') + ','):
            params.append('p' * len(p.group('ptr')) + p.group('type'))

        res = replace_types(res).replace('c_void', 'None')
        params = [replace_types(p) for p in params]

        print(f"{func} = get_func('{func}', {res}, [{', '.join(params)}])")
