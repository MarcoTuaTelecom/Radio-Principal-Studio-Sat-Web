#!/usr/bin/env python3
import argparse, hashlib, pathlib, tarfile, tempfile

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('bundle')
    args=ap.parse_args()
    src=pathlib.Path(args.bundle)
    with tempfile.TemporaryDirectory(prefix='rp-xray-verify-') as td:
        td=pathlib.Path(td)
        with tarfile.open(src,'r:*') as tf:
            tf.extractall(td, filter='data')
        roots=[p for p in td.iterdir() if p.is_dir()]
        root=roots[0] if len(roots)==1 else td
        mf=next(iter(root.rglob('MANIFEST.sha256')),None)
        if not mf:
            raise SystemExit('VERIFY_RESULT=FAIL_NO_MANIFEST')
        base=mf.parent.parent if mf.parent.name in ('integrity','summary') else mf.parent
        errors=[]
        for line in mf.read_text(errors='replace').splitlines():
            parts=line.split(None,1)
            if len(parts)!=2: continue
            expected,rel=parts
            p=base/rel.lstrip('*').strip()
            if not p.exists() or sha256(p)!=expected:
                errors.append(str(rel))
        print('MANIFEST_OK='+str(not errors).upper())
        print('ERRORS='+str(len(errors)))
        print('VERIFY_RESULT='+('PASS' if not errors else 'FAIL'))
        raise SystemExit(0 if not errors else 2)

if __name__=='__main__':
    main()
