from django.db import models
from django.contrib.auth.models import User

from main.utils import validator_text, check_word


class Word(models.Model):
    word = models.CharField(
        max_length=40, 
        verbose_name='Слово', 
        help_text='Слово, которое нужно отгадать'
    )
    is_guessed = models.BooleanField(
        default=False, 
        verbose_name='Отгадано', 
        help_text='Флаг, указывающий, было ли слово отгадано'
    )
    creator = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Создатель', 
        help_text='Пользователь, который создал слово'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания', 
        help_text='Дата и время создания записи'
    )

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        ordering = ["-created_at"]


class Room(models.Model):
    word = models.ForeignKey(
        Word, 
        on_delete=models.CASCADE, 
        verbose_name='Слово', 
        help_text='Слово, которое отгадывается в комнате'
    )
    creator = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Создатель', 
        help_text='Пользователь, который создал комнату'
    )
    is_closed = models.BooleanField(
        default=False, 
        verbose_name='Комната закрыта', 
        help_text='Флаг, указывающий, закрыта ли комната для новых участников'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания', 
        help_text='Дата и время создания записи'
    )

    def save(self, *args, **kwargs):
        if self.is_closed:
            self.word.is_guessed = True
            self.word.save()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Комната {self.id}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
        ordering = ["-created_at", "is_closed"]


class GuessedWord(models.Model):
    word = models.CharField(
        max_length=40, 
        verbose_name='Предложенное слово', 
        help_text='Слово, предложенное для отгадывания в комнате'
    )
    is_similar = models.CharField(
        max_length=8,
        verbose_name="Схожесть",
        blank=True,
        null=True,
        help_text="Процент совпадения с предполагаемым словом."
    )
    word_id = models.ForeignKey(
        Word, 
        on_delete=models.CASCADE, 
        verbose_name='Слово', 
        help_text='Идентификатор слова, которое отгадывается'
    )
    creator = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Создатель', 
        help_text='Пользователь, который предложил слово'
    )
    room = models.ForeignKey(
        Room, 
        on_delete=models.CASCADE, 
        verbose_name='Комната', 
        help_text='Комната, в которой было предложено слово'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания', 
        help_text='Дата и время создания записи'
    )

    def save(self, *args, **kwags) -> None:
        if validator_text(self.word) and validator_text(self.word_id.word):
            self.is_similar = check_word(self.word, self.word_id.word)
            return super().save(*args, **kwags)
        else:
            pass

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Предложенное слово'
        verbose_name_plural = 'Предложенные слова'
        ordering = ["-created_at"]

