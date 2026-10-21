# project-game-snake
Game Snake

Классическая змейка на pygame: меню, экран Game Over, счет и рекорд в JSON.

## Управление
Стрелками или клавишами WSAD в игре, играть - Space или MouthButtonDown, выход в меню после проигрыша - Escape.

## Правила
Рост при поеданию, проигрыш при столкновении с собой или со стеной.

## Структура
- `snake project` - папка с кодом и изображениями
- `draw.py` - отрисовка игры 
- `game.py` - сама игра
- `main.py` - работа игры
- `objects.py` - объекты в игре: Apple, Snake
- `highscore.json` - файл JSON с максимальным счетом
- `score.py` - счет и рекорд с помощью JSON
- `images` - папка с изображениями
- `requirements.txt` - зависимости

## Установка зависимостей
```bash
pip install -r requirements.txt
```
