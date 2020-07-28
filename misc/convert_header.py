import re

root = '../H2Lib/Library/'
file = 'krylovsolvers.h'

rgx_sig = r'(?im)^(?!\s*\*)(HEADER_PREFIX )?(?P<restype>.*)(\n| )(?P<funcname>.*)\((?P<params>(?:.|\n)*?)\);$'


def to_cstruct(type):
    if type not in ['real', 'field'] and not type.startswith('c_'):
        return f'CStruct{type[0].capitalize()}{type[1:]}'
    return type


def replace_types(p):
    ret = p.replace('void', 'c_void').replace('bool', 'c_bool') \
            .replace('uint', 'c_uint').replace('size_t', 'c_size_t') \
            .replace('char', 'c_char')
    if (ret.startswith('pc') and not ret.startswith('pcluster') and not ret.startswith('pc_')):
        ret = f'PTR({to_cstruct(ret[2:])})'
    if ret.startswith('p'):
        x = ret.count('p')
        ret = 'PTR(' * x + to_cstruct(ret[x:]) + ')' * x

    ret = ret.replace('PTR(c_char)', 'c_char_p').replace('PTR(c_void)', 'c_void_p')
    return ret


with open(root + file, mode='r') as f:
    content = f.read()
    for m in re.finditer(rgx_sig, content):
        res = m.group('restype')
        func = m.group('funcname')

        params = []
        for p in m.group('params').split(','):
            if p == '': break
            param = p.strip().split(' ')
            if param[0] == 'const': param = param[1:]
            if len(param) != 2: params = ['ERROR']; break
            type, name = param
            while name.startswith('*'):
                type = 'p' + type
                name = name[1:]
            params.append(type)

        res = replace_types(res).replace('c_void', 'None')
        params = [replace_types(p) for p in params]

        print(f"{func} = get_func('{func}', {res}, [{', '.join(params)}])")
