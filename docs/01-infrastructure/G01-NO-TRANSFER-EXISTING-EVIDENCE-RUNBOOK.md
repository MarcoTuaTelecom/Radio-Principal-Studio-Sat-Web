# G01 — Auditoria do que já existe no NS1, sem depender de novo upload

## Correção operacional

A tentativa anterior presumiu que o pacote `RadioPrincipal-NS1-Rebuild-Baseline-Toolkit-v1.0.0.tar.gz` já existia em `/root`. A evidência do terminal mostrou que isso era falso. O NS1 já possui o runner `01-RUN-NS1-REBUILD-BASELINE.sh` e, mais importante, vários artefatos de raio-X atuais e históricos.

## Nova regra

Antes de executar qualquer novo raio-X pesado, primeiro inventariar e validar o que já existe no NS1.

## Artefatos atuais evidenciados no root

Entre outros:
- `NS1-XRAY-LATEST.tar.gz` e `.txt`;
- `RESET00-XRAY-RADIOPRINCIPAL-20260918T174349Z.txt`;
- `rp-19-09.tgz` e `.txt`;
- `rx-2026-09-19.tgz`, `.txt` e diretório correspondente;
- `studiosat-xray-20260919T100432Z`;
- `studiosat-xray-20260919T104549Z` e `.tar.gz`;
- `STUDIOSAT-FORENSIC-NS1-20260917T023826Z.tar.gz`;
- múltiplos XRAYs da Rádio Principal e do NS1.

## Toolkit G01 v1.1.0

Foram criados quatro scripts locais e validados com `bash -n`:

1. `RP-G01-01-INVENTORY-EXISTING-XRAYS.sh` — inventário de raios-X e forenses existentes.
2. `RP-G01-02-VERIFY-XRAY-BUNDLES.sh` — SHA256, teste de tar, contagem de entries e indício de manifest.
3. `RP-G01-03-MUTATION-SURFACE-MAP.sh` — mapeia scripts em `/root` que contêm comandos potencialmente mutantes, sem executá-los.
4. `RP-G01-04-RUN-EXISTING-BASELINE-AUDIT.sh` — orquestra os três e gera um bundle pequeno de evidência.

SHA256 dos scripts:
- `56d982c556570147ad0a5b3decc24d922fb2a3ad120ec65a942a6cbdb6147478`
- `72026f90267758a3189beeca85ff20a7e7ab0cc653af47bcb7401c72e7fa985e`
- `e9060ca84e4692c5a76306ceadc5dc38c1998bea87660381307c6c738898ea56`
- `47be925101f04751a913e150ae898cabebd680b2b19f3e338910ca033763d007`

O bundle do toolkit v1.1.0 possui SHA256 `fea9023ac94c4c381f2ff83b21786fd52cc58488b836a94230deb90ea9590b78`.

## Gate

Nenhum DELETE/DISABLE é autorizado nesta fase. O objetivo é selecionar e validar o melhor conjunto de evidências atuais e produzir o mapa de superfície de mutação.