# Gates de Validação

G00 documentação base.
G01 raio-X atual.
G02 legado inventariado.
G03 backup verificado.
G04 arquitetura LAB congelada.
G05 CI PASS.
G06 ingest LAB PASS.
G07 control/queue PASS.
G08 assets PASS.
G09 shadow PASS.
G10 failover PASS.
G11 reboot/falhas PASS.
G12 soak 6h PASS.
G13 soak 24h PASS.
G14 rollback LAB PASS.
G15 autorização explícita para produção.
G16 observação pós-cutover.
G17 legado desabilitado e observado.
G18 decommission autorizado.

Qualquer FAIL bloqueia o gate seguinte.
