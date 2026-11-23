# Репозиторий `unterricht` — интерактивные материалы для уроков религии

Сайт: https://mythosymbolum.github.io/unterricht/ (GitHub Pages, ветка `main`, корень `/`).
Ученики открывают презентации на iPad по QR-коду без входа в аккаунт. Всё здесь публично:
никаких имён учеников, оценок и личных данных.

## Структура

```
index.html            ← главная страница, генерируется — вручную НЕ редактировать
lessons.json          ← список уроков (из него строится главная)
<schule>/<klasse>-<thema>/index.html   ← одна презентация = одна папка
_tools/build_site.py  ← собирает index.html из lessons.json
_tools/qr.py          ← QR-код (SVG/HTML/PDF) для папки урока
_tools/illus.py       ← иконки в стиле скетча (тот же стиль, что и в презентациях)
```

Школы: `gams` (Gebrüder-Asam-Mittelschule, классы 6, 8, 10), `wegs` (Wilhelm-Ernst-Grundschule, классы 1–4).
Имя папки: `kl<номер>-<тема>` строчными латинскими буквами, без умлаутов и пробелов
(ä→ae, ö→oe, ü→ue, ß→ss), например `gams/kl8-zehn-gebote/`, `wegs/kl4-pessach-ostern/`.

## Как выложить новую презентацию

1. Презентация — один самодостаточный файл `index.html` (стили, скрипты и шрифты внутри, без внешних ссылок),
   кладётся в новую папку `<schule>/kl<N>-<thema>/index.html`. Существующие папки не перезаписывать,
   если об этом не просили.
2. Добавить запись в `lessons.json`:
   `{"path": "gams/kl8-thema/", "schule": "GAMS", "klasse": "8", "titel": "...", "untertitel": "...", "icon": "kreuz"}`
   Допустимые `icon`: kelch, hostienschale, weihrauch, osterkerze, ewigeslicht, tabernakel, taufbecken,
   weihwasser, ambo, altar, kreuz, orgel, beichtstuhl, glocke, lektionar, kreuzweg, kirchturm.
3. `python3 _tools/build_site.py` — пересобрать главную.
4. `git add -A && git commit -m "<schule> Kl. <N>: <Thema>" && git push`
5. `python3 _tools/qr.py <schule>/kl<N>-<thema>/ "<Titel>"` — QR-плакат A4 в `qr_out/` (не коммитится),
   отправить PDF пользователю.
6. Через 1–2 минуты проверить, что страница открывается по адресу
   `https://mythosymbolum.github.io/unterricht/<schule>/kl<N>-<thema>/`, и сообщить пользователю ссылку.

Pages уже включён — в настройках репозитория ничего менять не нужно.

## Требования к презентациям (стиль пользователя)

- Язык материалов — немецкий; общение с пользователем — по-русски.
- Учитель — Religionslehrkraft (kath. RU, Bayern, LehrplanPLUS). Содержание богословски точное.
- Ученики работают сами на iPad: навигация стрелками, задания с кнопками «Prüfen / Lösung zeigen / Neu»,
  Drag & Drop с поддержкой касаний (pointer events) и вариантом «нажать карточку → нажать поле», баллы, Exit-Quiz.
- Фиксированная сцена 1200×800, масштабируется под экран; проверить скриншотами (1024×768) перед загрузкой.
- Скетч/комикс-стиль, тёплые цвета, профессиональные иллюстрации, без эмодзи.
- Жёлтые таблички «Arbeitsblatt N» показывают, когда переходить к бумажным листам.
