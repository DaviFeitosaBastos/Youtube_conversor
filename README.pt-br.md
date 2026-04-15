# Youtube Conversor

Uma ferramenta CLI em Python para baixar vídeos e áudios do YouTube, além de converter arquivos MP4 para GIF diretamente pelo terminal, com uma interface de menu limpa e interativa usando Rich.

---

## Funcionalidades

- Baixar vídeos do YouTube em **alta ou baixa resolução**
- Baixar **faixas de áudio** do YouTube como MP3
- Converter **vídeos MP4 para GIF** com configurações personalizáveis (FPS, resolução, corte)
- Visualizar **metadados do vídeo** antes de baixar
- Menu interativo com validação de URL
- Interface de terminal limpa usando Rich

---

## Estrutura do Projeto

```
Youtube_conversor/
├── main.py               # Ponto de entrada da aplicação
├── router.py             # Roteamento e lógica de navegação do menu
├── .gitignore            # Ignora arquivos desnecessários
├── README.md             # Versão em inglês
├── README.pt-BR.md       # Você está lendo agora
├── requirements.txt      # Todas as dependências
├── __init__.py
├── gifs/
│   └── # GIFs convertidos ficam aqui
├── web/
│   ├── __init__.py
│   └── log_utils.py     # Utilitários compartilhados (get_base_dir)(logger)
├── service/
│   ├── video_service.py  # Lógica de download de vídeo (alta res, baixa res, info)
│   ├── track_service.py  # Lógica de download de áudio
│   └── gif_service.py    # Lógica de conversão MP4 para GIF
└── ui/
    ├── __init__.py
    ├── display.py        # Helpers de exibição CLI (cabeçalhos, menus, carregamento)
    └── validation.py     # Validação de entrada (URL, inteiros, sim/não, seletor de arquivo)
```

---

## Configuração do Ambiente

**Crie e ative um ambiente virtual:**

```bash
python -m venv venv

# Linux
source venv/bin/activate

# Windows
venv\Scripts\Activate
```

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

> Certifique-se de que o `ffmpeg` está instalado no seu sistema e disponível no PATH.
>
> Linux: `sudo apt install ffmpeg`
>
> Windows: https://ffmpeg.org/download.html

---

## Uso

```bash
# linux
python3 main.py

# windows
python main.py
```

Navegue usando as opções numeradas:

```
================================
         Menu principal
================================
1 - Baixar vídeos do [YOUTUBE]
2 - Baixar faixa de áudio do [YOUTUBE]
3 - Converter MP4 para GIF
0 - Sair
```

Após selecionar uma opção, siga as instruções no terminal.

---

## Pastas de Saída

Todos os arquivos são salvos automaticamente na primeira execução:

| Pasta | Conteúdo |
|---|---|
| `videos/` | Vídeos MP4 baixados |
| `audios/` | Faixas MP3 baixadas |
| `gifs/` | Arquivos GIF convertidos |

---

## Gerando o Executável

```bash
pyinstaller --onefile --paths . main.py
```

> O executável será gerado na pasta `dist/`.
> As pastas `videos/`, `audios/` e `gifs/` são criadas automaticamente na primeira execução junto ao executável.

Para recompilar, limpe o build anterior primeiro:

```bash
rm -rf build/ dist/ main.spec
```

---

## Dependências

| Pacote | Finalidade |
|---|---|
| `pytubefix` | Download de vídeo/áudio do YouTube |
| `yt-dlp` | Backend alternativo de download |
| `ffmpeg-python` | Conversão de MP4 para GIF |
| `rich` | Estilização da interface no terminal |

---

## Roadmap

- [ ] Versão web da aplicação
- [ ] Interface gráfica no lugar do terminal
- [ ] Suporte a múltiplos provedores além do YouTube

---

## Notas

- Esta ferramenta é destinada apenas para uso pessoal.
- Respeite os Termos de Serviço do YouTube ao baixar conteúdo.

---

## Autor

[DaviFeitosaBastos](https://github.com/DaviFeitosaBastos)
