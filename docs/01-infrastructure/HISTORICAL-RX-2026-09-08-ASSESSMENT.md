# Avaliação do raio-X histórico de 08/09/2026

Pacote analisado: `TPS-NS1-FULL-RX-ns1-20260908T205701Z.tar.gz`.

## Integridade

- SHA256 do pacote: `70329f7343cd49247ef5fec186793825517be2b1417a91b5f4f560e717086a90`.
- Coletor: `TPS-M00-02-DEEP-ENTERPRISE-FULL-RX-v4.1.0.sh`.
- Schema: `TPS-RX-SCHEMA-4.1`.
- 69 seções de cobertura.
- 268 comandos indexados.
- Required: 37/37 PASS.
- PASS: 264.
- TIMEOUT opcionais: 3.
- FAIL opcional: 1.
- `LOCAL_RX_STATUS=PASS`.
- `PRODUCTION_GUARD=PASS_UNCHANGED`.
- Manifesto SHA256 validado integralmente.

## Decisão

Esse coletor enterprise é suficientemente amplo para continuar sendo a base global do raio-X do NS1. Não será reescrito do zero.

O rebuild adicionará uma camada complementar específica da Rádio Principal para mapear ownership de units e paths, referências legadas, scripts capazes de mutação, restore points de 13–17/09, estado dos publishers e evidência necessária para classificar o legado.

## Regra

A coleta de 08/09 é histórica e não pode autorizar remoção de nenhum componente atual. A classificação de legado depende de uma nova coleta do NS1.