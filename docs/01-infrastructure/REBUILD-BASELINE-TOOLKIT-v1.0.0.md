# Rebuild Baseline Toolkit v1.0.0

Toolkit construído e testado em 2026-09-19 para a fase G01.

## Componentes

- `01-RUN-NS1-REBUILD-BASELINE.sh` — orquestrador dos coletores existentes.
  SHA256: `7263fea598ab2d204113ca801d00ac719527351b57c4c4242ce378f053a77514`
- `02-COLLECT-RADIOPRINCIPAL-DELTA-READONLY.sh` — complemento de ownership, legado, paths e restore points.
  SHA256: `c1c5f08987a31a06bed3d94c1b63aa7c3ddea1514d80f182f01b5038129b44a8`
- `tools/verify_xray_bundle.py` — verificador de integridade; já versionado nesta branch.
- `tools/analyze_xray_bundle.py` — analisador automático; já versionado nesta branch.
- `tools/compare_xray_runs.py` — comparador histórico x atual; já versionado nesta branch.

## Coletores reconhecidos pelo runner

- `TPS-M00-02-DEEP-ENTERPRISE-FULL-RX-v4.1.0.sh`, SHA256 aprovado `f7247b16a6105eae8f4a4d32c3113cb2f0d05e157cae05813d3a0a8bff336c7d`.
- `STUDIOSAT-RADIOPRINCIPAL-FULL-XRAY-V2.sh`, Git blob `5128ecfb411bb4244cac7b383a2fef62bfc68aac`.
- `RESET00-NS1-FULL-XRAY-READONLY.sh`, Git blob `759f971169b968b70e63b4a72a2f1859a81271a3`.

## Testes executados

- `bash -n` dos dois shell scripts: PASS.
- `py_compile` das ferramentas Python: PASS.
- bundle histórico de 08/09 verificado: PASS.
- analisador executado sobre 268 comandos históricos: PASS.
- comparador self-test histórico contra ele mesmo: 0 mudanças, PASS.

Os shell scripts permanecem como artefatos entregáveis do toolkit até o conector permitir seu versionamento direto sem bloquear conteúdo executável.