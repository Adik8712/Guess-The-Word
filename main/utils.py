from random import randint

utf_letters = "ёйцукенгшщзхфывапролджэячсмитьъбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮЪЁ"


def validator_text(text: str):
    """
    Функция проверяет, соответствует ли переданный текст заданному формату.

    Аргументы:
        text (str): Входной текст, который требуется проверить.

    Возвращает:
        bool: True, если текст соответствует формату, и False в противном случае.

    Формат текста:
        - Текст должен состоять из одного слова (без пробелов).
        - В слове допускаются только буквы из стандартной UTF-8 кодировки, без цифр и специальных символов.

    Примеры:
        >>> validator_text("apple")
        False
        >>> validator_text("123")
        False
        >>> validator_text("hello world")
        False
        >>> validator_text("Привет")
        True
        >>> validator_text("привет")
        True
    """
    text: str = text.split()

    if len(text) > 1:
        return False
    
    for word in text:
        if word.isdigit():
            return False
        
        for letter in word:
            if letter not in utf_letters:
                return False
    
    return True


import re
import numpy as np
from difflib import SequenceMatcher


def preprocess_text(text):
    return re.sub(r'[^a-zA-Zа-яА-Я]', '', text.lower())


def check_word(word1: str, word2: str):
    word1 = preprocess_text(word1)
    word2 = preprocess_text(word2)
    
    if not word1 or not word2:
        return 0.0
    
    match = 2
    mismatch = -1
    gap_penalty = -1
    
    m = len(word1)
    n = len(word2)
    
    dp = np.zeros((m+1, n+1))
    for i in range(m+1):
        dp[i][0] = i * gap_penalty
    for j in range(n+1):
        dp[0][j] = j * gap_penalty
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = max(dp[i-1][j-1] + match, dp[i-1][j] + gap_penalty, dp[i][j-1] + gap_penalty)
            else:
                dp[i][j] = max(dp[i-1][j-1] + mismatch, dp[i-1][j] + gap_penalty, dp[i][j-1] + gap_penalty)
    
    nw_similarity = dp[m][n]
    max_score = max(m, n) * max(match, gap_penalty)
    nw_similarity = nw_similarity / max_score

    seq_matcher = SequenceMatcher(None, word1, word2)
    seq_similarity = seq_matcher.ratio()
    
    word1_bigrams = [word1[i:i+2] for i in range(len(word1)-1)]
    word2_bigrams = [word2[i:i+2] for i in range(len(word2)-1)]
    bigram_similarity = len(set(word1_bigrams) & set(word2_bigrams)) / max(len(set(word1_bigrams)), len(set(word2_bigrams)))
    
    total_similarity = (nw_similarity + seq_similarity + bigram_similarity) / 3
    
    return str(round(total_similarity * 100, 2)) + "%"
