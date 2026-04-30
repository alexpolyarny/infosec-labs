# Тестовый коммент 1

import typer


def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(
        False, "--formal", "-f", help="Использовать формальное приветствие."
    ),
):
<<<<<<< HEAD
 """
 Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
 """
=======
"""
 Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
"""
>>>>>>> 97a603d (сode style changes to hello.py 2)
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")


if __name__ == "__main__":
    typer.run(main)
