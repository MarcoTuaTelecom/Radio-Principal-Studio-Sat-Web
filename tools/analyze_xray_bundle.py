#!/usr/bin/env python3
import argparse,csv,pathlib,tarfile,tempfile
from collections import Counter

def env(text):
    out={}
    for line in text.splitlines():
        if '=' in line:
            k,v=line.split('=',1); out[k.strip()]=v.strip()
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('bundle'); ap.add_argument('--out',required=True); a=ap.parse_args()
    out=pathlib.Path(a.out); out.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='rp-xray-analyze-') as td:
        td=pathlib.Path(td)
        with tarfile.open(a.bundle,'r:*') as tf: tf.extractall(td,filter='data')
        roots=[p for p in td.iterdir() if p.is_dir()]; root=roots[0] if len(roots)==1 else td
        final=next(iter(root.rglob('final-status.txt')),None)
        meta=env(final.read_text(errors='replace')) if final else {}
        cmd=next(iter(root.rglob('command-index.tsv')),None)
        rows=[]
        if cmd:
            with cmd.open(errors='replace') as f: rows=list(csv.DictReader(f,delimiter='\t'))
        counts=Counter(r.get('status','') for r in rows)
        bad=[r for r in rows if r.get('status') not in ('PASS','')]
        lines=['# Análise automática do raio-X','',f'- Host: `{meta.get("HOST_FQDN") or meta.get("HOST_SHORT") or "desconhecido"}`',f'- Coletor: `{meta.get("SCRIPT_NAME","desconhecido")}` versão `{meta.get("SCRIPT_VERSION","desconhecida")}`',f'- Required: `{meta.get("REQUIRED_PASS","?")}/{meta.get("REQUIRED_TOTAL","?")}`',f'- Status: `{meta.get("LOCAL_RX_STATUS","não informado")}`','', '## Status dos comandos']
        for k,v in sorted(counts.items()): lines.append(f'- {k}: {v}')
        lines += ['', '## Comandos não-PASS']
        for r in bad: lines.append(f'- `{r.get("section")}/{r.get("item")}`: {r.get("status")} rc={r.get("rc")}')
        if not bad: lines.append('- nenhum')
        (out/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
        print('COMMAND_ROWS='+str(len(rows)))
        print('NON_PASS='+str(len(bad)))
        print('ANALYSIS_OUT='+str(out))

if __name__=='__main__': main()
