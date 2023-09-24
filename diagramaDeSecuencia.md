# Grafico diseño felicitaciones 🤩
https://mermaid.live/edit#pako:eNqVVF1r2zAU_StCTyt4wXZiu9FDIW3GKLSjMMZgGMatddNo2JInyWVpyA_aQ__AXvPHJn8EXDVlGX4xuufcc-_V0d3SQnGkjBr82aAscCngQUOVS0KgsEqTL6YBLVR7UIO2ohA1SEu-rsGaRV1fKuuHLsHgEpdglfFDi8aqCqx4gkIo6UfvUBslIe8Cg-77i4uRFCNXGkETIY0FWQhokaO4Q4_UGbmWLjeUTk-TQkkCuliLx66ZEc5nLe610CdibxA14Ydex0C_8u6UlLh_5j24VKomd6CBFMCBcDRWSLCHafuNDdM5OgIf-3LOb1CGhEfgn_Z_KtTKlUQslvvfKyUV2RCpqnuNPfklxe_1poTKCQJB-ShAf69QGviB785OKdYniwoeUB64r4R9-oeORXrWUY5f7XUH7eV4NxyU_B_OukKt4VSTfHRW5vCGT_4r8XFTuZfadC4fnDWu2zGGp8TIbX8NZmi1BbcfDai77goEd4tg2ybIqV1jhTll7pfjCprS5jSXOwcFN8zPG1lQZnWDAW1q19Zhb1C2gtK4U_egKdvSX5RFcTJJzrM4m86iNJpnURLQDWVxmEzmYRjOoul5FqVpmuwC-qSUSxFOsvlsGqdRnCZZMssCily4XXTbr6puY3UK3zp4W8buL9Rjqis

```mermaid



sequenceDiagram
  actor Usuario
  participant WhatsAppBot
  participant BaseDeDatos
  participant Automatizacion
  participant Persona

  Usuario->>WhatsAppBot: Crear instancia
  WhatsAppBot->>BaseDeDatos: Inicializar con archivo
  BaseDeDatos->>BaseDeDatos: Abrir archivo
  BaseDeDatos->>BaseDeDatos: Leer datos
  BaseDeDatos-->>WhatsAppBot: Datos leídos
  loop Para cada destinatario
    WhatsAppBot->>Persona: Crear instancia
    WhatsAppBot->>Automatizacion: Crear instancia
    Persona->>Automatizacion: Número de teléfono y nombre
    Automatizacion->>WhatsAppBot: Llamar a enviar_mensaje()
    WhatsAppBot->>Automatizacion: Llamar a enviar_imagen()
    Automatizacion->>Automatizacion: Enviar imagen
    Automatizacion-->>WhatsAppBot: Imagen enviada
  end
  WhatsAppBot->>BaseDeDatos: Cerrar archivo
  BaseDeDatos->>BaseDeDatos: Guardar datos
  BaseDeDatos->>BaseDeDatos: Cerrar archivo
  BaseDeDatos-->>WhatsAppBot: Datos actualizados
  WhatsAppBot-->>Usuario: Mensajes enviados

    
```
