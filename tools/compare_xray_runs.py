#!/usr/bin/env python3
import argparse,csv,pathlib,tarfile,tempfile

def extract(src,td):
    src=pathlib.Path(src); td=pathlib.Path(td)
    if src.is_dir(): return src
    with tarfile.open(src,'r:*') as tf: tf.extractall(td,filter='data')
    roots=[p for p in td.iterdir() if p.is_dir()]
    return roots[0] if len(roots)==1 else td

def env(root):
    p=next(iter(root.rglob('final-status.txt')),None); d={}
    if p:
        for line in p.read_text(errors='replace').splitlines():
            if '=' in line:
                k,v=line.split('=',1); d[k]=v
    return d

def commands(root):
    p=next(iter(root.rglob('command-index.tsv')),None)
    if not p: return {}
    with p.open(errors='replace') as f:
        return {(r.get('section'),r.get('item')):r for r in csv.DictReader(f,delimiter='\t')}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('old'); ap.add_argument('new'); ap.add_argument('--out',required=True); a=ap.parse_args()
    out=pathlib.Path(a.out); out.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='rp-xray-old-') as t1, tempfile.TemporaryDirectory(prefix='rp-xray-new-') as t2:
        old=extract(a.old,t1); new=extract(a.new,t2); eo,en=env(old),env(new); co,cn=commands(old),commands(new)
        keys=sorted(set(co)|set(cn)); changes=[]
        for k in keys:
            r0=co.get(k,{}); r1=cn.get(k,{})
            s0=r0.get('status','MISSING'); s1=r1.get('status','MISSING')
            if s0!=s1: changes.append((*k,s0,s1))
        lines=['# Comparação de raio-X','',f'- OLD: `{eo.get("RUN_ID","unknown")}`',f'- NEW: `{en.get("RUN_ID","unknown")}`','',f'- Mudanças de status em comandos: **{len(changes)}**','', '## Mudanças']
        lines += [f'- `{s}/{i}`: `{o}` -> `{n}`' for s,i,o,n in changes] if changes else ['- nenhuma mudança de status detectada']
        (out/'XRAY-DIFF.md').write_text('\n'.join(lines)+'\n')
        with (out/'STATUS-CHANGES.tsv').open('w') as f:
            f.write('section\titem\told_status\tnew_status\n')
            for row in changes: f.write('\t'.join(row)+'\n')
        print('STATUS_CHANGES='+str(len(changes)))
        print('DIFF_OUT='+str(out))
if __name__=='__main__': main()
